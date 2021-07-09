<template>
  <div>
    <v-carousel
      height="200"
      :show-arrows="placeInfo.photos.length > 1 ? true : false"
      v-if="placeInfo.photos.length"
      hide-delimiters
    >
      <v-carousel-item
        v-for="(img, i) in placeInfo.photos"
        :key="i"
        :src="img.image"
      ></v-carousel-item>
    </v-carousel>
    <v-card-title class="card-info__title px-4">
      {{ placeInfo.place.name }}
    </v-card-title>
    <v-card-text class="pb-0">
      <v-row class="px-4" align-content="center">
        <img class="mr-2" height="20px" :src="status.icon" alt="" srcset="" />
        <span>{{ status.msg }}</span>
        <span v-if="placeInfo.date != null">Fecha: {{ placeInfo.date }}</span>
      </v-row>
      <v-radio-group
        dense
        :hide-details="true"
        class="px-0"
        v-model="statusVal"
        row
      >
        <v-radio label="Visitado" :value="1"></v-radio>
        <v-radio label="Favorito" :value="2"></v-radio>
        <v-radio label="Sueño" :value="3"></v-radio>
      </v-radio-group>
      <UploadPhotos v-on:imgsData="setImgsData" />
    </v-card-text>
    <v-card-actions class="px-3 pb-4">
      <v-btn outlined color="error darken-2"> Eliminar </v-btn>
      <v-btn :loading="loading" @click="savePlace" color="primary darken-2"> Guardar </v-btn>
    </v-card-actions>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import UploadPhotos from "../components/UploadPhotos.vue";
export default {
  name: "PlaceInfo",
  props: ["place"],
  components: {
    UploadPhotos,
  },
  data: () => ({
    imgs: [],
    apiEndpoint : "places/trips/",
    loading: false,
  }),
  computed: {
    ...mapState(["baseUrl"]),
    statusVal: {
      get: function () {
        return this.placeInfo.status;
      },
      set: function (value) {
        this.placeInfo.status = value;
      },
    },
    placeInfo: function () {
      return this.place;
    },
    status: function () {
      let status = {};
      switch (parseInt(this.place.status)) {
        case 0:
          status = {
            msg: "Posición temporal",
            icon: require("../assets/icons/place_clock.png"),
          };
          break;
        case 1:
          status = {
            msg: "Estuve aquí",
            icon: require("../assets/icons/place_check.png"),
          };
          break;
        case 2:
          status = {
            msg: "Guardado en favs!",
            icon: require("../assets/icons/place_star.png"),
          };
          break;
        case 3:
          status = {
            msg: "Sueño estar en este lugar!",
            icon: require("../assets/icons/place_love.png"),
          };
          break;
        default:
          break;
      }
      return status;
    },
  },
  methods: {
    ...mapActions({
      setPlace: "userPlaces",
    }),
    setImgsData(data) {
      this.imgs = data;
    },
    savePlace() {
      this.loading = true;
      let formData = this.placeInfo;
      formData.photos = this.imgs;
      console.log(formData);
      let data = {
        endpoint: this.baseUrl + this.apiEndpoint,
        conf: {
          headers: {
            "Authorization": "Bearer null",
            "Content-type": "application/json"
          },
          method: "POST",
          body: JSON.stringify(formData)
        }
      }
      
      this.setPlace(data)
      .finally(()=>this.loading =false)
    },
  },
};
</script>

<style>
.card-info__title {
  word-break: unset !important;
}
img {
  display: inline-block;
}
</style>