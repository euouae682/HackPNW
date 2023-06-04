<script setup>
import { store } from "../store.js";
import Navbar from "./Navbar.vue";
</script>

<template>
  <main class="hero" :id="store.showNav">
    <div class="wave">
      <section class="hero-text">
        <h1 class="hero-name">EcoTribes</h1>
        <p class="hero-description">
          A powerful web application designed specifically to empower Native
          American communities in the United States.
        </p>
      </section>
    </div>
  </main>
</template>

<style scoped>
/****************/
/* HERO SECTION */
/****************/
.hero {
  background-image: url(../assets/home/hero.png);
  background-size: cover;
  height: 100vh;
}

/********/
/* TEXT */
/********/
.hero-text {
  display: flex;
  justify-content: center;
  flex-direction: column;

  position: relative;
  z-index: 1;

  /* background-color: #32773f; */
  width: 65rem;
  height: 100%;
  gap: 4.8rem;
}
.hero-name {
  color: #78c286;
  font-size: 9.8rem;
  letter-spacing: -0.5px;
  padding-left: 6.4rem;
}

.hero-description {
  color: #ebfbee;
  font-size: 3rem;
  line-height: 1.6;
  padding-left: 6.4rem;
}

/********/
/* WAVE */
/********/

.wave {
  height: 100vh;
  background-image: url(../assets/home/wave.png);
  background-size: contain;
  /* background-repeat: no-repeat; */

  animation: animate 3s linear infinite reverse;
  z-index: 0;
  opacity: 1;
  animation-delay: 0s;
}
@keyframes animate {
  0% {
    background-position-y: 0;
  }
  100% {
    background-position-y: 100vh;
  }
}
</style>
