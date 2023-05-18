<template>
    <div class="home-container">
      <h1>Welcome</h1>
      <h3>Thank you for choosing Sosso Hair Braiding for your hair needs</h3>
      <h4>Omaha Hair Salon</h4>
      <p>We believe that the right hairstyle will light a woman's or man's face, giving him or her more confidence and assurance in front of people. This is why we put great effort into meeting our customer's needs, whatever their background and origin. We do hair for all communities. Just tell us what you want to do. 
</p>
      <router-link to="/hairstyles" class="btn-link">View Available Hairstyles</router-link>
      <div>
      <router-link to="/schedule" class="btn-link">Schedule an Appointment</router-link>
    </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Home',
  };
  </script>
  
  <style>
  .home-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
  }
  
  h1 {
    font-size: 2.5rem;
    margin-bottom: 20px;
  }
  
  p {
    font-size: 1.2rem;
    margin-bottom: 30px;
  }
  
  .btn {
    display: inline-block;
    padding: 10px 20px;
    background-color: #337ab7;
    color: #fff;
    text-decoration: none;
    font-size: 1rem;
    border-radius: 5px;
  }
  
  .btn:hover {
    background-color: #23527c;
  }
  </style>
  