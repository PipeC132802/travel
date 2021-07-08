<template>
  <GmapMap
    :options="mapOptions"
    :center="{ lat: 0, lng: 0 }"
    :zoom="3"
    map-type-id="terrain"
    style="width: 100vw; height: 100vh;"
  >
  </GmapMap>
</template>

<script>
import {mapActions} from "vuex";
export default {
  name: "Home",
 
  data: () => ({
    mapOptions: {
      zoomControl: true,
      mapTypeControl: false,
      scaleControl: true,
      streetViewControl: false,
      rotateControl: false,
      fullscreenControl: false,
      disableDefaultUi: true,
      maxZoom: 10,
      minZoom: 3,
      restrictions: {
        north: 0,
        south: 0,
        west: 0,
        east: 0,
      },
    },
  }),
  created() {
    this.checkUser();
  },
  methods:{
    ...mapActions({
      checkUser: "getUserData",
    }),
  }
};
</script>
