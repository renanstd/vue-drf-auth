<template>
  <b-container>
    <b-row>
      <h1>Login</h1>
    </b-row>
    <b-form @submit="onSubmit">

      <b-row>
        <b-form-group
          id="input-group-user"
          label="User:"
          label-for="input-user"
        >
        </b-form-group>
        <b-form-input
          id="input-user"
          v-model="loginForm.user"
          type="text"
          required
        ></b-form-input>
      </b-row>

      <br>

      <b-row>
        <b-form-group
          id="input-group-pass"
          label="Password:"
          label-for="input-pass"
        >
        </b-form-group>
        <b-form-input
          id="input-pass"
          v-model="loginForm.password"
          type="password"
          required
        ></b-form-input>
      </b-row>

      <br>

      <b-row>
        <b-button type="submit" variant="primary">Login</b-button>
      </b-row>
    </b-form>
  </b-container>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      loginForm: {
        user: '',
        password: ''
      }
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      const payload = {
        username: this.loginForm.user,
        password: this.loginForm.password,
      }
      const path = "http://localhost:8000/api/token/";
      axios.post(path, payload)
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      })
    }
  }
}
</script>
