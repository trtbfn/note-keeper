import Vue from 'vue';

const port = 3000;
const baseUrl = `http://localhost:${port}/api/`;

//storage for events parameters
export const store = Vue.observable({
  baseUrl,
  isEditOpen: false,
  editForm: {
    id: '',
    title: '',
    text: '',
  }
});

export const mutations = {
  toggleEdit() {
    store.isEditOpen = !store.isEditOpen;
	},
  initEditForm() {
    store.editForm.id = '';
    store.editForm.title = '';
    store.editForm.text = '';
  }
};