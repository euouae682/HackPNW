<script setup>
import { store } from "../store.js";

defineProps({
  title: {
    type: String,
    required: true
  },
  desc: {
    type: String,
    required: true
  },
  bg: {
    type: String,
    required: true
  },
  tcol: {
    type: String,
    required: true
  },
  align: {
    type: String,
    required: true
  },
  imgUrl: {
    type: String,
    required: true
  },
})
</script>

<template>
  <main class="edu-element" :id="store.showNav" :style="'background-color: ' + bg">
    <img v-if="align == 'right'" :src="'src/assets/' + imgUrl" width="900" height="900" />
    <section class="text">
      <h1 class="title" :style="'color: ' + tcol">{{ title }}</h1>
      <p class="description" :style="'color: ' + tcol">{{ desc }}</p>
    </section>
    <img v-if="align == 'left'" :src="'src/assets/' + imgUrl" width="900" height="900" />
  </main>
</template>

<style scoped>
.edu-element {
  display: flex;
  height: 100vh;
  background-color: #32773f;
}

.text {
    width: 50%;
  position: relative;
}
.title {
  color: white;
  font-size: 7rem;
  margin: 12rem 12rem 8rem 12rem;
  letter-spacing: -0.5px;
}

.description {
  color: #ebfbee;
  font-size: 2.5rem;
  margin: 0rem 12rem 0rem 12rem;
  line-height: 1.6;
}

img {
    border-radius: 25px;
    margin: auto;
}
</style>
