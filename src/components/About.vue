<script setup></script>

<template>
  <section class="about">
    <div class="about-box">
      <h2 class="about-header">What is EcoTribe?</h2>
      <p class="about-text">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid,
        officiis ipsum perspiciatis repudiandae illo eveniet voluptatem non. Qui
        enim aliquam deserunt nobis minus cumque. Vero a nobis nesciunt
        temporibus sit.
      </p>
    </div>
    <img src="../assets/placeholder-hero.jpg" alt="" class="about-img" />

    <img src="../assets/placeholder-hero.jpg" alt="" class="about-img" />
    <div class="about-box">
      <h2 class="about-header">How does it work?</h2>
      <p class="about-text">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid,
        officiis ipsum perspiciatis repudiandae illo eveniet voluptatem non. Qui
        enim aliquam deserunt nobis minus cumque. Vero a nobis nesciunt
        temporibus sit.
      </p>
    </div>
  </section>
</template>

<style scoped>
/*****************/
/* ABOUT SECTION */
/*****************/
.about {
  display: grid;
  grid-template-columns: 1fr 1fr;
  justify-items: center;
  align-items: center;
  row-gap: 4.8rem;
  margin-bottom: 9.6rem;
}

.about-box {
  display: flex;
  flex-direction: column;
  gap: 2.4rem;
  padding: 0 10%;
}

.about-header {
  font-size: 3.6rem;
  font-weight: 700;
}

.about-text {
  font-size: 1.8rem;
  line-height: 1.6;
}

.about-img {
  width: 80%;
  border-radius: 1.2rem;
}
</style>
