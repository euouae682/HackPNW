<script setup>
import { store } from "../../store.js";
</script>

<template>
  <div class="video-main">
    <div class="video-box">
      <iframe
        class="video"
        src="https://www.youtube.com/embed/ib0GDAPeymo?autoplay=1"
      >
      </iframe>
    </div>

    <h2 class="video-title">Indigenous Women Keep Going Missing in Montana</h2>
    <p class="video-description">
      Montana, a state known for its stunning natural landscapes, has
      unfortunately gained attention for a troubling issue: the alarming rate at
      which indigenous women are going missing. Indigenous women, who are
      already marginalized and vulnerable, face a disproportionately high risk
      of disappearing without a trace in this region. Despite efforts to raise
      awareness and address the issue, the cases of missing indigenous women in
      Montana continue to persist, leaving their families and communities
      devastated. This heartbreaking situation highlights the urgent need for
      increased awareness, improved law enforcement response, and systemic
      changes to ensure the safety and well-being of indigenous women in Montana
      and beyond.
    </p>
  </div>
</template>

<style scoped>
.video {
  width: 100%;
  height: 100%;
  display: block;
}

.video-box {
  background-color: red;
  height: 50rem;
  margin-bottom: 4.8rem;
}

.video-title {
  color: #32773f;
  font-size: 3rem;
  margin-bottom: 2.4rem;
}

.video-description {
  font-size: 1.8rem;
  line-height: 1.3;
}
</style>
