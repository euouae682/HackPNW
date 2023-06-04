<script setup>
import { store } from "../../store.js";

defineProps({
  title: {
    type: String,
    required: true
  },
  article: {
    type: String,
    required: true
  },
  topics: {
    type: String,
    required: true
  },
  date: {
    type: String,
    required: true
  },
  time: {
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
    <section class="post" :id="store.showNav">
        hi hi hi hi
        <img class="thumbnail" :src="'src/assets/' + imgUrl" width="700" height="700" />
        <h1 class="title">{{ title }}</h1>
        <p class="article">{{ article }}</p>
        <footer class="footer"></footer>
    </section>
</template>

<style scoped>
.post {
  border: 3px solid black;
  border-radius: 5rem;
  width: 30%;
  height: 50%;
  display: flex;
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
  white-space: pre-line;
}

img {
    border-radius: 25px;
    margin: auto;
}
</style>
