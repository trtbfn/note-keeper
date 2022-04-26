import 'bootstrap/dist/css/bootstrap.css';
import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Notes from '@/components/Notes';
import Notes1 from '@/components/Notes1';

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
    {
      path: '/notes1',
      name: 'Notes1',
      component: Notes1,
    },
  ],
  mode: 'history',
});
