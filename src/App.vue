<script setup>
import { RouterLink, RouterView } from "vue-router";
import Navbar from "./components/Navbar.vue";
</script>

<template>
  <Hero />
  <RouterView />
  <Navbar />
</template>

<style scoped></style>
