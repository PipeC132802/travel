<template>
  <v-img
    src="https://cdn.pixabay.com/photo/2016/01/09/18/27/journey-1130732_960_720.jpg"
    class="login-div"
  >
    <v-container class="login-container">
      <v-row
        justify="center"
        align-content="center"
        class="login-container__row"
      >
        <v-col cols="12" class="login-container__row_col white--text" md="6">
          <h1>Inicia sesión</h1>
          <v-form ref="form" @submit.prevent="login" class="">
            <v-text-field
              v-model="username"
              label="Usuario"
              required
              color="primary darken-2"
              :rules="[rules.required]"
            ></v-text-field>
            <v-text-field
              v-model="password"
              label="Contraseña"
              required
              :type="!eye ? 'password' : 'text'"
              :append-icon="eye ? 'mdi-eye' : 'mdi-eye-off'"
              :rules="[rules.required]"
              color="primary darken-2"
              @click:append="toggleEye"
            ></v-text-field>
            <a class="login-container__a">¿Olvidaste tu contraseña?</a>
            <v-btn
              color="primary darken-2"
              class="mt-3"
              type="submit"
              block
              :loading="loading"
            >
              Iniciar sesión
            </v-btn>
            <p  class="black--text mt-3">
              ¿No tienes una cuenta?
              <a class="login-container__a">Regístrate! </a>
            </p>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </v-img>
</template>
<script>
import { mapState, mapMutations } from "vuex";
export default {
  data: () => ({
    username: "",
    password: "",
    eye: false,
    valid: false,
    loading: false,
    apiEndpoint: "auth/login/",
    rules: {
      required: (value) => !!value || "Campo obligatorio.",
    },
  }),

  computed: {
    ...mapState(["baseUrl"]),
  },

  methods: {
    ...mapMutations(["changeSnackbarState", "setAuthInfo", "setUserInfo"]),
    toggleEye() {
      this.eye = !this.eye;
    },
    login() {
      if (this.password.length < 1 && this.username.length < 1) {
        this.changeSnackbarState({
          color: "error",
          msg: "Todos los campos son obligatorios.",
          status: true,
        });
        return 0;
      }
      this.loading = true;
      let data = {
        username: this.username,
        password: this.password,
        email: "",
      };
      fetch(this.baseUrl + this.apiEndpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })
        .then((response) => {
          if (response.status >= 400) {
            throw Error;
          }
          return response.json();
        })
        .then((response) => {
          let authentication = {
            accessToken: response.access_token,
            refreshToken: response.refresh_token,
            userIsAuthenticated: true,
          };
          this.setAuthInfo(authentication);
          this.setUserInfo(response.user);
          this.$router.push({name:"Home"})
        })
        .catch(() => {
          this.changeSnackbarState({
            color: "error",
            msg: "Credenciales inválidas",
            status: true,
          });
          this.password = "";
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
};
</script>
<style >

a{
  color: var(--v-primary-darken2) !important;
}
p{
  text-align: center;
}
.login-container__a:hover {
  text-decoration: underline;
  cursor: pointer;
  color: var(--v-primary-darken2);
}
.login-div,
.login-container {
  width: 100vw;
  height: 100vh;
}

.login-container__row {
  height: 100%;
  padding: 50px;
}
.login-container__row_col {
  background-color: rgba(95, 95, 95, 0.281);
  height: 66%;
  max-height: 600px;
  border-radius: 10px;
  padding: 20px;
  backdrop-filter: blur(5px);
  
}
</style>