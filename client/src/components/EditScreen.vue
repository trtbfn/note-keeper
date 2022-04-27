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
            @click="updateNote"
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
            v-model="editForm.title"
            required
            placeholder="Enter a title"
          >
          </b-form-input>
        </b-form-group>
        <br>
        <b-form-group
          id="form-text-group"
          label="Text:"
          lable-for="form-text-textarea"
        >
          <b-form-textarea
            id="form-text-textarea"
            v-model="editForm.text"
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
import { BIconX, BIconCheck } from "bootstrap-vue";
import { store } from "@/store.js";
import axios from "axios";

export default {
  data() {
    return {
      editForm: {
        title: '',
        text: '',
      },
			backNoteURL: null,
    };
  },
  methods: {
    getNoteData() {
      this.editForm.id = this.$route.params.id;
      this.backNoteURL = store.backBaseURL + `/notes/${this.editForm.id}`;
      axios.get(this.backNoteURL)
        .then((res) => {
          this.editForm.title = res.data.body[1];
          this.editForm.text = res.data.body[2];
          console.log(this.editForm);
        })
        .catch((error) => {
          console.error(error);
        });
    },
		updateNote() {
			const payload = {
				title: this.editForm.title,
				text: this.editForm.text
			};

			axios.put(this.backNoteURL, payload)
				.then(res => {
					store.message = res.data.message;
					store.isMessageExist = true;
          // Go to notes page
					this.$router.replace('/');
				})
				.catch(error => {
					console.error(error);
				});
		},
		closeNote() {
      // Go to notes page
			this.$router.replace('/');
		}
  },
  components: {
    'bi-close': BIconX,
    'bi-check': BIconCheck,
  },
  created() {
    this.getNoteData();
  },
};
</script>

