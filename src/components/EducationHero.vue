<script setup>
import { store } from "../store.js";
import Navbar from "./Navbar.vue";
</script>

<template>
  <main class="hero" :id="store.showNav">
    <section class="hero-text">
    <div class="hero-name">
        <h1>Read.</h1>
        <h1>Learn.</h1>
        <h1>Educate.</h1>
    </div>
      <p class="hero-description">
        While staying informed is the future, it's always important to reflect on the past.
      </p>
    </section>
    <section class="flex-container">
        <div class="flex-item traditions" v-scroll-to="'#traditions'" @mouseover="store.toggleTrad" :id="store.tradExpand">
            <p>Native American Traditions</p>
        </div>
        <div class="flex-item women" v-scroll-to="'#women'" @mouseover="store.toggleWomen" :id="store.womenExpand">
            <p>Native Women</p>
        </div>
        <div class="flex-item warming" v-scroll-to="'#warming'" @mouseover="store.toggleWarming" :id="store.warmingExpand">
            <p>Global Warming</p>
        </div>
    </section>
  </main>
</template>

<style scoped>
/****************/
/* HERO SECTION */
/****************/
.hero {
  display: grid;
  grid-template-columns: 60rem 1fr 30rem;
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

  background-color: white;
  gap: 4.8rem;
  margin: 7.2rem 1.8rem 7.2rem 6.0rem;
}
.hero-name {
  color: black;
  font-size: 8.0rem;
  letter-spacing: -0.5px;
  line-height: 12rem;
  font-weight: 300;
}

.hero-description {
  color: #32773f;
  font-size: 3.2rem;
  line-height: 1.6;
  text-align: center;
  font-weight: 500;
}

.flex-container {
    display: flex;
    position: absolute;
    width: 60%;
    height: 80%;
    bottom: 8%;
    right: 5%;
}

.flex-item {
    position: relative;
    border-radius: 15px;
    background-color: black;
    margin: 15px;
    width: 30%;
    font-size: 3rem;
    color: white;
    transition: width 0.2s;
    cursor: pointer;
}

.flex-item p {
    position: absolute;
    bottom: 15%;
    margin: 25px;
    font-size: 40px;
    font-weight: bold;
}

#true {
    width: 50%;
}

#false > p {
    background-color: green;
    height: 35%;
    overflow-y: visible;
    padding: 16px;
    writing-mode: vertical-lr;
    text-orientation: sideways;
    transition: all 0.5s;
    line-height: 86%;
    letter-spacing: 8px;
    overflow: none;
}

.traditions {
    background: url(../assets/traditions.png);
    background-position: center;
    background-size: cover;
}

.women {
    background: url(../assets/nawomen.png);
    background-position: center;
    background-size: cover;
}

.warming {
    background: url(../assets/globalwarming.png);
    background-position: center;
    background-size: cover;
}
</style>
