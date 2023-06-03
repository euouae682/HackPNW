<script setup></script>

<template>
  <main class="hero">
    <section class="hero-text">
      <p class="">Earth Guardian</p>
      <p>
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quae ipsam
        saepe eius possimus debitis, eligendi soluta a vitae neque corrupti
        facere ipsa esse quo harum officia molestiae similique, quasi at!
      </p>
    </section>

    <nav class="header-nav">
      <ul class="header-nav-list">
        <li><a class="header-nav-link">Section 1</a></li>
        <li><a class="header-nav-link">Section 2</a></li>
        <li><a class="header-nav-link">Section 3</a></li>
        <li><a class="header-nav-link">Section 4</a></li>
        <li><a class="header-nav-link">Section 5</a></li>
      </ul>
    </nav>
  </main>
</template>

<style scoped>
/****************/
/* HERO SECTION */
/****************/
.hero {
  display: grid;
  justify-content: space-between;

  background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)),
    url(../assets/placeholder-hero.jpg);
  background-size: cover;
  height: 100vh;
}

/**************/
/* NAVIGATION */
/**************/

.header-nav {
  font-size: 1.8rem;
  padding: 3.2rem 9.6rem;
  background-color: #32773f;
}

.header-nav-list {
  display: flex;
  flex-direction: column;
  align-items: flex-start;

  gap: 2.4rem;

  list-style: none;
  cursor: pointer;
}

.header-nav-link:link,
.header-nav-link:visited {
  transition: color 0.5s;
}

.header-nav-link:hover,
.header-nav-link:active {
  color: #aaa;
}
</style>
