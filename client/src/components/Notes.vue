<template>
	<div>
    <column :notes="notes"></column>   
		<add-note-button class="add-btn"></add-note-button>
	</div>
</template>

<script>
//assets
import axios from "axios";
import { store } from "@/store.js";

//components
import Column from "./Column.vue";
import AddNoteButton from './AddNoteButton';


export default {
  data() {
    return {
      notes: [],
      backNotesURL: store.backBaseURL 
        + '/notes',
    };
  },
  methods: {
    getNotes() {
      axios
        .get(this.backNotesURL)
        .then((res) => {
          //Each note represents as a list with parameters
          this.notes = res.data.body;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  components: {
    'column': Column,
		'add-note-button': AddNoteButton
  },
  created() {
    this.getNotes();
  },
};
</script>

<style scoped>
.add-btn {
	position: fixed;
	right: 0;
	bottom: 0;
  cursor: pointer;
	transform: translate(-100%, -20%);
}
</style>

<style>
.point {
  cursor: pointer;
}
</style>