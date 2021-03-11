<template>
  <b-navbar variant="info">
    <b-container fluid>
      <b-col>
        <b-navbar-brand href="#">
          <b>Lista de tarefas</b>
        </b-navbar-brand>
      </b-col>
      <b-col>
        <b-row align-h="center">
          <span>Bem vindo, {{ username }}</span>
        </b-row>
      </b-col>
      <b-col>
        <b-button v-on:click="logout" size="sm" class="float-right"> Logout </b-button>
      </b-col>
    </b-container>
  </b-navbar>
</template>

<script>

import route from '../router'

export default {
  mounted() {
    this.username = this.$cookies.get("auth").username
  },
  data() {
    return {
      username: null
    }
  },
  methods: {
    logout() {
      this.$cookies.remove("auth")
      route.push('/login')
    }
  }
}
</script>
