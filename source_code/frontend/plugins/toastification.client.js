import Vue from "vue";
import Toast from "vue-toastification"
import "vue-toastification/dist/index.css"
 
const options = {
    timeout: 5000,
    draggable: false  
};
 
 
Vue.use(Toast, options);