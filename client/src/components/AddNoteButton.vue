<template>
	<button class="reject-styles">
		<bi-circle-fill></bi-circle-fill>
	</button>
</template>


<script>
import { BIconExclamationCircleFill } from "bootstrap-vue";

export default {
  components: {
    'bi-circle-fill': BIconExclamationCircleFill
  },
};
</script>

<style scoped>
button:focus {
	outline: none;
};

.reject-styles {
	all: unset;
	cursor: pointer;
};	
</style>