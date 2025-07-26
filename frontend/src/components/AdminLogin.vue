<template>
    <div class="register-container">
        <div class="login-form">
            <h2>Login as Admin</h2>
            <form @submit.prevent="handleLogin">
                <div class="form-group">
                    <label for="username">Admin Username:</label>
                    <input type="text" id="username" v-model="username" required autocomplete="username">
                </div>
                <div class="form-group">
                    <label for="password">Admin Password:</label>
                    <input type="password" id="password" v-model="password" required autocomplete="new-password">
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
        <div class="admin-link">
            <router-link to="/login/student" class="admin-button">Go to Student Login</router-link>
            <router-link to="/login/instructor" class="admin-button">Go to Instructor Login</router-link>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import { useRouter } from 'vue-router';
export default {
    name: 'AdminLogin',
    data() {
        return {
            username: '',
            password: ''
        };
    },
    setup() {
        const router = useRouter();

        return {
            router
        };
    },
    methods: {
        async handleLogin() {
            try {
                const response = await axios.post('/api/admin/login', {
                    username: this.username,
                    password: this.password
                });
                if (response.data.success) {
                    // Redirect to the admin dashboard after successful login
                    this.router.push({ name: 'admindashboard' });
                } else {
                    // Handle login error
                    alert('Login failed: ' + response.data.message);
                }
            } catch (error) {
                console.error('An error occurred during login:', error);
                alert('An error occurred. Please try again.');
            }
        }
    }
};
</script>
<style scoped>
.login-form {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 15px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    background-color: #efefef;
    width: 400px;
    margin: 0 auto;
    margin-top: 50px;
}
.admin-link {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    margin-top: 20px;
}
.admin-link p {
    margin-bottom: 10px;
    font-size: 14px;
    color: #555;
}
.admin-button {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 50px;
    background-color: #fff;
    color: #57e87b;
    border: 2px solid #42e955;
    text-decoration: none;
    font-size: 16px;
    transition: background-color 0.2s, color 0.2s, border-color 0.2s;
}
.admin-button:hover {
    background-color: #08a9ee;
    color: #fff;
    border-color: transparent;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
}
.admin-button:active {
    background-color: #08b8ee;
    border-color: transparent;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
}
.admin-button:focus {
    outline: none;
}
.register-container {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background-color: lemonchiffon;
    background-size: cover;
    background-position: center;
    flex-direction: column;
}
h2 {
    font-size: 24px;
    margin-bottom: 20px;
}
form {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.form-group {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
    width: 100%;
}
label {
    font-weight: bold;
    margin-right: 10px;
    flex: 1;
    text-align: right;
}
input {
    flex: 2;
}
label {
    font-weight: bold;
    margin-right: 10px;
    margin-bottom: 10px;
}
input {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 100%;
    max-width: 300px;
}
button {
    background-color: #14c0eb;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.2s ease;
    margin-top: 20px;
}
button:hover {
    background-color: #0b8fa2;
}
button:active {
    background-color: #0c7b8c;
}
button:focus {
    outline: none;
}
</style>

