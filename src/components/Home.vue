<script setup>
import Hero from "./Hero.vue";
import About from "./About.vue";
import Navbar from "./Navbar.vue";
import Motto from "./Motto.vue";
import CallToAction from "./CallToAction.vue";
import { store } from "../store.js";
</script>

<template>
  <main class="home" :id="store.showNav">
    <Hero />
    <About />
    <Motto />
    <CallToAction />
  </main>
</template>

<style scoped>
#true {
  -webkit-filter: blur(10px);
  filter: blur(10px);
}

#false {
  -webkit-filter: none;
  filter: none;
}

.home {
  transition: filter 0.5s;
  overflow: hidden;
}
</style>
