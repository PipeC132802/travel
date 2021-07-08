<template>
  <div>
      <v-carousel v-if="placeInfo.photos.length" hide-delimiters>
    <v-carousel-item
      v-for="(img,i) in placeInfo.photos"
      :key="i"
      :src="img.image"
    ></v-carousel-item>
  </v-carousel>
    <v-card-title> {{ placeInfo.place.name }} </v-card-title>

  </div>
</template>

<script>
export default {
  name: "PlaceInfo",
  props: ["place"],
  data: () => ({
  }),
  computed: {
    placeInfo: function () {
      return this.place;
    },
  },
  methods: {
    funs() {
      console.log("over");
    },
  },
};
</script>

<style>

#overlay {
  z-index: -1 !important;
}
</style>