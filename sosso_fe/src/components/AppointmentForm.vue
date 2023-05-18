<template>
    <div class="appointment-form">
      <h2>{{ formTitle }}</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="date">Date:</label>
          <input type="date" id="date" v-model="formData.date" required>
        </div>
        <div>
          <label for="time">Time:</label>
          <input type="time" id="time" v-model="formData.time" required>
        </div>
        <div>
          <label for="hairstyle">Hairstyle:</label>
          <select id="hairstyle" v-model="formData.hairstyle" required>
            <option v-for="hairstyle in hairstyles" :key="hairstyle.id" :value="hairstyle.id">
              {{ hairstyle.name }}
            </option>
          </select>
        </div>
        <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
        <button type="submit" class="btn">{{ buttonLabel }}</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import APIService from '@/http/APIService';

  export default {
    name: 'AppointmentForm',
    props: {
      appointmentId: {
        type: String,
        default: null,
      },
    },
    data() {
      return {
        formTitle: this.appointmentId ? 'Reschedule Appointment' : 'Schedule Appointment',
        buttonLabel: this.appointmentId ? 'Reschedule' : 'Schedule',
        hairstyles: [],
        formData: {
          date: '',
          time: '',
          hairstyle: '',
        },
        errorMessage: '',
      };
    },
    created() {
      // Fetch available hairstyles from the backend
      this.fetchHairstyles();
    },
    methods: {
      fetchHairstyles() {
      APIService.getHairstyles()
        .then(hairstyles => {
          this.hairstyles = hairstyles;
        })
        .catch(error => {
          console.error('Failed to fetch hairstyles:', error);
        });
    },
      submitForm() {
        // Validate form data
        if (!this.validateFormData()) {
          return;
        }
  
        // Prepare the data to be sent to the backend
        const { date, time, hairstyle } = this.formData;
        const appointmentData = {
          date,
          appointment_time: time,
          hairstyle,
        };
  
        // Make API call to create/update appointment
        // Example using axios library
        const endpoint = this.appointmentId ? `/api/appointments/${this.appointmentId}/` : '/api/appointments/';
        const httpMethod = this.appointmentId ? 'put' : 'post';
        axios[httpMethod](endpoint, appointmentData)
          .then(data => {
            // Handle successful form submission
            console.log('Appointment submitted successfully:', data);
            // Redirect to desired page or perform additional logic
          })
          .catch(error => {
            // Handle form submission error
            console.error('Failed to submit appointment:', error);
            this.errorMessage = 'Failed to submit appointment. Please try again.';
          });
      },
      validateFormData() {
        const { date, time, hairstyle } = this.formData;
        if (!date || !time || !hairstyle) {
          this.errorMessage = 'Please fill in all required fields.';
          return false;
        }
        return true;
      },
    },
  };
  </script>
  
  <style>
.appointment-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}

.appointment-form h2 {
  margin-bottom: 20px;
}

.appointment-form label {
  display: block;
  margin-bottom: 10px;
}

.appointment-form input[type="date"],
.appointment-form input[type="time"],
.appointment-form select {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
}

.appointment-form .error-message {
  color: red;
  margin-bottom: 10px;
}

.appointment-form button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
}

.appointment-form button:hover {
  background-color: #45a049;
}
</style>