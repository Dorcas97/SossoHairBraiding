<template>
    <div class="appointment-details">
      <h2>Appointment Details</h2>
      <div class="details">
        <div><strong>Date:</strong> {{ appointment.date }}</div>
        <div><strong>Time:</strong> {{ appointment.appointment_time }}</div>
        <div><strong>Stylist:</strong> {{ appointment.stylist.name }}</div>
        <div><strong>Client:</strong> {{ appointment.client.name }}</div>
        <div><strong>Hairstyle:</strong> {{ appointment.hairstyle.name }}</div>
      </div>
      <div class="actions">
        <button @click="rescheduleAppointment">Reschedule</button>
        <button @click="cancelAppointment">Cancel</button>
      </div>
    </div>
  </template>
  

  <script>
  import APIService from '@/http/APIService';

  export default {
    name: 'AppointmentDetails',
    props: {
      appointmentId: {
        type: String,
        required: true,
      },
    },
    data() {
      return {
        appointment: null,
      };
    },
    created() {
      // Fetch appointment details from the backend
      this.fetchAppointmentDetails();
    },
    methods: {
      fetchAppointmentDetails() {
        // Make API call to fetch appointment details
        // Example using axios library
        axios.get(`/api/appointments/${this.appointmentId}/`)
          .then(response => {
            this.appointment = response.data;
          })
          .catch(error => {
            console.error('Failed to fetch appointment details:', error);
          });
      },
      rescheduleAppointment() {
        // Redirect to the appointment reschedule page with the appointment ID
        this.$router.push(`/reschedule/${this.appointmentId}`);
      },
      cancelAppointment() {
        // Redirect to the appointment cancel page with the appointment ID
        this.$router.push(`/cancel/${this.appointmentId}`);
      },
    },
  };
  </script>
  
  <style>
  .appointment-details {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .appointment-details h2 {
    margin-bottom: 20px;
  }
  
  .appointment-details .details {
    margin-bottom: 20px;
  }
  
  .appointment-details .details div {
    margin-bottom: 10px;
  }
  
  .appointment-details .actions button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
    margin-right: 10px;
  }
  
  .appointment-details .actions button:hover {
    background-color: #45a049;
  }
  </style>
  