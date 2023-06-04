<script setup>
defineProps({
  title: {
    type: String,
    required: true,
  },
  article: {
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
    <!-- <img class="tn-img" :src="'src/assets/' + imgUrl" />

    <div class="tn-text">
      <h1 class="tn-title">{{ title }}</h1>
      <p class="tn-article">{{ article }}</p>
    </div> -->

    <img class="tn-img" src="../../assets/placeholder-hero.jpg" />

    <div class="tn-text">
      <h1 class="tn-title">TITLE</h1>
      <p class="tn-article">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse quis
        expedita nostrum corporis sunt at, nam adipisci tempore in voluptates
        nisi iusto incidunt assumenda fugiat consectetur dolorem! Illo, soluta
        quo?
      </p>
    </div>
  </section>
</template>

<style scoped></style>
