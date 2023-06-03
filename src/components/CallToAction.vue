<script setup></script>

<template>
  <div class="cta">
    <img src="../assets/placeholder-hero.jpg" class="cta-img" />

    <div class="cta-box">
      <h2 class="cta-header">The Planet is Changing</h2>
      <div class="cta-text">
        <p class="cta-goal">
          At EcoTribe, we aim on uniting native communities to protect and
          restore our sacred environment
        </p>
        <p class="cta-description">
          Join the EcoTribe movement today and make a difference for our sacred
          lands. Together, let's map, document, and take action against
          environmental challenges facing Native American communities in the
          United States.
        </p>
      </div>
      <a href="#" class="cta-btn">Try today</a>
    </div>
  </div>
</template>

<style scoped>
.cta {
  display: grid;
  grid-template-columns: 1fr 1fr;
  justify-items: center;
  align-items: start;
  margin: 9.6rem 0;
}

.cta-img {
  width: 80%;
  border-radius: 1.2rem;
}

.cta-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3.2rem;
}

.cta-header {
  font-size: 6.2rem;
  font-weight: 700;
  color: #32773f;
}

.cta-text {
  display: flex;
  flex-direction: column;
  gap: 2.4rem;
  padding: 0 6.4rem;
  margin-bottom: 2.4rem;
}

.cta-goal {
  font-size: 2.4rem;
  color: #78c286;
}

.cta-description {
  font-size: 2.4rem;
}

.cta-btn:any-link {
  font-size: 3rem;
  font-weight: 700;
  text-decoration: none;
  text-transform: uppercase;
  color: #fff;
  background-color: #32773f;
  padding: 1.6rem 3.2rem;
  border-radius: 1.6rem;
  transition: background-color 0.3s;
}

.cta-btn:hover,
.cta-btn:active {
  background-color: #2d6b39;
}
</style>
