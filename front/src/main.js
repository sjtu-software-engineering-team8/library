import Vue from "vue";
import VueRouter from "vue-router";
import VueResource from "vue-resource";
import elementUI from "Element-UI";
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(elementUI);
Vue.use(VueResource);
Vue.http.options.root = "http://127.0.0.1:8000";
import Vuex from "vuex";
Vue.use(Vuex);
Vue.use(VueRouter);
import router from "./router.js";

import app from "./App.vue";

import { Header, Swipe, SwipeItem } from "mint-ui";

import "mint-ui/lib/style.css";

import "./lib/mui/css/mui.min.css";

Vue.component(Header.name, Header);
Vue.component(Swipe.name, Swipe);
Vue.component(SwipeItem.name, SwipeItem);




var store = new Vuex.Store({
    state: {
        cookie: "",
        No: "",
        flag: true
    },
    mutations: {
        //如果组件想要调用mutations中的方法，只能调用this.$store.commit("方法名",传参)最多两个此参数第一个参数是status状态
    }
});
var vm = new Vue({
    el: "#app",
    render: c => c(app),
    router,
    store
});