<script setup>
import BlogHeader from "./blog/BlogHeader.vue";
import BlogPost from "./blog/BlogPost.vue";
import { ref } from "vue";
import { store } from "../store.js";

const posts = ref([
  {
    title: "Intertwined with the Land",
    article:
      "Native American communities have long-standing relationships with their ancestral lands, viewing them not merely as resources but as living entities. Climate change disrupts this intricate balance, altering ecosystems, diminishing biodiversity, and threatening cultural practices tied to the land...",
    topic: "Native living",
    date: "May 14th",
    time: "15min",
    imgUrl: "../assets/placeholder-hero.jpg",
  },
]);
</script>

<template>
  <BlogHeader />
  <section class="blog-container" v-for="post in posts">
    <BlogPost
      :title="post.title"
      :article="post.article"
      :topic="post.title"
      :date="post.date"
      :time="post.time"
      :imgUrl="post.imgUrl"
    />
    <BlogPost
      :title="post.title"
      :article="post.article"
      :topic="post.title"
      :date="post.date"
      :time="post.time"
      :imgUrl="post.imgUrl"
    />
    <BlogPost
      :title="post.title"
      :article="post.article"
      :topic="post.title"
      :date="post.date"
      :time="post.time"
      :imgUrl="post.imgUrl"
    />
    <BlogPost
      :title="post.title"
      :article="post.article"
      :topic="post.title"
      :date="post.date"
      :time="post.time"
      :imgUrl="post.imgUrl"
    />
  </section>
</template>

<style scoped>
.blog-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  margin: 4.8rem;
  gap: 3.2rem;
}
</style>
