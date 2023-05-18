<template>
    <div class="gallery">
      <div class="gallery-item" v-for="(image, index) in images" :key="index">
        <img :src="require(`@/assets/${image}`)" alt="Gallery Image">
      </div>
    </div>
</template>
  

  <script>
  export default {
    data() {
      return {
        images: ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg', 'image6.jpg', 'image7.jpg', 'image8.jpg', 'image9.jpg', 'image10.jpg', 'image11.jpg', 'image12.jpg']
      };
    }
  };
  </script>
  
<style scoped>
    .gallery {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
    }

    .gallery-item img {
    width: 100%;
    height: auto;
    }
</style>
