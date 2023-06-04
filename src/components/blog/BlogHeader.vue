<script setup>
</script>

<template>
  <div class="blog">
    <h1 class="blog-title">EcoTribe Blog</h1>

    <div class="topics">
      <span class="topics-label">Topics:</span>
      <button class="btn">Native Living</button>
      <button class="btn">Climate Change</button>
      <button class="btn">Adaptation</button>
      <button class="btn">Leadership and Advocacy</button>
    </div>
  </div>
</template>

<style scoped>
/****************/
/* BLOG SECTION */
/****************/
.blog {
  display: flex;
  flex-direction: column;
  gap: 4.8rem;
  margin: 4.8rem;
}

/*********/
/* TITLE */
/*********/
.blog-title {
  color: #32773f;
  font-size: 7.4rem;
  font-weight: 700;
}

/***********/
/* BUTTONS */
/***********/
.topics {
  display: flex;
  align-items: center;
  gap: 3.2rem;
}

.topics-label {
  font-size: 3rem;
  font-weight: 700;
}

.btn {
  display: inline-block;
  padding: 1.2rem 2.4rem;
  border-radius: 2.4rem;

  font-size: 1.6rem;
  background-color: #fff;
  border: 3px solid #212529;
  cursor: pointer;
}
</style>
