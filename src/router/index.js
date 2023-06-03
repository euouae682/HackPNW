import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Education from '../components/Education.vue'
import Map from '../components/Map.vue'
import Ping from '../components/Ping.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/education',
      name: 'education',
      component: Education
    },
    // {
    //   path: '/blog',
    //   name: 'blog',
    //   component: Blog
    // },
    {
      path: '/map',
      name: 'map',
      component: Map
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
  ]
})

export default router
