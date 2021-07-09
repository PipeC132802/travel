<template>
  <div>
    <v-file-input
      :disabled="disabled"
      :rules="rules"
      accept="image/png, image/jpeg, image/bmp"
      placeholder="Selecciona tus fotos"
      prepend-icon="mdi-camera"
      label="Fotos"
      multiple
      v-model="photos"
      @change="previewPhotos"
    ></v-file-input>
    <div v-for="(pic, i) in photos" :key="i"></div>
    <v-dialog persistent v-model="dialog" width="450">
      <v-card>
        <v-carousel
          height="300"
          :show-arrows="photos.length > 1 ? true : false"
          v-if="photos.length"
          :continuous="false"
          hide-delimiters
        >
          <v-carousel-item v-for="(img, i) in imgsUrl" :key="i" :src="img.src">
            <v-row class="pa-6 carousel-row" justify="end">
              <v-chip
                @click="deletePic(i)"
                class=""
                color="error darken-1"
                text-color="white"
              >
                Eliminar
                <v-icon right>mdi-delete</v-icon>
              </v-chip>
            </v-row>
            <v-text-field
              solo
              dense
              class="mx-5"
              label="Título"
              @keypress="changeTitle(i)"
              :id="'title_' + i"
            ></v-text-field>
          </v-carousel-item>
        </v-carousel>
        <v-card-actions>
          <v-btn
            @click="savePhotos"
            :loading="loading"
            color="primary darken-2"
            class="ml-auto"
          >
            <v-icon left>mdi-upload</v-icon>
            Cargar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "UploadPhotos",
  data: () => ({
    dialog: false,
    loading: false,
    disabled: false,
    imgsResponse: [],
    errors: 0,
    rules: [
      (imgs) => {
        let imgsCount = null;
        try {
          imgsCount = imgs.length;
        } catch (error) {
          imgsCount = 0;
        }
        if (imgsCount > 5) {
          return "Max. 5 imágenes";
        }
        return true;
      },
    ],
    photos: [],
    imgsUrl: [],
  }),
  computed: {
    ...mapState(["imgStorage"]),
  },
  methods: {
    previewPhotos() {
      if (this.photos.length > 0 && this.photos.length < 6) {
        this.photos = this.photos.slice(0, 4);
        this.dialog = true;
        this.photos.forEach((photo) => {
          this.imgsUrl.push({ src: URL.createObjectURL(photo), title: "" });
        });
      }
    },
    deletePic(index) {
      this.photos.splice(index, 1);
      this.imgsUrl.splice(index, 1);
      if (this.photos.length < 1) {
        this.dialog = false;
      }
    },
    changeTitle(index) {
      let textInput = document.getElementById("title_" + index);
      this.imgsUrl[index].title = textInput.value;
    },
    savePhotos() {
      this.loading = true;
      for (const [index, photo] of this.photos.entries()) {
        let data = new FormData();
        data.append("image", photo);
        data.append("key", this.imgStorage.key);
        fetch(this.imgStorage.uri, {
          method: "POST",
          body: data,
        })
          .then((resp) => {
            if (resp.status >= 400) throw Error;
            return resp.json();
          })
          .then((resp) => {
            let objResp = {
              image: resp.data.url,
              name: this.imgsUrl[index].title,
              meta: resp.data,
            };
            this.imgsResponse.push(objResp);
          })
          .catch(() => (this.errors += 1))
          .finally(() => {
            if (index == this.photos.length - 1) {
              this.loading = false;
              this.dialog = false;
              this.disabled = true;
              this.$emit("imgsData", this.imgsResponse);
            }
          });
      }
    },
  },
};
</script>

<style>
.carousel-row {
  height: 270px;
}
</style>

