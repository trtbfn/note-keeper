<template>
	<b-container>
		<column :notes="notes"></column>
		<column :notes="notes"></column>
		<edit-screen></edit-screen>
	</b-container>
</template>

<script>
import axios from 'axios';
import Column from './Column.vue';
import Edit from './Edit.vue';

//Assets
const ipAddr = 'localhost',
			port = 3000,
			apiBase = `http://${ipAddr}:${port}/api/`;

export default {
	data() {
		return {
			notes: []
		}
	},
	methods: {
		getNotes() {
      axios.get(apiBase + 'notes')
        .then(res => {
          //Each note represents as a list with parameters
          this.notes = res.data.body;
        })
        .catch(error => {
          console.log(error);
        });
    },
		fillTwoCols() {

		}
    // addNote(payload) {
    //   axios.post(apiBase + 'notes', payload)
    //     .then((res) => {
    //       this.message = res.data.message;
    //       this.isMessageShowed = true;
    //       this.getNotes();
    //     })
    //     .catch(error => {
    //       console.error(error)
    //       this.getNotes();
    //     })
    // },
    // initForm() {
    //   this.addNoteForm.title = '';
    //   this.addNoteForm.text = '';
    //   this.editForm.title = '';
    //   this.editForm.text = '';
    //   this.editForm.id = null;
    // },
    // onSumbit(e) {
    //   e.preventDefault();
    //   this.$refs.addNoteModal.hide()
    //   const payload = {
    //     title: this.addNoteForm.title,
    //     text: this.addNoteForm.text,
    //   };
    //   this.addNote(payload);
    //   this.initForm();
    // },
    // onReset(e) {
    //   e.preventDefault();
    //   this.$refs.addNoteModal.hide()
    //   this.initForm();
    // },
    // editNote(id, title, text) {
    //   this.editForm = {id, title, text};
    // },
    // onEditNote(note) {
    //   // Note represents as a list
    //   this.editNote(note[0], note[1], note[2]);
    // },
    // onSubmitUpdate(e) {
    //   e.preventDefault();
    //   this.$refs.editNoteModal.hide();
    //   const payload = {
    //     title: this.editForm.title,
    //     text: this.editForm.text,
    //   }
    //   this.updateNote(payload, this.editForm.id);
    // },
    // updateNote(payload, noteId) {
    //   axios.put(apiBase + `notes/${noteId}`, payload)
    //     .then((res) => {
    //       this.getNotes();
    //       this.message = res.data.message;
    //       this.isMessageShowed = true;
    //     })
    //     .catch((error) => {
    //       console.error(error);
    //       this.getNotes();
    //     });
    // },
    // onResetUpdate(e) {
    //   e.preventDefault();
    //   this.$refs.editNoteModal.hide();
    //   this.initForm();
    //   this.getNotes();
    // },
    // removeNote(noteId) {
    //   axios.delete(apiBase + `notes/${noteId}`)
    //     .then((res) => {
    //       this.getNotes();
    //       this.message = res.data.message;
    //       this.isMessageShowed = true;
    //     })
    //     .catch(error => {
    //       console.error(error);
    //       this.getNotes();
    //     });
    // },
    // onDeleteNote(note) {
    //   // Note represents as a list
    //   this.removeNote(note[0])
    // }
	},
	components: {
		'column': Column,
		'edit-screen': Edit,
	},
	created() {
		this.getNotes();
	}
}
</script>