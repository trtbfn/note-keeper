<template>
  <b-container>
    <b-row align-h="center" align-v="center">
      <b-container>
          <bi-close 
            class="h1 point"
            @click="closeNote"
          ></bi-close>
          <bi-check 
            class="h1 point"
            @click="addNote"
          ></bi-check>
      </b-container>
        

      <b-form class="w-100">
        <b-form-group
          id="form-title-group"
          label="Title:"
          lable-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            type="text"
            v-model="addForm.title"
            required
            placeholder="Enter a title"
          >
          </b-form-input>
        </b-form-group>
        <br />
        <b-form-group
          id="form-text-group"
          label="Text:"
          lable-for="form-text-textarea"
        >
          <b-form-textarea
            id="form-text-textarea"
            v-model="addForm.text"
            placeholder="Enter text"
            no-resize
            rows="14"
          >
          </b-form-textarea>
        </b-form-group>
        <br />
      </b-form>
    </b-row>
  </b-container>
</template>

<script>
import { BIconCheck, BIconX } from "bootstrap-vue";
import { store } from '@/store.js';
import axios from "axios";

export default {
  data() {
    return {
			addForm: {
				title: '', 
				text: '',
    	}
		}
  },
	methods: {
		addNote() {
			const payload = {
				title: this.addForm.title,
				text: this.addForm.text,
			}

			axios.post(store.backBaseURL + '/notes', payload)
				.then(res => {
					store.message = res.data.message;
					store.isMessageExist = true;
          // Go to frontpage
					this.$router.replace('/');
				})
				.catch(error => {
					console.error(error);
				});
		},
		closeNote() {
      // Go to frontpage
			this.$router.replace('/');
		}
	},
	components: {
		'bi-check': BIconCheck,
		'bi-close': BIconX,
	}
};
</script>



