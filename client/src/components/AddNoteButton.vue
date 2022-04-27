<template>
	<bi-plus-circle-fill 
		class="h1"
		@click="addNote"
	></bi-plus-circle-fill>
</template>


<script>
import { BIconPlusCircleFill } from "bootstrap-vue";

export default {
  components: {
    'bi-plus-circle-fill': BIconPlusCircleFill
  },
  methods: {
		addNote() {
			this.$router.push('/add');
		}
  }
};
</script>
