import { createApp } from 'vue'
// import './style.css'
import App from './App.vue'
import router from './router/router.js'
import vue3GoogleLogin from 'vue3-google-login'

const app = createApp(App);
app.use(router);
app.use(vue3GoogleLogin, {
    clientId: '788845846356-e34ued6ntmj3t4l2417nm5hmvrefsrna.apps.googleusercontent.com'
  })
app.mount('#app');