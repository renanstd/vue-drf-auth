<template>
    <navbar user="teste"></navbar>
</template>

<script>
import Navbar from './Navbar'

export default {
    data() {
        return {
            user: 'renan'
        }
    },
    components: {
        navbar: Navbar
    }
}
</script>
