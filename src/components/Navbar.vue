<script setup>
import { store } from "../store.js";
</script>

<template>
  <div class="open-nav">
    <i @click="store.toggleNav" class="material-icons" style="font-size: 48px"
      >menu</i>
  </div>
  <div :id="store.showNav" class="sidenav">
    <a href="javascript:void(0)" class="closebtn" @click="store.toggleNav"
      >&times;</a
    >
    <router-link to="/">Home</router-link>
    <router-link to="/education">Education</router-link>
    <router-link to="/blog">Blog</router-link>
    <router-link to="/map">Map</router-link>
  </div>
</template>

<style scoped>
/****************/
/* HERO SECTION */
/****************/
/* The side navigation menu */
#true {
  width: 40rem;
}

#false {
  width: 0px;
}

.open-nav,
.sidenav {
  position: fixed;
  z-index: 1;
  top: 0;
  right: 0;
}

.open-nav {
  margin-right: 30px;
  padding-top: 30px;
  color: #32773f;
  cursor: pointer;
}

i {
  background-color: white;
  padding: 3px;
  border-radius: 15px;
}

.sidenav {
  height: 100%;
  width: 0;
  position: fixed;
  z-index: 1;
  top: 0;
  right: 0;
  background-color: #32773f;
  overflow-x: hidden;
  padding-top: 60px;
  transition: 0.5s;
  text-align: center;
}

/* The navigation menu links */
.sidenav a {
  padding: 8px 8px 8px 32px;
  text-decoration: none;
  font-size: 4rem;
  color: #fff;
  display: block;
  transition: 0.3s;
  padding: 4rem;
}

/* When you mouse over the navigation links, change their color */
.sidenav a:hover {
  color: #cecece;
}

/* Position and style the close button (top right corner) */
.sidenav .closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 50px;
}

/* Style page content - use this if you want to push the page content to the right when you open the side navigation */
#main {
  transition: margin-left 0.5s;
  padding: 20px;
}

/* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */
@media screen and (max-height: 450px) {
  .sidenav {
    padding-top: 15px;
  }
  .sidenav a {
    font-size: 18px;
  }
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
