<script setup></script>

<template>
  <section class="about fade-in">
    <div class="about-box">
      <div class="about-heading">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="about-icon"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9 5.25h.008v.008H12v-.008z"
          />
        </svg>

        <h2 class="about-header">What is EcoTribe?</h2>
      </div>

      <p class="about-text">
        With EcoTribe, community members can map and document environmental
        concerns plaguing their areas. With a user-friendly user interface it
        enables users to mark locations of pollution, habitat degradation, or
        any other environmental challenges they come across. By including photos
        and detailed descriptions, EcoTribe empowers communities to raise
        awareness about these issues effectively.
      </p>
    </div>
    <img src="../../assets/home/about-what.png" alt="" class="about-img" />

    <img src="../../assets/home/about-how.png" alt="" class="about-img" />
    <div class="about-box">
      <div class="about-heading">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="about-icon"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 013 19.875v-6.75zM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V8.625zM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V4.125z"
          />
        </svg>

        <h2 class="about-header">How does it work?</h2>
      </div>
      <p class="about-text">
        Not only does it serve as a platform for sharing concerns, but it also
        acts as a data collection hub, fostering a deeper understanding of the
        environmental landscape. With this comprehensive tool in their hands,
        communities gain the ability to take meaningful action and drive
        positive change for their sacred lands. Together, as EcoTribe, they can
        safeguard their natural heritage and pave the way for a sustainable
        future.
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
  margin: 9.6rem 0;
}

.about-box {
  display: flex;
  flex-direction: column;
  gap: 2.4rem;
  padding: 0 10%;
}

.about-heading {
  display: flex;
  align-items: center;
  gap: 1.2rem;
}

.about-icon {
  height: 4.8rem;
  stroke: #32773f;
}

.about-header {
  font-size: 3.6rem;
  font-weight: 700;
  color: #32773f;
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
