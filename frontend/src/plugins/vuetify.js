import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
      options: {
        customProperties: true,
      },
    themes: {
      light: {
        primary: '#436ff5',
        secondary: '#0045c1',
        accent: '#f09845',
        error: '#C2151B',
        info: '#8183F0',
        success: '#2BCB4B',
        warning: '#F0DC4C'
      },
    },
  },
});
