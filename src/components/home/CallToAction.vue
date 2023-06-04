<script setup></script>

<template>
  <div class="cta fade-in">
    <img src="../../assets/home/cta.png" class="cta-img" />

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
      <a href="map" class="cta-btn">Try today</a>
    </div>
  </div>
</template>

<style scoped>
/**************************/
/* CALL-TO-ACTION SECTION */
/**************************/
.cta {
  display: flex;
  justify-items: center;
  align-items: center;
  margin: 9.6rem;
}

/**********/
/* IMAGE */
/**********/
.cta-img {
  height: 60rem;
  border-radius: 1.2rem;
}

/********/
/* TEXT */
/********/
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

  font-size: 2.4rem;
  text-align: center;
}

.cta-goal {
  color: #78c286;
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
