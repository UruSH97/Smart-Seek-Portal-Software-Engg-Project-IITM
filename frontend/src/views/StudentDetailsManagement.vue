<template>
    <div class="student-details-management-container">
        <header class="management-header">
            <h1>Student Details Management</h1>
            <nav class="dashboard-nav">
                <router-link to="/" class="nav-link">Home</router-link>
                <router-link to="/course/statistics" class="nav-link">Course Statistics</router-link>
                <router-link to="/admin/dashboard" class="nav-link">Admin Dashboard</router-link>
                <router-link to="/admin/course/management" class="nav-link">Admin Course Management</router-link>
                <router-link to="/assignment/status" class="nav-link">Assignment Status</router-link>
                <button class="logout-button">Log Out</button>
            </nav>
            <button class="add-student-button" @click="toggleAddStudentForm">Add New Student</button>
        </header>
        <div v-if="showAddStudentForm" class="add-student-form">
            <h2>Add New Student:</h2>
            <form @submit.prevent="addStudent">
                <div class="form-group">
                    <label for="studentName">Student Name:</label>
                    <input v-model="newStudent.name" type="text" id="studentName" required />
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input v-model="newStudent.email" type="email" id="email" required />
                </div>
                <div class="form-group">
                    <label for="enrollmentDate">Enrollment Date:</label>
                    <input v-model="newStudent.enrollmentDate" type="date" id="enrollmentDate" required />
                </div>
                <div class="form-group">
                    <label for="course">Course:</label>
                    <input v-model="newStudent.course" type="text" id="course" required />
                </div>
                <button type="submit" class="submit-button">Add Student</button>
            </form>
        </div>
        <div class="student-list">
            <h2>Existing Students</h2>
            <table>
                <thead>
                    <tr>
                        <th>Student Name</th>
                        <th>Email</th>
                        <th>Enrollment Date</th>
                        <th>Course</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="student in students" :key="student.id">
                        <td>{{ student.name }}</td>
                        <td>{{ student.email }}</td>
                        <td>{{ student.enrollmentDate }}</td>
                        <td>{{ student.course }}</td>
                        <td>
                            <button @click="editStudent(student.id)" class="edit-button">Edit</button>
                            <button @click="deleteStudent(student.id)" class="delete-button">Delete</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script>
export default {
    name: 'StudentDetailsManagement',
    data() {
        return {
            showAddStudentForm: false,
            newStudent: {
                name: '',
                email: '',
                enrollmentDate: '',
                course: ''
            },
            students: [
                // Example data
                { id: 1, name: 'Alice Johnson', email: 'alice@example.com', enrollmentDate: '2024-01-15', course: 'Introduction to Programming' },
                { id: 2, name: 'Bob Smith', email: 'bob@example.com', enrollmentDate: '2024-02-20', course: 'Advanced Python' }
            ]
        };
    },
    methods: {
        toggleAddStudentForm() {
            this.showAddStudentForm = !this.showAddStudentForm;
        },
        addStudent() {
            const newId = this.students.length + 1;
            this.students.push({ ...this.newStudent, id: newId });
            this.newStudent = { name: '', email: '', enrollmentDate: '', course: '' };
            this.toggleAddStudentForm();
        },
        editStudent(studentId) {
            // Logic for editing a student
            alert(`Edit student with ID: ${studentId}`);
        },
        deleteStudent(studentId) {
            // Logic for deleting a student
            this.students = this.students.filter(student => student.id !== studentId);
        }
    }
};
</script>
<style scoped>
.student-details-management-container {
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
.add-student-button {
    background-color: #08a9ee;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}
.add-student-form {
    margin: 20px 0;
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.add-student-form h2 {
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
.student-list {
    margin-top: 20px;
}
.student-list h2 {
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



