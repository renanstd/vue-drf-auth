import Vue from 'vue'
import axios from 'axios'

export default {
    getTodos() {
        const path = process.env.VUE_APP_BACKEND_URL + "/api/todos"
        const token = Vue.$cookies.get("auth").jwt.access
        axios.get(path, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        }).then((response) => {
            console.log(response.data)
        }).catch((error) => {
            console.log(error)
        })
    }
}
