<template> 
	<div>
		<b-container>
			<b-row align-h="between">
				<b-col col offset="1">
					<bi-arrow-left @click="closeEdit"></bi-con-arrow-left>
					<bi-check-lg></bi-check-lg>	
				</b-col>
				<br>
			</b-row>
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
            placeholder="Enter a note"
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
            v-model="editForm.text"
            placeholder="Enter text"
            no-resize
          >
          </b-form-textarea>
        </b-form-group>
        <br />
        <b-button type="submit" variant="primary">Submit</b-button>
      </b-form>
	</div>
</template>

<script>
import { BIconArrowLeft, BIconCheckLg } from "bootstrap-vue";
import { store, mutations } from "@/store.js";
import axios from 'axios';

export default {
  data() {
    return {
      editForm: {
        title: "",
        text: ""
      }
    };
  },
  methods: {
    closeEditScreen: mutations.toggleEdit,
    getDataNote() {
			axios.get(store.baseUrl + `notes/${this.$route.params.id}`)
				.then((res) => {
					this.editNote.title = res.data.body.title;
					this.editNote.text = res.data.body.text;		
				})
				.catch(error => {
					console.error(error);
				})
		}
  },
  components: {
    "bi-arrow-left": BIconArrowLeft,
    "bi-check-lg": BIconCheckLg,
  },
	created(): {
		this.getDataNote();
	}
};
</script>

<style>
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.2s ease;
}

.slide-enter,
.slide-leave-to {
  transform: translateX(-100%);
  transition: all 150ms ease-in 0s;
}

.sidebar-backdrop {
  background-color: rgba(0, 0, 0, 0.5);
  width: 100vw;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  cursor: pointer;
}

.sidebar-panel {
  overflow-y: auto;
  background-color: #130f40;
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh;
  z-index: 999;
  padding: 3rem 20px 2rem 20px;
  width: 300px;
}
</style>
