<script setup>
import { store } from "../../store.js";

defineProps({
  title: {
    type: String,
    required: true,
  },
  desc: {
    type: String,
    required: true,
  },
  bg: {
    type: String,
    required: true,
  },
  hcol: {
    type: String,
    required: true,
  },

  tcol: {
    type: String,
    required: true,
  },
  align: {
    type: String,
    required: true,
  },
  imgUrl: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <main
    class="edu-element"
    :id="store.showNav"
    :style="'background-color: ' + bg"
  >
    <img v-if="align == 'right'" :src="'src/assets/' + imgUrl" />

    <section class="text">
      <h1 class="title" :style="'color: ' + hcol">{{ title }}</h1>
      <p class="description" :style="'color: ' + tcol">{{ desc }}</p>
    </section>

    <img v-if="align == 'left'" :src="'src/assets/' + imgUrl" />
  </main>
</template>

<style scoped>
/*************/
/* CONTAINER */
/*************/
.edu-element {
  display: flex;
  background-color: #32773f;
  height: 100vh;
  padding: 4.8rem 3.2rem;
}

/********/
/* TEXT */
/********/
.text {
  display: flex;
  flex-direction: column;
  gap: 3.2rem;
  margin: 0 6.4rem;
}
.title {
  font-size: 5.2rem;
  letter-spacing: -0.3px;
}

.description {
  font-size: 1.8rem;
  line-height: 1.3;
}

/*********/
/* IMAGE */
/*********/
img {
  border-radius: 25px;
  width: 70rem;
}
</style>
