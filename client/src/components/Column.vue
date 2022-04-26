<template>
    <b-row cols="6" >
				<b-col v-for="(note, index) in notes"
						:key="index"
						cols="5"
						class="m-4 border border-secondary rounded p-5">
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
export default {
	props: ['notes']
}
</script>