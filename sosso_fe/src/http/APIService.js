import axios from 'axios';

const API_URL = 'http://dorcas.pythonanywhere.com/api/';

export default {
  getHairstyles() {
    return axios.get(API_URL + 'hairstyles/')
      .then(response => response.data)
      .catch(error => {
        throw new Error('Failed to fetch hairstyles: ' + error);
      });
  },

  getAppointments() {
    return axios.get(API_URL + 'appointments/')
      .then(response => response.data)
      .catch(error => {
        throw new Error('Failed to fetch appointments: ' + error);
      });
  },

  createAppointment(appointmentData) {
    return axios.post(API_URL + 'appointments/', appointmentData)
      .then(response => response.data)
      .catch(error => {
        throw new Error('Failed to create appointment: ' + error);
      });
  },

  updateAppointment(appointmentId, appointmentData) {
    return axios.put(API_URL + `appointments/${appointmentId}/`, appointmentData)
      .then(response => response.data)
      .catch(error => {
        throw new Error('Failed to update appointment: ' + error);
      });
  },

  deleteAppointment(appointmentId) {
    return axios.delete(API_URL + `appointments/${appointmentId}/`)
      .then(response => response.data)
      .catch(error => {
        throw new Error('Failed to delete appointment: ' + error);
      });
  },

  getStylists() {
    return axios.get(API_URL + 'stylists/')
      .then(response => response.data)
      .catch(error => {
        throw new Error('Failed to fetch stylists: ' + error);
      });
  },

  createStylist(stylistData) {
    return axios.post(API_URL + 'stylists/', stylistData)
      .then(response => response.data)
      .catch(error => {
        throw new Error('Failed to create stylist: ' + error);
      });
  },

  updateStylist(stylistId, stylistData) {
    return axios.put(API_URL + `stylists/${stylistId}/`, stylistData)
      .then(response => response.data)
      .catch(error => {
        throw new Error('Failed to update stylist: ' + error);
      });
  },

  deleteStylist(stylistId) {
    return axios.delete(API_URL + `stylists/${stylistId}/`)
      .then(response => response.data)
      .catch(error => {
        throw new Error('Failed to delete stylist: ' + error);
      });
  },
};

