<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-10">
                <h1>Books</h1>
                <hr><br><br>
                <button type="button" class="btn btn-success btn-sm" v-b-modal.note-modal>Add Note</button>
                <br><br>
                <alert :message="message" v-if="isMessageShowed"></alert>
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Title</th>
                            <th scope="col">Text</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(note, index) in notes" :key="index">
                            <td>{{note[1]}}</td>
                            <td>{{note[2]}}</td>
                            <td>
                                <button type="button" 
                                class="btn btn-warning btn-sm"
                                v-b-modal.note-update-modal
                                @click="onEditNote(note)">Update</button>
                                <button type="button" 
                                class="btn btn-danger btn-sm"
                                @click="onDeleteNote(note)">Delete</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <b-modal ref="addNoteModal"
              id="note-modal"
              title="Add a new note"
              hide-footer>
        <b-form @submit="onSumbit" @reset="onReset" class="w-100">
          <b-form-group id="form-title-group"
                        label="Title:"
                        lable-for="form-title-input">
            <b-form-input id="form-title-input"
                          type="text"
                          v-model="addNoteForm.title"
                          required
                          placeholder="Enter a note">
            </b-form-input>
          </b-form-group>
          <br>
          <b-form-group id="form-text-group"
                        label="Text:"
                        lable-for="form-text-textarea">
            <b-form-textarea id="form-text-textarea"
                             v-model="addNoteForm.text"
                             placeholder="Enter text"
                             no-resize>
            </b-form-textarea>
          </b-form-group>
          <br>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
      </b-modal>
      <b-modal ref="editNoteModal"
               id="note-update-modal"
               title="Update"
               hide-footer>
        <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
          <b-form-group id="form-text-edit-group"
                        label="Title:"
                        label-for="from-text-edit-input">
            <b-form-input id="form-text-edit-input"
                          type="text"
                          v-model="editForm.title"
                          required
                          placeholder="Enter text">
            </b-form-input>
          </b-form-group>
          <br>
          <b-form-group id="form-text-edit-group"
                        label="Text:"
                        lable-for="form-text-edit-tetarea">
            <b-form-textarea id="form-text-edit-textarea"
                             v-model="editForm.text"
                             placeholder="Enter text"
                             no-resize>
            </b-form-textarea>
          </b-form-group>
          <br>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-form>
      </b-modal>
    </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      notes: [],
      addNoteForm: {
        title: '',
        text: '',
      }   ,
      message: '',
      isMessageShowed: false,
      editForm: {
        id: null,
        title: '',
        text: '',
      }
    };
  },
  methods: {
    getNotes() {
      const url = 'http://localhost:3000/api/notes'
      axios.get(url)
        .then(res => {
          //Each note represents as a list with parameters
          this.notes = res.data.body;
        })
        .catch(error => {
          console.log(error);
        });
    },
    addNote(payload) {
      const url = 'http://localhost:3000/api/notes';
      axios.post(url, payload)
        .then((res) => {
          this.message = res.data.message;
          this.isMessageShowed = true;
          this.getNotes();
        })
        .catch(error => {
          console.error(error)
          this.getNotes();
        })
    },
    initForm() {
      this.addNoteForm.title = '';
      this.addNoteForm.text = '';
      this.editForm.title = '';
      this.editForm.text = '';
      this.editForm.id = null;
    },
    onSumbit(e) {
      e.preventDefault();
      this.$refs.addNoteModal.hide()
      const payload = {
        title: this.addNoteForm.title,
        text: this.addNoteForm.text,
      };
      this.addNote(payload);
      this.initForm();
    },
    onReset(e) {
      e.preventDefault();
      this.$refs.addNoteModal.hide()
      this.initForm();
    },
    editNote(id, title, text) {
      this.editForm = {id, title, text};
    },
    onEditNote(note) {
      // Note represents as a list
      this.editNote(note[0], note[1], note[2]);
    },
    onSubmitUpdate(e) {
      e.preventDefault();
      this.$refs.editNoteModal.hide();
      const payload = {
        title: this.editForm.title,
        text: this.editForm.text,
      }
      this.updateNote(payload, this.editForm.id);
    },
    updateNote(payload, noteId) {
      const url = `http://localhost:3000/api/notes/${noteId}`;
      axios.put(url, payload)
        .then((res) => {
          this.getNotes();
          this.message = res.data.message;
          this.isMessageShowed = true;
        })
        .catch((error) => {
          console.error(error);
          this.getNotes();
        });
    },
    onResetUpdate(e) {
      e.preventDefault();
      this.$refs.editNoteModal.hide();
      this.initForm();
      this.getNotes();
    },
    removeNote(noteId) {
      const url = `http://localhost:3000/api/notes/${noteId}`;
      axios.delete(url)
        .then((res) => {
          this.getNotes();
          this.message = res.data.message;
          this.isMessageShowed = true;
        })
        .catch(error => {
          console.error(error);
          this.getNotes();
        });
    },
    onDeleteNote(note) {
      // Note represents as a list
      this.removeNote(note[0])
    }
  },
  components: {
    alert: Alert,
  },
  created() {
    this.getNotes();
  }
}
</script>
