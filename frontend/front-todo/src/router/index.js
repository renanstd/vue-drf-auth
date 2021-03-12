import Vue from 'vue';
import VueRouter from 'vue-router';
import Login from '../components/Login.vue';
import Todos from '../components/Todos.vue';


Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Todos',
    component: Todos,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const auth = Vue.$cookies.get("auth")
    if (auth == null || !auth.is_auth) {
      next({ name: 'Login' })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router;
