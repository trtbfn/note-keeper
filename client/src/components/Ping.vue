<template>
    <div class="container">
      <button class="btn btn-primary">{{msg}}</button>
    </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: 'pong!',
    }
  },
  methods: {
    getMessage() {
    const url = 'http://localhost:3000/ping';
    axios.get(url)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
            })
        }
    },
  created() {
    this.getMessage();
  }
};
</script>
