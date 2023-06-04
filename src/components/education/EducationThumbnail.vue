<script setup>
import { store } from "../../store.js";

defineProps({
  title: {
    type: String,
    required: true,
  },
  description: {
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
  <section class="tn" :id="store.showNav">
    <img class="tn-img" :src="'src/assets/' + imgUrl" />

    <div class="tn-text">
      <h1 class="tn-title">{{ title }}</h1>
      <p class="tn-article">{{ description }}</p>
    </div>

    <!-- <img class="tn-img" src="../../assets/placeholder-hero.jpg" />

    <div class="tn-text">
      <h1 class="tn-title">TITLE</h1>
      <p class="tn-article">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse quis
        expedita nostrum corporis sunt at, nam adipisci tempore in voluptates
        nisi iusto incidunt?
      </p>
    </div> -->
  </section>
</template>

<style scoped>
/*************/
/* THUMBNAIL */
/*************/
.tn {
  background-color: #fff;
  display: flex;
  gap: 0.8rem;
  padding: 1rem;
  margin-bottom: 1.2rem;
  border-radius: 2rem;
  cursor: pointer;
  transition: all 0.3s;
}

.tn:hover {
  background-color: #32773f;
  color: #fff;
}

/*********/
/* IMAGE */
/*********/
.tn-img {
  width: 20rem;
  border-radius: 2rem;
}

.tn-text {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  margin: 1.2rem;
}

.tn-title {
  font-size: 2.4rem;
  font-weight: 700;
}

.tn-article {
  font-size: 1.4rem;
}
</style>
