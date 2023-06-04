<script setup>
import { store } from "../store.js";
</script>

<template>
  <main class="map" :id="store.showNav">
    <header class="map-header">
      <h1 class="map-title">EcoTribe Map</h1>

      <button class="btn">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          fill="#fff"
          viewBox="0 0 256 256"
          class="btn-icon"
        >
          <path
            d="M224,128a8,8,0,0,1-8,8H136v80a8,8,0,0,1-16,0V136H40a8,8,0,0,1,0-16h80V40a8,8,0,0,1,16,0v80h80A8,8,0,0,1,224,128Z"
          ></path>
        </svg>
        <span>Add a Point</span>
      </button>
    </header>

    <div class="world-map">
      <p>test</p>
    </div>
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

/***************/
/* MAP SECTION */
/***************/

.map {
  margin: 4.8rem;
  height: 100vh;
}

/**********/
/* HEADER */
/**********/

.map-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-right: 12.8rem;
  margin-bottom: 4.8rem;
}
.map-title {
  color: #32773f;
  font-size: 7.4rem;
  font-weight: 700;
}

.btn {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1.2rem;
  padding: 1.2rem 2.4rem;
  border-radius: 2.4rem;

  font-size: 2rem;
  background-color: green;
  color: #fff;
  transition: background-color 0.3s;
  cursor: pointer;
}

.btn:hover,
.btn:active {
  background-color: #2d6b39;
}

/*************/
/* WORLD MAP */
/*************/
.world-map {
  width: 100%;
  height: 70%;
  background-color: red;
}
</style>
