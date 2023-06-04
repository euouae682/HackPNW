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
    <img v-if="align == 'right'" :src="'src/assets/' + imgUrl" width="700" height="700" />
    <section class="text">
      <h1 class="title" :style="'color: ' + tcol">{{ title }}</h1>
      <p class="description" :style="'color: ' + tcol">{{ desc }}</p>
    </section>
    <img v-if="align == 'left'" :src="'src/assets/' + imgUrl" width="700" height="700" />
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
  font-size: 5rem;
  margin: 6rem 6rem 3rem 6rem;
  letter-spacing: -0.5px;
}

.description {
  color: #ebfbee;
  font-size: 2rem;
  margin: 0rem 6rem 0rem 6rem;
  line-height: 1.6;
}

img {
    border-radius: 25px;
    margin: auto;
}
</style>
