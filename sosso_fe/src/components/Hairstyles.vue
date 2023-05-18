<template>
    <div class="hairstyles-container">
      <h1>Available Hairstyles</h1>
      <ul class="hairstyle-list">
        <li v-for="hairstyle in hairstyles" :key="hairstyle.id" class="hairstyle-item">
            <h2 class="hairstyle-name">{{ hairstyle.name }}</h2>
            <img :src="hairstyle.image" alt="Hairstyle" class="hairstyles-img">
          <p class="hairstyle-description">{{ hairstyle.description }}</p>
          <p class="hairstyle-price">Price: ${{ hairstyle.price }}</p>
          <router-link to="/schedule" class="button-rectangular">Schedule an Appointment</router-link>
        </li>
      </ul>
    </div>
  </template>
  

  <script>
import APIService from '@/http/APIService';

export default {
  name: 'Hairstyles',
  data() {
    return {
      hairstyles: [],
    };
  },
  created() {
    this.fetchHairstyles();
  },
  methods: {
    fetchHairstyles() {
      APIService.getHairstyles()
        .then(data => {
          this.hairstyles = data;
        })
        .catch(error => {
          console.error('Failed to fetch hairstyles:', error);
        });
    },
  },
};
</script>
  
  <style>
.hairstyles-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.hairstyles-img {
  max-width: 500px;
  height: 350px;
}

.hairstyle-list {
  list-style-type: none;
  padding: 0;
}

.hairstyle-item {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  margin-bottom: 20px;
}

.hairstyle-name {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.hairstyle-description {
  margin-bottom: 10px;
}

.hairstyle-price {
  font-weight: bold;
}

.button-rectangular {
  display: inline-block;
  padding: 5px 10px;
  border: 1px solid #000;
  border-radius: 5px;
  text-decoration: none;
  color: #000;
}

</style>
  