<template>
    <div class="dashboard-container">
        <header class="dashboard-header">
            <h1>Admin Dashboard</h1>
            <nav class="dashboard-nav">
                <router-link to="/" class="nav-link">Home</router-link>
                <router-link to="/course/statistics" class="nav-link">Course Statistics</router-link>
                <router-link to="/admin/course/management" class="nav-link">Admin Course Management</router-link>
                <router-link to="/student/details/management" class="nav-link">Student Details Management</router-link>
                <router-link to="/assignment/status" class="nav-link">Assignment Status</router-link>
                <button class="logout-button">Log Out</button>
            </nav>
        </header>
        <div class="dashboard-content">
            <div class="dashboard-item">
                <p>Total Students</p>
                <h3>263</h3>
            </div>
            <div class="dashboard-item">
            <p>Total Instructors</p>
            <h3>14</h3>
            </div>
            <div class="dashboard-item">
            <p>New Student Users</p>
            <h3>23</h3>
            </div>
            <div class="dashboard-item large">
            <p>New Lectures Uploaded</p>
            <div class="circle">
                <span>32</span>
            </div>
            <div class="timeframe">
                <label><input type="radio" name="timeframe" checked>Today</label>
                <label><input type="radio" name="timeframe">Week</label>
                <label><input type="radio" name="timeframe">Month</label>
            </div>
        </div>
        <div class="dashboard-item large">
            <p>Total Lectures Uploaded</p>
            <div class="circle">
                <span>132</span>
            </div>
        </div>
        <div class="dashboard-item small">
            <p>Flagged Students</p>
            <h3>4</h3>
            <button class="flag-button">&gt;</button>
        </div>
    </div>
    </div>
</template>
<script>
  export default {
    name: 'AdminDashboard',
  };
</script>
<style scoped>
.dashboard-container {
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    background-color: #f4f4f4;
}
.dashboard-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #e0e0e0;
    padding: 20px;
}  
.dashboard-header h1 {
    font-size: 24px;
} 
.dashboard-nav {
    display: flex;
}
.nav-link {
    margin-right: 20px;
    text-decoration: none;
    color: black;
    font-size: 16px;
} 
.logout-button {
    background-color: #ff0000;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}
.dashboard-content {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    padding: 20px;
}
.dashboard-item {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    text-align: center;
} 
.dashboard-item.large {
    grid-column: span 2;
} 
.dashboard-item.small {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.circle {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background-color: #efefef;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 auto;
    font-size: 24px;
    color: #333;
}
.timeframe {
    display: flex;
    justify-content: center;
    margin-top: 10px;
} 
.timeframe label {
    margin: 0 10px;
} 
.flag-button, .category-button {
    background-color: #08a9ee;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 20px;
}
</style>









  