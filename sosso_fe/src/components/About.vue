<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" />
  <div class="about">
    <h2>About Us</h2>
    <div class="stylist-info-container" v-for="stylist in stylists" :key="stylist.id">
      <div class="image-container">
        <img src="@/assets/stylist.jpg" alt="Stylist Image" class="img">
      </div>
      <div class="stylist-info">
        <h3>{{ stylist.name }}</h3>
        <p><strong>Email:</strong> {{ stylist.email }}</p>
        <p><strong>Phone:</strong> {{ stylist.phone }}</p>
        <p><strong>Address:</strong> {{ stylist.address }}</p>
      <p>Mon-Sat | 8 am - 7 pm</p>
        Please follow us on TikTok:
        <a href="https://www.tiktok.com/@soniaouedraogo39" target="_blank" rel="noopener noreferrer">
      <i class="fab fa-tiktok"></i>
    </a>
      </div>
    </div>
  </div>
</template>

  

  <script>
import axios from 'axios';
import APIService from '@/http/APIService';


export default {
  name: 'About',
  data() {
    return {
      stylists: [],
    };
  },
  created() {
    // Fetch stylist information from the backend
    this.fetchStylists();
  },
  methods: {
    fetchStylists() {
    // Make API call to fetch stylist information
    APIService.getStylists()
        .then(data => {
        this.stylists = data;
        })
        .catch(error => {
        console.error('Failed to fetch stylist information:', error);
    });
},

  },
};
</script>

<style>

  .about {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }

  .about h2 {
    margin-bottom: 20px;
  }

  .stylist-info-container {
    display: flex;
    align-items: flex-start;
    margin-bottom: 20px;
  }

  .image-container {
    flex-shrink: 0;
    margin-right: 20px;
  }

  .img {
    width: 200px;
    height: auto;
  }

  .stylist-info {
    flex-grow: 1;
  }

  .stylist-info h3 {
    margin-bottom: 10px;
  }

  .stylist-info p {
    margin-bottom: 5px;
  }

</style>
  