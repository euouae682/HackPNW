<script setup>
import BlogHeader from "./blog/BlogHeader.vue";
import BlogPost from "./blog/BlogPost.vue";
import { ref } from "vue";
import { store } from "../store.js";

store.filterPosts('');
</script>

<template>
  <BlogHeader />
  <section class="blog-container">
    <BlogPost v-for="post in store.filteredPosts" @click="store.toggleDetail(post)"
      :title="post.title"
      :article="post.article"
      :topic="post.topic"
      :date="post.date"
      :time="post.time"
      :inset="post.inset"
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
