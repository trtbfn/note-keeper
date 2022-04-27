<template>
  <b-container>
    <b-row align-h="center">
      <b-col
        v-for="(note, index) in notes"
        :key="index"
        cols="5"
        class="m-3 border border-secondary rounded px-5 pb-5"
      >
        <b-container class="mt-4 between">
          <bi-pen-fill 
            class="h4"
            @click.prevent="openEditScreen(note[0])"
          ></bi-pen-fill>

          <span class="h2">|</span>

          <bi-trash 
            class="h3"
            @click.prevent="deleteNote(note[0])"
          ></bi-trash>
        </b-container>

        <h4 class="mt-2">{{ handleNoteContentNull(note[1]) }}</h4>
        <hr />
        
        <p class="text-break">
          {{ handleNoteContentNull(note[2]) }}
        </p>
      </b-col>
    </b-row>   
  </b-container>
</template>


<script>
import axios from "axios";
import { BIconPenFill, BIconTrash } from "bootstrap-vue";
import { store } from "@/store.js";

export default {
  props: ["notes"],
  components: {
    "bi-pen-fill": BIconPenFill,
    "bi-trash": BIconTrash,
  },
  data() {
    return {
      backNotesURL: store.backBaseURL,
    }
  },
  methods: {
    openEditScreen(note_id) {
      this.$router.push(`/${note_id}`);
    },
    deleteNote(note_id) {
      axios
        .delete(this.backNotesURL + `/notes/${note_id}`)
        .then((res) => {
          store.message = res.data.message;
          store.status = res.data.status;
          console.log('pushed')
          this.$router.go().catch(err=>console.error(err));
        })
        .catch((error) => {
          console.error(error);
          this.$router.catch(err=>console.error(err));;
        });
    },
    handleNoteContentNull(content) {
      if(content == null) return '';
      else {
        return content.length > 255
                ? content
                + "..." : content;
      }
    }
  }
};
</script>