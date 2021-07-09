import Vue from 'vue'
import Vuex from 'vuex'
import { readCookie, setCookie, removeCookie } from "../functions/cookies.js"
import {fetchApi} from "../functions/fetchApi.js"
import router from '../router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    imgStorage: {
      uri: 'https://api.imgbb.com/1/upload',
      key: '92a2d2e3986a3c0235eff2cde14a62d8'
    },
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
      username: "Tú",
      first_name: "",
      last_name: "",
      pk: null
    },
    places: []
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
    addPlace(state, places) {
      state.places = places
    }
  },
  actions: {
    getUserData({ commit }, endpoint) {
      let token = readCookie("token");
      fetch(endpoint, {
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
          router.push({ name: "Login" });
        });
    },
    userPlaces({commit}, elements){
      if (elements.conf.headers.Authorization.includes("null"))
      elements.conf.headers.Authorization = "Bearer " + readCookie("token");
      fetchApi(elements.endpoint, elements.conf)
      .then((response) => {
        commit('addPlace', response)
      })
    
    }
  },
  modules: {
  },
  getters: {
    loggedIn(state) {
      return !!state.authentication.accessToken
    }
  }
})
