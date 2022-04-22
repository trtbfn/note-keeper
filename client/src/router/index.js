import 'bootstrap/dist/css/bootstrap.css';
import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Notes from '@/components/Notes';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/notes',
      name: 'Notes',
      component: Notes,
    },
  ],
  mode: 'history',
});
