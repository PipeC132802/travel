<template>
  <div>
    <div class="pa-3" id="search-places">
      <GmapAutocomplete
        class="app-bar--search"
        placeholder="Buscar..."
        @place_changed="setPlace"
        @focus="overlay = true"
        @focusout="overlay = false"
      />
    </div>

    <GmapMap
      :options="mapOptions"
      :center="center"
      :zoom="zoom"
      map-type-id="terrain"
      style="width: 100vw; height: 100vh"
      ref="mapRef"
    >
      <GmapMarker
        :key="index"
        v-for="(place, index) in places"
        :position="place.place"
        :icon="iconPreferences(place)"
        @click="pinSelected(place)"
        @focusout="show = false"
      />
    </GmapMap>
    <v-dialog v-model="show" width="400">
      <v-card class="mx-auto" elevation="3">
        <place-info :place="currentPlace" />
        
      </v-card>
    </v-dialog>
    <v-overlay @click="overlay = false" :value="overlay"></v-overlay>
  </div>
</template>

<script>
import { mapActions, mapMutations, mapState } from "vuex";
import PlaceInfo from "../components/PlaceInfo.vue";
export default {
  name: "Home",
  components: {
    PlaceInfo,
  },
  data: () => ({
    show: false,
    overlay: false,
    currentPlace: null,
    mapOptions: {
      zoomControl: true,
      mapTypeControl: false,
      scaleControl: true,
      streetViewControl: false,
      rotateControl: false,
      fullscreenControl: false,
      disableDefaultUi: true,
      maxZoom: 15,
      minZoom: 3,
      restrictions: {
        north: 0,
        south: 0,
        west: 0,
        east: 0,
      },
    },
    center: {
      lat: 0,
      lng: 0,
    },
    zoom: 3,
    endpoints: {
      user: "auth/user/",
      places: "places/trips/",
    },
    showInfo: false,
  }),
  created() {
    this.checkUser(this.baseUrl + this.endpoints.user);
  },
  mounted() {
    let conf = {
      headers: {
        Authorization: "Bearer " + this.authentication.accessToken,
      },
      method: "GET",
    };
    let paramenters = {
      endpoint: this.baseUrl + this.endpoints.places,
      conf: conf,
    };
    this.getPlaces(paramenters);
  },
  computed: {
    ...mapState(["baseUrl", "authentication", "places", "user"]),
  },
  methods: {
    ...mapActions({
      checkUser: "getUserData",
      getPlaces: "userPlaces",
    }),
    ...mapMutations(["addPlace"]),
    infoClicked(context) {
      console.log(context);
    },
    pinSelected(place) {
      this.currentPlace = place;
      this.$refs.mapRef.$mapPromise.then((map) => {
        this.center = {
          lat: map.center.lat(),
          lng: map.center.lng(),
        };
        this.zoom = map.zoom;
      });
      setTimeout(() => {
        this.center = place.place;
        this.zoom = 12;
        this.show = true;
      }, 50);
    },
    setPlace(place) {
      this.overlay = false;
      let geometry = {
        lng: place.geometry.location.lng(),
        lat: place.geometry.location.lat(),
        name: place.formatted_address
      };
      var place_obj = {
        date: null,
        photos: [],
        place: geometry,
        status: 0,
        user: this.user.pk,
      };
      let placesTemp = this.places;
      placesTemp.push(place_obj);
      this.addPlace(placesTemp)
      this.center = geometry;
      this.zoom = 10;
    },
    iconPreferences(place) {
      let url = "";
      switch (place.status) {
        case 0:
          url = require("../assets/icons/place_clock.png");
          break;
        case 1:
          url = require("../assets/icons/place_check.png");
          break;
        case 2:
          url = require("../assets/icons/place_star.png");
          break;
        case 3:
          url = require("../assets/icons/place_love.png");
          break;

        default:
          return "";
      }
      return { url: url,
      scaledSize: {width: 20, height: 30, f: 'px', b: 'px',},
      size: {width: 20, height: 30, f: 'px', b: 'px',},
       };
    },
  },
};
</script>
<style scoped>
#search-places {
  position: absolute;
  left: calc(30vw);
  top: 75px;
  z-index: 10;
}
.app-bar--search {
  width: 40vw;
  outline: transparent;
  background: white;
  padding: 15px;
  border-radius: 5px;
}
.card-info {
  position: absolute;
  bottom: 20%;
  left: 40%;
  z-index: 10000000;
}
</style>