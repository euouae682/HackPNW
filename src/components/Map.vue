<script setup>
import { store } from '../store.js'
</script>

<template>
  <main class="map" :id=store.showNav>
    <h1>Placeholder</h1>
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
</style>
