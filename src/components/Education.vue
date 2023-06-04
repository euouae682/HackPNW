<script setup>
import { store } from "../store.js";
import { onMounted, onUnmounted } from "vue";
import EducationHero from "./education/EducationHero.vue";
import EducationThumbnail from "./education/EducationThumbnail.vue";
import EducationMain from "./education/EducationMain.vue";

var fadeInElements = [];

onMounted(() => {
  fadeInElements = Array.from(document.getElementsByClassName("fade-in"));
  document.addEventListener("scroll", handleScroll);
  handleScroll();
});

onUnmounted(() => {
  document.removeEventListener("scroll", handleScroll);
});

const handleScroll = (evt) => {
  for (var i = 0; i < fadeInElements.length; i++) {
    var elem = fadeInElements[i];
    if (isElemVisible(elem)) {
      elem.style.opacity = "1";
      elem.style.transform = "scale(1)";
      fadeInElements.splice(i, 1); // only allow it to run once
    }
  }
};

const isElemVisible = (el) => {
  var rect = el.getBoundingClientRect();
  var elemTop = rect.top + 300; // 200 = buffer
  var elemBottom = rect.bottom;
  return elemTop < window.innerHeight && elemBottom >= 0;
};
</script>

<template>
  <EducationHero />
  <EducationThumbnail />
  <main class="education" :id="store.showNav">
    <aside>
      <EducationThumbnail />
      <EducationThumbnail />
    </aside>
    <article>
      <EducationMain />
    </article>
  </main>
</template>

<style scoped>
#true {
  -webkit-filter: blur(10px);
  filter: blur(10px);
}

#false {
  -webkit-filter: none;
  filter: none;
}

.fade-in {
  opacity: 0;
  transition: 0.5s opacity ease-out;
}

.education {
  background-color: #cbe1cf;
  display: flex;

  transition: filter 0.5s;
  overflow: hidden;
}
</style>
