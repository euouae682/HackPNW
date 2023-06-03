<script setup>
import { RouterLink, RouterView } from "vue-router";
import Hero from "./components/Hero.vue";
import About from "./components/About.vue";
import Motto from "./components/Motto.vue";
import CallToAction from "./components/CallToAction.vue";
import Navbar from "./components/Navbar.vue";
</script>

<template>
  <Hero />
  <About />
  <Motto />
  <CallToAction />
  <RouterView />
  <Navbar />
</template>

<style scoped></style>
