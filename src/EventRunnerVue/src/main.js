// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store/main'
import VueAxios from 'vue-axios'
import jwt_decode from 'jwt-decode'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

import Axios from 'axios'

Vue.prototype.$http = Axios;
const token = localStorage.getItem('token')
if (token) {
  Vue.prototype.$http.defaults.headers.common['Authorization'] = token
}




Vue.use(Buefy, {
  defaultIconPack: 'fa'

});
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
