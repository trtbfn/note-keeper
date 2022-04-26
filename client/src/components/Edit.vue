<template>
  <div class="edit">
    <div class="sidebar-backdrop" v-if="isEditScreenClosed">
			<transition name="slide">
				<div class="sidebar-panel" v-if="isEditScreenClosed">
					<b-container >
						<b-row align-h="between">	
								<b-col col offset="1">
									<bi-con-arrow-left @click="closeEdit"></bi-con-arrow-left>
								</b-col>
								<b-col col offset="8">
									<bi-trash></bi-trash>
								</b-col>
								<hr>
								
								<b-form @submit="onEditSumbit" class="w-100">
									<b-form-group id="form-title-group"
																label="Title:"
																lable-for="form-title-input">
										<b-form-input id="form-title-input"
																	type="text"
																	v-model="editForm.title"
																	required
																	placeholder="Enter a note">
										</b-form-input>
									</b-form-group>
									<br>
									<b-form-group id="form-text-group"
																label="Text:"
																lable-for="form-text-textarea">
										<b-form-textarea id="form-text-textarea"
																		v-model="editForm.text"
																		placeholder="Enter text"
																		no-resize>
										</b-form-textarea>
									</b-form-group>
									<br>
									<b-button type="submit" variant="primary">Submit</b-button>
								</b-form>
						</b-row>
					</b-container>
				</div>
			</transition>
    </div>
  </div>
</template>

<script>
import { BIconArrowLeft, BIconTrash } from "bootstrap-vue";
import { store, mutations } from "@/store.js";

export default {
  data() {
    return {
			editForm: {
				id: '',
				title: '',
				text: '',
			}
		};
  },
  methods: {
    closeEditScreen: mutations.toggleEdit,
		onEditSubmit() {

		},
		closeEdit() {
			
		}
  },
  computed: {
    isEditScreenClosed() {
      return store.isEditOpen;
    },
  },
  components: {
    "bi-con-arrow-left": BIconArrowLeft,
    "bi-trash": BIconTrash,
  },
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