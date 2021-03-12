<template>
  <navbar></navbar>
</template>

<script>

import Navbar from "./Navbar"
import api from "./api"

export default {
  mounted() {
    api.getTodos()
  },
  components: {
    navbar: Navbar,
  },
}

</script>
