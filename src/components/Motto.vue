<script setup></script>

<template>
  <div class="motto">
    <h3 class="motto-text">Empowering native voices.</h3>
    <h3 class="motto-text">Preserving sacred lands.</h3>
  </div>
</template>

<style scoped>
.motto {
  min-height: 100vh;
  background-image: url(../assets/home/motto.png);
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;

  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 3.2rem;
  padding-left: 6.4rem;
}

.motto-text {
  color: #fff;
  font-size: 6.2rem;
}
</style>
