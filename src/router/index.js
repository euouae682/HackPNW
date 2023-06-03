import { createRouter, createWebHistory } from 'vue-router'
import Hero from '../components/Hero.vue'
import Map from '../components/Map.vue'
import Ping from '../components/Ping.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Hero
    },
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
