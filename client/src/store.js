import Vue from 'vue';

const backDomen = 'localhost',
      backPort = 5000,
      frontDomen = 'localhost',
      frontPort = 8080;

//storage for events parameters
export const store = Vue.observable({
  isEditOpen: false,
  info: {
    message: '',
    status: 200,
    isMessageGot: false,
  },
  backBaseURL: `http://${backDomen}:${backPort}/api`,
  frontBaseURL: `http://${frontDomen}:${frontPort}`,
});

export const mutations = {
  toggleEdit() {
    store.isEditOpen = !store.isEditOpen;
	},
};