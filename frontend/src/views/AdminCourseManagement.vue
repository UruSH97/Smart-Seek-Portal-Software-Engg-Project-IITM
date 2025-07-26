<template>
    <div class="admin-course-management-container">
        <header class="management-header">
            <h1>Admin Course Management</h1>
            <nav class="dashboard-nav">
                <router-link to="/" class="nav-link">Home</router-link>
                <router-link to="/course/statistics" class="nav-link">Course Statistics</router-link>
                <router-link to="/admin/dashboard" class="nav-link">Admin Dashboard</router-link>
                <router-link to="/student/details/management" class="nav-link">Student Details Management</router-link>
                <router-link to="/assignment/status" class="nav-link">Assignment Status</router-link>
                <button class="logout-button">Log Out</button>
            </nav>
            <button class="add-course-button" @click="toggleAddCourseForm">Add New Course</button>
        </header>
        <div v-if="showAddCourseForm" class="add-course-form">
            <h2>Add New Course:</h2>
            <form @submit.prevent="addCourse">
                <div class="form-group">
                    <label for="courseName">Course Name:</label>
                    <input v-model="newCourse.name" type="text" id="courseName" required />
                </div>
                <div class="form-group">
                    <label for="instructor">Instructor:</label>
                    <input v-model="newCourse.instructor" type="text" id="instructor" required />
                </div>
                <div class="form-group">
                    <label for="duration">Duration (weeks):</label>
                    <input v-model="newCourse.duration" type="number" id="duration" required />
                </div>
                <div class="form-group">
                    <label for="description">Description:</label>
                    <textarea v-model="newCourse.description" id="description" required></textarea>
                </div>
                <button type="submit" class="submit-button">Add Course</button>
            </form>
        </div>
        <div class="course-list">
            <h2>Existing Courses</h2>
            <table>
                <thead>
                    <tr>
                        <th>Course Name</th>
                        <th>Instructor</th>
                        <th>Duration</th>
                        <th>Description</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="course in courses" :key="course.id">
                        <td>{{ course.name }}</td>
                        <td>{{ course.instructor }}</td>
                        <td>{{ course.duration }} weeks</td>
                        <td>{{ course.description }}</td>
                        <td>
                        <button @click="editCourse(course.id)" class="edit-button">Edit</button>
                        <button @click="deleteCourse(course.id)" class="delete-button">Delete</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script>
export default {
    name: 'AdminCourseManagement',
    data() {
      return {
        showAddCourseForm: false,
        newCourse: {
          name: '',
          instructor: '',
          duration: '',
          description: ''
        },
        courses: [
          // Example data
          { id: 1, name: 'Introduction to Programming', instructor: 'John Doe', duration: 6, description: 'Learn the basics of programming.' },
          { id: 2, name: 'Advanced Python', instructor: 'Jane Smith', duration: 8, description: 'Deep dive into Python programming.' }
        ]
      };
    },
methods: {
    toggleAddCourseForm() {
        this.showAddCourseForm = !this.showAddCourseForm;
    },
    addCourse() {
        const newId = this.courses.length + 1;
        this.courses.push({ ...this.newCourse, id: newId });
        this.newCourse = { name: '', instructor: '', duration: '', description: '' };
        this.toggleAddCourseForm();
    },
    editCourse(courseId) {
        // Logic for editing a course
        alert(`Edit course with ID: ${courseId}`);
    },
    deleteCourse(courseId) {
        // Logic for deleting a course
        this.courses = this.courses.filter(course => course.id !== courseId);
    }
}
};
</script>
<style scoped>
.admin-course-management-container {
    padding: 20px;
    background-color: #f4f4f4;
    min-height: 100vh;
}
.management-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #e0e0e0;
    padding: 15px;
    border-radius: 5px;
}
.management-header h1 {
    font-size: 24px;
    margin: 0;
}
.add-course-button {
    background-color: #08a9ee;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}
.add-course-form {
    margin: 20px 0;
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.add-course-form h2 {
    margin-bottom: 20px;
}
.form-group {
    margin-bottom: 15px;
}
.form-group label {
    display: block;
    margin-bottom: 5px;
}  
.form-group input,
.form-group textarea {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
textarea {
    resize: vertical;
}
.submit-button {
    background-color: #08a9ee;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}
.logout-button {
    background-color: #ff0000;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}
.course-list {
    margin-top: 20px;
}
.course-list h2 {
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
.edit-button {
    background-color: #08a9ee;
    color: white;
    border: none;
    padding: 8px 12px;
    border-radius: 5px;
    cursor: pointer;
    margin-right: 10px;
}
.delete-button {
    background-color: #ff0000;
    color: white;
    border: none;
    padding: 8px 12px;
    border-radius: 5px;
    cursor: pointer;
}
</style>




  