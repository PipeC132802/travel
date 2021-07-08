<template>
  <v-app class="app primary">
    <nav-bar v-if="loggedIn || authentication.userIsAuthenticated" />
    <v-main>
      <router-view />
    </v-main>
    <v-snackbar v-model="snackbar.status">
      {{ snackbar.msg }}

      <template v-slot:action="{ attrs }">
        <v-btn
          :color="snackbar.color"
          text
          v-bind="attrs"
          @click="
            changeSnackbarState({
              color: snackbar.color,
              msg: snackbar.msg,
              status: false,
            })
          "
        >
          cerrar
        </v-btn>
      </template>
    </v-snackbar>
  </v-app>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import { mapState, mapMutations, mapGetters } from "vuex";
export default {
  name: "App",
  components: {
    NavBar,
  },
  data: () => ({
    //
  }),
  computed: {
    ...mapState(["authentication", "snackbar"]),
    ...mapGetters(["loggedIn"])
  },
  methods: {
    ...mapMutations(["changeSnackbarState"]),
  },
};
</script>

<style>
::-webkit-scrollbar {
  display: none;
}
body {
  overflow: hidden;
}
</style>