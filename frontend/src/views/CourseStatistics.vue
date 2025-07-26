<template>
    <div class="course-statistics-container">
        <header class="statistics-header">
            <h1>Course Statistics</h1>
            <nav class="dashboard-nav">
                <router-link to="/" class="nav-link">Home</router-link>
                <router-link to="/admin/dashboard" class="nav-link">Admin Dashboard</router-link>
                <router-link to="/admin/course/management" class="nav-link">Admin Course Management</router-link>
                <router-link to="/student/details/management" class="nav-link">Student Details Management</router-link>
                <router-link to="/assignment/status" class="nav-link">Assignment Status</router-link>
                <button class="logout-button">Log Out</button>
            </nav>
        </header>
        <div class="statistics-content">
            <h2>All Courses Statistics:</h2>
            <table>
                <thead>
                    <tr>
                        <th>Course Name</th>
                        <th>Enrolled Students</th>
                        <th>Average Rating</th>
                        <th>Total Hours of Content</th>
                        <th>Completed Percentage</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="course in courseStatistics" :key="course.id">
                        <td>{{ course.name }}</td>
                        <td>{{ course.enrolledStudents }}</td>
                        <td>{{ course.averageRating }}</td>
                        <td>{{ course.totalHours }}</td>
                        <td>{{ course.completedPercentage }}%</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script>
export default {
    name: "CourseStatistics",
    data() {
        return {
            courseStatistics: [
                // Example data, this would typically be fetched from an API or backend
                {
                    id: 1,
                    name: "Introduction to Programming",
                    enrolledStudents: 150,
                    averageRating: 4.5,
                    totalHours: 12,
                    completedPercentage: 75,
                },
                {
                    id: 2,
                    name: "Advanced Python",
                    enrolledStudents: 90,
                    averageRating: 4.8,
                    totalHours: 20,
                    completedPercentage: 60,
                },
                {
                    id: 3,
                    name: "Data Science Basics",
                    enrolledStudents: 200,
                    averageRating: 4.7,
                    totalHours: 15,
                    completedPercentage: 80,
                },
            ],
        };
    },
};
</script>
<style scoped>
.course-statistics-container {
    padding: 20px;
    background-color: #f4f4f4;
    min-height: 100vh;
}  
.statistics-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #e0e0e0;
    padding: 15px;
    border-radius: 5px;
}
.statistics-header h1 {
    font-size: 24px;
    margin: 0;
}
.logout-button {
    background-color: #ff0000;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}
.statistics-content {
    margin-top: 20px;
}
.statistics-content h2 {
    margin-bottom: 20px;
} 
table {
    width: 100%;
    border-collapse: collapse;
    background-color: white;
    border-radius: 5px;
    overflow: hidden;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
table th,
table td {
    padding: 15px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
table th {
    background-color: #f4f4f4;
}
</style>





  