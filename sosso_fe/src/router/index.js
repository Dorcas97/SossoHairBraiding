import { createRouter, createWebHistory } from 'vue-router';
import Hairstyles from '@/components/Hairstyles.vue';
import AppointmentForm from '@/components/AppointmentForm.vue';
import AppointmentDetails from '@/components/AppointmentDetails.vue';
import Home from '@/components/Home.vue';
import About from '@/components/About.vue';
import Gallery from '@/components/Gallery.vue';


const routes = [
  {
    path: '/',
    component: Home,
  },
  {
    path: '/hairstyles',
    name: 'Hairstyles',
    component: Hairstyles,
  },
  {
    path: '/schedule',
    component: AppointmentForm,
  },
  {
    path: '/reschedule/:appointmentId',
    component: AppointmentForm,
    props: true,
  },
  {
    path: '/cancel/:appointmentId',
    component: AppointmentForm,
    props: true,
  },
  {
    path: '/appointment/:appointmentId',
    component: AppointmentDetails,
    props: true,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
  {
    path: '/gallery',
    name: 'Gallery',
    component: Gallery,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});


export default router;
