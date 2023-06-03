<script setup>
import { store } from '../store.js'
import Navbar from './Navbar.vue'
</script>

<template>
  <main class="hero" :id=store.showNav>
    <section class="hero-text">
      <p class="">Earth Guardian</p>
      <p>
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quae ipsam
        saepe eius possimus debitis, eligendi soluta a vitae neque corrupti
        facere ipsa esse quo harum officia molestiae similique, quasi at!
      </p>
    </section>
  </main>
  <Navbar />
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
