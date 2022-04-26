<template>
    <b-row cols="6">
				<b-col v-for="(note, index) in notes"
						:key="index"
						cols="5"
						class="m-4 border border-secondary rounded p-5">
							<b-container>
								<b-row>
									<bi-pencil-fill @click="updateNote(note.id)"></bi-pencil-fill>
									<bi-trash @click="deleteNote(note.id)"></bi-trash>
								</b-row>
							</b-container>

							<!-- note title -->
							<h4>{{ note[1] }}</h4>
							<hr>
							<!-- note text -->
							<p class="text-break">{{ note[2].length > 255?
										note[2].substring(0, 255) + '...':
										note[2] }}</p>
				</b-col>
    </b-row>
</template>

<script>
import {store, mutations} from '@/store.js';
import {BIconTrash, BIconPencilFill} from 'bootstrap-vue';

export default {
	data() {
		return {

		}
	},
	props: ['notes'],
	methods: {

	},
	components: {
		'bi-trash': BIconTrash,
		'bi-pencil-fill': BIconPencilFill,
	}
}
</script>