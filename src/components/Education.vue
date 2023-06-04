<script setup>
import { store } from '../store.js';
import { onMounted, onUnmounted } from 'vue';
import EducationHero from './EducationHero.vue';
import EduElement from './EduElement.vue';

var fadeInElements = []

onMounted(() => {
    fadeInElements = Array.from(document.getElementsByClassName('fade-in'))
    document.addEventListener('scroll', handleScroll)
    handleScroll()
})

onUnmounted(() => {
    document.removeEventListener('scroll', handleScroll)
})

const handleScroll = (evt) => {
      for (var i = 0; i < fadeInElements.length; i++) {
        var elem = fadeInElements[i]
        if (isElemVisible(elem)) {
          elem.style.opacity = '1'
          elem.style.transform = 'scale(1)'
          fadeInElements.splice(i, 1) // only allow it to run once
        }
      }
}

const isElemVisible = (el) => {
      var rect = el.getBoundingClientRect()
      var elemTop = rect.top + 300 // 200 = buffer
      var elemBottom = rect.bottom
      return elemTop < window.innerHeight && elemBottom >= 0
}
</script>

<template>
  <main class="education" :id="store.showNav">
    <EducationHero />
    <EduElement id="traditions" title="Native American Traditions" desc="Native American traditions encompass a rich tapestry of cultural practices that have been passed down through generations. Rooted in deep reverence for the land, these traditions emphasize a harmonious relationship between humans and nature. 

    Native American communities have an intricate understanding of their surroundings, recognizing the interconnectedness of all living beings. Traditional ceremonies, such as powwows, sweat lodges, and vision quests, play a vital role in spiritual expression and community bonding. The oral tradition, storytelling, remains a fundamental aspect, preserving ancestral knowledge, history, and cultural values. Native American arts and crafts, such as intricate beadwork, pottery, and intricate carvings, not only showcase remarkable craftsmanship but also reflect profound connections to nature and ancestral heritage.

    Respect for elders, communal decision-making, and a profound sense of interconnectedness shape the social fabric of these communities. Native American traditions are a testament to the enduring spirit and resilience of Indigenous cultures, serving as a wellspring of wisdom and inspiration for all who seek to understand and honor their heritage.
" bg="#32773f" tcol="white" align=right imgUrl="traditions.png" />
<EduElement id="women" title="Native American Women" desc="Native American women and elders hold significant roles within their communities, serving as pillars of strength, wisdom, and cultural preservation. Native American women have been essential in upholding and passing down traditions, maintaining the social fabric, and nurturing the next generation. They are revered for their resilience, leadership, and deep connection to the land. 

Native American elders, both men and women, are revered for their wisdom and life experiences. They are the custodians of ancestral knowledge, embodying the traditions, stories, and teachings that have been passed down through generations. Elders play a crucial role in decision-making, guiding community members, and providing guidance on spiritual and cultural matters. 

Their presence is cherished, and their wisdom is sought after to ensure the continuity and preservation of Indigenous traditions. Native American women and elders are the bearers of cultural heritage, embodying the strength, resilience, and wisdom that enriches their communities and inspires future generations.
" bg="white" tcol="#32773f" align=left imgUrl="nawomen.png" />
<EduElement id="warming" title="Global Warming" desc="Global warming presents a multitude of complex challenges that have far-reaching impacts on Native American communities across the globe. These communities, deeply rooted in their ancestral lands, face unique vulnerabilities and are disproportionately affected by the consequences of climate change. Rising temperatures, changing precipitation patterns, and increased frequency of extreme weather events are just some of the consequences that Native American communities experience firsthand.

In addition to the direct impacts on livelihoods, global warming also affects the delicate balance between nature and spirituality within Native American communities. These communities have deep spiritual connections to the land, water bodies, and natural resources. Changes in ecosystems, such as the loss of sacred sites or the diminishing availability of medicinal plants, have profound implications for their cultural and spiritual practices. The loss of biodiversity and the degradation of ecosystems undermine the traditional knowledge passed down through generations and jeopardize the integrity of their cultural heritage.

Furthermore, the impacts of global warming exacerbate pre-existing socio-economic disparities faced by Native American communities. Many of these communities are located in rural and remote areas with limited access to resources and infrastructure.
" bg="#32773f" tcol="white" align=right imgUrl="globalwarming.png" />
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
  transition: filter 0.5s;
  overflow: hidden;
}
</style>
