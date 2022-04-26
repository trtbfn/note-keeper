import Vue from 'vue';

//storage for events parameters
export const store = Vue.observable({
  isEditOpen: false,
});

export const mutations = {
  toggleEdit() {
    store.isEditOpen = !store.isEditOpen;
	},
};