<script setup>
import { RouterLink, RouterView } from "vue-router";
import Hero from "./components/Hero.vue";
import About from "./components/About.vue";
import Navbar from "./components/Navbar.vue";
</script>

<template>
  <Hero />
  <About />
  <RouterView />
</template>

<style scoped></style>
