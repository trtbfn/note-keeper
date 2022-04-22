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
                            <th scope="col">Note</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(note, index) in notes" :key="index">
                            <td>{{note.text}}</td>
                            <td>
                                <button type="button" class="btn btn-warning btn-sm">Update</button>
                                <button type="button" class="btn btn-danger btn-sm">Delete</button>
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
                          v-model="addNoteForm.text"
                          required
                          placeholder="Enter a note">
            </b-form-input>
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
                        label="Text"
                        label-for="from-text-edit-input">
            <b-form-input id="form-text-edit-input"
                          type="text"
                          v-model="editForm.text"
                          required
                          placeholder="Enter text">
            </b-form-input>
            <b-button type="submit" variant="primary">Update</b-button>
            <b-button type="reset" variant="danger">Cancel</b-button>
          </b-form-group>
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
        text: '',
      }   ,
      message: '',
      isMessageShowed: false
    };
  },
  methods: {
    getNotes() {
      const url = 'http://localhost:5000/api/get_notes'
      axios.get(url)
        .then(res => {
          this.notes = res.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    addNote(payload) {
      const url = 'http://localhost:5000/api/add_note';
      axios.post(url, payload)
        .then((res) => {
          this.message = res.data;
          this.isMessageShowed = true;
          this.getNotes();
        })
        .catch(error => {
          console.error(error)
          this.getNotes();
        })
    },
    initForm() {
      this.addNoteForm.text = '';
    },
    onSumbit(e) {
      e.preventDefault();
      this.$refs.addNoteModal.hide()
      const payload = {
        text: this.addNoteForm.text
      };
      this.addNote(payload);
      this.initForm();
    },
    onReset(e) {
      e.preventDefault();
      this.$refs.addNoteModal.hide()
      this.initForm();
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
