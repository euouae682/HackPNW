<script setup>
import { store } from "../store.js";
import Navbar from "./Navbar.vue";
</script>

<template>
  <main class="hero" :id="store.showNav">
    <section class="hero-text">
      <h1 class="hero-name">Eco Tribes</h1>
      <p class="hero-description">
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quae ipsam
        saepe eius possimus debitis, eligendi soluta a vitae neque corrupti
        facere ipsa esse quo harum officia molestiae similique, quasi at!
      </p>
    </section>
  </main>

  <div class="wave"></div>
</template>

<style scoped>
/****************/
/* HERO SECTION */
/****************/
.hero {
  display: grid;
  grid-template-columns: 60rem 1fr 30rem;

  background-image: linear-gradient(
      to right,
      rgba(0, 0, 0, 1),
      rgba(0, 0, 0, 0.4)
    ),
    url(../assets/placeholder-hero.jpg);
  background-size: cover;
  height: 100vh;
}

/********/
/* TEXT */
/********/
.hero-text {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;

  position: relative;
  z-index: 1;

  background-color: #32773f;
  gap: 4.8rem;
  padding: 3.2rem;
}
.hero-name {
  color: #78c286;
  font-size: 9.8rem;
  letter-spacing: -0.5px;
}

.hero-description {
  color: #fff;
  font-size: 2.4rem;
  line-height: 1.6;
}

/********/
/* WAVE */
/********/

.wave {
  position: absolute;
  top: 0;
  left: 0;
  width: 46.1%;
  height: 100vh;
  background-image: url(../assets/wave.png);
  background-size: 10rem 100rem;
  /* background-size: cover; */

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
    background-position-y: 100rem;
  }
}

/* .hero-spinner {
  position: absolute;
  top: 0;
  left: 0;
  transform: translate(-40%, 0);
  z-index: 0;
  height: 100%;
  overflow: hidden;

  animation-name: ckw;
  animation-duration: 5s;
  animation-iteration-count: infinite;
  transform-origin: 50% 50%;
  display: inline-block;
}
@keyframes ckw {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
} */

/**************/
/* NAVIGATION */
/**************/

/* .header-nav {
  font-size: 1.8rem;
  padding: 3.2rem 9.6rem;
  background-color: #32773f;

  grid-column: 3 / -1;
}

.header-nav-list {
  display: flex;
  flex-direction: column;
  align-items: flex-start;

  gap: 2.4rem;

  list-style: none;
  cursor: pointer;
}

.header-nav-link:link,
.header-nav-link:visited {
  transition: color 0.5s;
}

.header-nav-link:hover,
.header-nav-link:active {
  color: #aaa;
} */
</style>
