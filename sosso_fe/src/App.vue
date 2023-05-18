<template>
  <div id="app">
    <header>
      <img src="@/assets/logo.png" alt="Logo" class="logo" />
      <nav>
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/hairstyles">Hairstyles</router-link></li>
          <li><router-link to="/about">About</router-link></li>
          <li><router-link to="/gallery">Gallery</router-link></li>
        </ul>
      </nav>
    </header>
    <router-view />
  </div>
</template>


<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  max-width: 960px;
  margin: 0 auto;
  padding: 20px;
}

header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px;
}

.logo {
  width: 100px;
  height: auto;
}

nav ul {
  list-style: none;
  display: flex;
}

nav ul li {
  margin-right: 10px;
}

nav ul li a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
}
</style>

