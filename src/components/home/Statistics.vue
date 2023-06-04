<script setup></script>

<template>
  <div class="stats fade-in">
    <h2 class="stats-header">What's happening to indigenous land?</h2>

    <div class="stats-box">
      <div class="stats-info">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="#fff"
          viewBox="0 0 256 256"
          class="stats-icon"
        >
          <path
            d="M223.77,150.09a8,8,0,0,1-5.86,9.68l-24.64,6,6.46,24.11a8,8,0,0,1-5.66,9.8A8.25,8.25,0,0,1,192,200a8,8,0,0,1-7.72-5.93l-7.72-28.8L136,141.86v46.83l21.66,21.65a8,8,0,0,1-11.32,11.32L128,203.31l-18.34,18.35a8,8,0,0,1-11.32-11.32L120,188.69V141.86L79.45,165.27l-7.72,28.8A8,8,0,0,1,64,200a8.25,8.25,0,0,1-2.08-.27,8,8,0,0,1-5.66-9.8l6.46-24.11-24.64-6a8,8,0,0,1,3.82-15.54l29.45,7.23L112,128,71.36,104.54l-29.45,7.23A7.85,7.85,0,0,1,40,112a8,8,0,0,1-1.91-15.77l24.64-6L56.27,66.07a8,8,0,0,1,15.46-4.14l7.72,28.8L120,114.14V67.31L98.34,45.66a8,8,0,0,1,11.32-11.32L128,52.69l18.34-18.35a8,8,0,0,1,11.32,11.32L136,67.31v46.83l40.55-23.41,7.72-28.8a8,8,0,0,1,15.46,4.14l-6.46,24.11,24.64,6A8,8,0,0,1,216,112a7.85,7.85,0,0,1-1.91-.23l-29.45-7.23L144,128l40.64,23.46,29.45-7.23A8,8,0,0,1,223.77,150.09Z"
          ></path>
        </svg>
        <p>
          Arctic sea ice extent has declined at a rate of 13.2% per decade since
          the late 1970s.
        </p>
      </div>

      <div class="stats-info">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="#fff"
          viewBox="0 0 256 256"
          class="stats-icon"
        >
          <path
            d="M173.79,51.48a221.25,221.25,0,0,0-41.67-34.34,8,8,0,0,0-8.24,0A221.25,221.25,0,0,0,82.21,51.48C54.59,80.48,40,112.47,40,144a88,88,0,0,0,176,0C216,112.47,201.41,80.48,173.79,51.48ZM96,184c0-27.67,22.53-47.28,32-54.3,9.48,7,32,26.63,32,54.3a32,32,0,0,1-64,0Zm77.27,15.93A47.8,47.8,0,0,0,176,184c0-44-42.09-69.79-43.88-70.86a8,8,0,0,0-8.24,0C122.09,114.21,80,140,80,184a47.8,47.8,0,0,0,2.73,15.93A71.88,71.88,0,0,1,56,144c0-34.41,20.4-63.15,37.52-81.19A216.21,216.21,0,0,1,128,33.54a215.77,215.77,0,0,1,34.48,29.27C193.49,95.5,200,125,200,144A71.88,71.88,0,0,1,173.27,199.93Z"
          ></path>
        </svg>
        <p>
          Climate change contributes to more frequent and intense wildfires,
          which pose risks to Native American lands, homes, and ecosystems.
        </p>
      </div>

      <div class="stats-info">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="#fff"
          viewBox="0 0 256 256"
          class="stats-icon"
        >
          <path
            d="M174,47.75a254.19,254.19,0,0,0-41.45-38.3,8,8,0,0,0-9.18,0A254.19,254.19,0,0,0,82,47.75C54.51,79.32,40,112.6,40,144a88,88,0,0,0,176,0C216,112.6,201.49,79.32,174,47.75ZM128,216a72.08,72.08,0,0,1-72-72c0-57.23,55.47-105,72-118,16.53,13,72,60.75,72,118A72.08,72.08,0,0,1,128,216Zm55.89-62.66a57.6,57.6,0,0,1-46.56,46.55A8.75,8.75,0,0,1,136,200a8,8,0,0,1-1.32-15.89c16.57-2.79,30.63-16.85,33.44-33.45a8,8,0,0,1,15.78,2.68Z"
          ></path>
        </svg>
        <p>
          Reduced water availability due to drought, changes in rainfall
          patterns, and glacial melt can impact the availability and quality of
          water resources.
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
/**********************/
/* STATISTICS SECTION */
/**********************/
.stats {
  padding: 9.6rem;
  background-color: #32773f;
}

/***********/
/* HEADING */
/***********/
.stats-header {
  color: #fff;
  font-size: 3.6rem;
  margin-bottom: 6.4rem;
}

/**************/
/* STATISTICS */
/**************/
.stats-box {
  display: flex;
  gap: 4.8rem;
}

.stats-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1 1 0px;
  gap: 2.4rem;
}

.stats-info p {
  color: #fff;
  font-size: 2rem;
}

.stats-icon {
  width: 6.4rem;
}
</style>
