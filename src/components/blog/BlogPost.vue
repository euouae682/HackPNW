<script setup>
import { store } from "../../store.js";

defineProps({
  title: {
    type: String,
    required: true,
  },
  article: {
    type: String,
    required: true,
  },
  topics: {
    type: String,
    required: true,
  },
  date: {
    type: String,
    required: true,
  },
  time: {
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
  <section class="blog-post" :id="store.showNav">
    <img class="blog-thumbnail" :src="'src/assets/' + imgUrl" />

    <h1 class="blog-title">{{ title }}</h1>
    <p class="blog-article">{{ article }}</p>

    <footer class="blog-footer">
      <span class="blog-footer-topic">Native Living</span>
      <span class="blog-footer-date">May 14, 2023</span>
      <span class="blog-footer-time">15 min</span>
    </footer>
  </section>
</template>

<style scoped>
/****************/
/* BLOG SECTION */
/****************/
.blog-post {
  border: 3px solid black;
  border-radius: 3rem;
  padding: 2rem 2rem 1rem 2rem;
  box-shadow: 0 0 30px 0 rgba(0, 0, 0, 0.07);

  display: flex;
  flex-direction: column;
  gap: 1.6rem;
  cursor: pointer;
  transition: all 0.3s;
}

.blog-post:hover {
  background-color: #32773f;
  color: #fff;
  border: 3px solid #fff;
}
.blog-post:hover > footer {
  border-top: 3px solid #fff;
}
.blog-post:hover > footer span {
  border-right: 3px solid #fff;
}

.blog-post:hover > footer span:last-child {
  border-right: none;
}

/*************/
/* THUMBNAIL */
/*************/
.blog-thumbnail {
  width: 100%;
  border-radius: 3rem;
}

/********/
/* TEXT */
/********/
.blog-title {
  font-size: 2.4rem;
}

.blog-article {
  font-size: 1.6rem;
  line-height: 1.2;
}

/**********/
/* FOOTER */
/**********/
.blog-footer {
  display: flex;
  justify-content: space-around;
  font-size: 1.4rem;
  border-top: 3px solid #000;
  transition: border 0.3s;
}

.blog-footer span {
  padding: 1.2rem 0;
  border-right: 3px solid #000;
  flex: 1 0 0;
  text-align: center;
  transition: border 0.3s;
}

.blog-footer span:last-child {
  border-right: none;
}
</style>
