import Vue from 'vue'
import Vuex from 'vuex'
import { readCookie, setCookie, removeCookie } from "../functions/cookies.js"
import router from '../router'

Vue.use(Vuex)
const url = "http://127.0.0.1:8000/api/v1.0/";
export default new Vuex.Store({
  state: {
    authentication: {
      accessToken: null,
      refreshToken: null,
      userIsAuthenticated: false,
    },
    baseUrl: "http://127.0.0.1:8000/api/v1.0/",
    snackbar: {
      color: "primary",
      msg: "",
      status: false
    },
    user: {
      username: "Tú"
    },
  },
  mutations: {
    changeSnackbarState(state, snackbar) {
      state.snackbar = snackbar;
    },
    setAuthInfo(state, auth) {
      state.authentication = auth;
      setCookie("token", state.authentication.accessToken, 6)
    },
    setUserInfo(state, user) {
      state.user = user;
    },

  },
  actions: {
    getUserData({ commit }) {
      let token = readCookie("token");
      fetch(url + "auth/user/", {
        headers: {
          "Authorization": "Bearer " + token
        }
      })
        .then((response) => {
          if (response.status >= 400) throw Error
          return response.json()
        })
        .then(response => { 
          commit('setUserInfo', response); 
          commit('setAuthInfo', {
            accessToken: token,
            refreshToken: null,
            userIsAuthenticated: true,
          }); 
        })
        .catch(() => {
          commit('setAuthInfo', {
            accessToken: null,
            refreshToken: null,
            userIsAuthenticated: false,
          });
          removeCookie("token")
          router.push({name:"Login"});
        }

        );
    },

  },
  modules: {
  },
  getters: {
    loggedIn(state) {
      
      return !!state.authentication.accessToken
    }
  }
})
