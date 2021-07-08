<template>
  <v-app-bar
    dark
    src="https://picsum.photos/seed/travel/1920/1080?random=1&blur=5"
    absolute
    class="nav-bar"
    
  >
    <div class="d-flex align-center">
      <v-img
        alt="Tu viaje"
        class="mx-3"
        contain
        src="@/assets/logo.png"
        transition="scale-transition"
        width="40"
      />

      <h2>TU VIAJE</h2>
    </div>      
    <v-spacer></v-spacer>
    <div>
      
      <v-btn icon class="mx-2">
        <v-avatar color="primary" size="35">{{
          user.username.slice(0, 1)
        }}</v-avatar>
      </v-btn>
      <v-btn color="error" icon @click="logout">
        <v-icon>mdi-logout</v-icon>
      </v-btn>
    </div>
  </v-app-bar>
</template>

<script>
import { mapState, mapMutations } from "vuex";
export default {
  name: "NavBar",
  data: () => ({
    logoutEndpoint: "auth/logout/",
  }),
  computed: {
    ...mapState(["user", "baseUrl", "authentication"]),
  },

  
  methods: {
    
    ...mapMutations(["setAuthInfo"]),
    
    logout() {
      fetch(this.baseUrl + this.logoutEndpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + this.authentication.accessToken,
        },
      }).then(() => {
        let authentication = {
          accessToken: null,
          refreshToken: null,
          userIsAuthenticated: false,
        };
        this.setAuthInfo(authentication);
        this.$router.push({ name: "Login" });
      });
    },
  },
};
</script>


<style >
.nav-bar{
  z-index: 1000;
}
</style>

