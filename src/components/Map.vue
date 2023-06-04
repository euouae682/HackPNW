<script setup>
import { store } from '../store.js'
</script>

<template>
  <main class="map" :id=store.showNav>
    <h1 class="map-title">EcoTribe Map</h1>
    <button class="add-point">
      <p>add a point</p>
    </button>
    <aside class="legend">
      <p>test</p>
    </aside>
    <div class="world-map">
      <p>test</p>
    </div>
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

.map {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 4.8rem;
  margin: 4.8rem;
  height: 100vh;
}

.map-title {
  color: #32773f;
  font-size: 7.4rem;
  font-weight: 700;
  width: 70%;
}

.add-point {
  width: 10%;
  background-color: green;
}

.legend {
  width: 20%;
  height: 80%;
  background-color: green;
}

.world-map {
  width: 70%;
}
</style>
