import 'bootstrap/dist/css/bootstrap.css';
import Vue from 'vue';
import Router from 'vue-router';
import Notes from '@/components/Notes';
import EditScreen from '@/components/EditScreen';
import AddScreen from '@/components/AddScreen';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Notes',
      component: Notes,
    },
    {
      path: '/add',
      name: 'AddScreen',
      component: AddScreen,
    },
    {
      path: '/:id',
      name: 'EditScreen',
      component: EditScreen,
    },
  ],
  mode: 'history',
});
