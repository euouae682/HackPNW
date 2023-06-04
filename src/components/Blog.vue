<script setup>
import BlogHeader from "./blog/BlogHeader.vue";
import BlogPost from './blog/BlogPost.vue';
import { ref } from 'vue';
import { store } from '../store.js';

</script>

<template>
  <BlogHeader />
  <section class="blog-container" v-for="post in store.posts">
      <BlogPost :title="post.title" :article="post.article" :topic="post.title" :date="post.date" :time="post.time" :imgUrl="post.imgUrl"/>
    </section>
</template>

<style scoped></style>
