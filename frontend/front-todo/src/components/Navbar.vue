<template>
    <b-navbar
        variant="success"
        type="light"
        sticky="true"
    >
        <b-navbar-brand href="#">
            <b>Lista de tarefas</b>
        </b-navbar-brand>
        <b-navbar-nav class="ml-auto">
            <b-nav-text class="ml-auto">
                Usuário logado: {{ user }}
            </b-nav-text>
            <b-button pill v-if="user"
                variant="primary"
                type="submit"
            >Logout</b-button>
            <b-button pill v-else
                variant="primary"
                type="submit"
            >Login</b-button>
        </b-navbar-nav>
    </b-navbar>
</template>

<script>
export default {
    props: ['user'],
}
</script>
