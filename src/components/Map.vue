<script setup>
import { store } from '../store.js'
</script>

<template>
  <main class="hero" :id=store.showNav>
    <section class="hero-text">
      <p class="">Earth Guardian</p>
      <p>
        idk theres some stuff here lol
      </p>
    </section>
  </main>
</template>

<style scoped>
/****************/
/* HERO SECTION */
/****************/
#true {
  -webkit-filter: blur(10px); /* Safari 6.0 - 9.0 */
  filter: blur(10px);
}

#false {
  -webkit-filter: none;
  filter: none;
}

.hero {
  display: grid;
  justify-content: space-between;

  background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)),
    url(../assets/placeholder-hero.jpg);
  background-size: cover;
  height: 100vh;
  transition: filter 0.5s;
}
</style>
