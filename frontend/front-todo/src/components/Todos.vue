<template>
  <b-container fluid>
    <navbar></navbar>
    <b-row>
      <b-col>
        <h2>Todo</h2>
        <b-table striped hover :items="todos" :fields="fields">

        </b-table>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>

import Navbar from "./Navbar"
import axios from 'axios'
import router from '../router'

export default {
  data() {
    return {
      fields: ['name', 'content', 'date', 'done'],
      todos: []
    }
  },

  mounted() {
    this.getTodos()
  },

  components: {
    navbar: Navbar,
  },

  methods: {
    getTodos() {
      const path = process.env.VUE_APP_BACKEND_URL + "/api/todos"
      const token = this.$cookies.get("auth").jwt.access
      axios.get(path, {
          headers: {
              'Authorization': `Bearer ${token}`
          }
      }).then((response) => {
          const data = response.data
          console.log(data)
          this.todos = data
      }).catch((error) => {
          const status = error.response.status
          if (status === 401) {
              this.$cookies.remove("auth")
              router.push('/login')
          } else {
              console.log(error.response.data)
          }
      })
    }
  }
}

</script>
