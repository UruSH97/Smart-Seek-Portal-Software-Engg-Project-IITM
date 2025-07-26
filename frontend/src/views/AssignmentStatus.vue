<template>
    <div class="assignment-status-container">
        <header class="status-header">
            <h1>Assignment Status</h1>
            <nav class="dashboard-nav">
                <router-link to="/" class="nav-link">Home</router-link>
                <router-link to="/admin/dashboard" class="nav-link">Admin Dashboard</router-link>
                <router-link to="/admin/course/management" class="nav-link">Admin Course Management</router-link>
                <router-link to="/course/statistics" class="nav-link">Course Statistics</router-link>
                <router-link to="/student/details/management" class="nav-link">Student Details Management</router-link>
                <button class="logout-button">Log Out</button>
            </nav>
        </header>
        <div class="assignment-content">
            <h2>Assignment Status Overview:</h2>
            <table>
                <thead>
                    <tr>
                        <th>Assignment Title</th>
                        <th>Course</th>
                        <th>Deadline</th>
                        <th>Students Completed</th>
                        <th>Students Pending</th>
                        <th>Actions</th>
                        </tr>
                </thead>
                <tbody>
                    <tr v-for="assignment in assignments" :key="assignment.id">
                        <td>{{ assignment.title }}</td>
                        <td>{{ assignment.course }}</td>
                        <td>{{ assignment.deadline }}</td>
                        <td>
                            <ul>
                                <li v-for="student in assignment.completedStudents" :key="student.id">
                                    {{ student.name }}
                                </li>
                            </ul>
                        </td>
                        <td>
                            <ul>
                                <li v-for="student in assignment.pendingStudents" :key="student.id">
                                    {{ student.name }}
                                </li>
                            </ul>
                        </td>
                        <td>
                            <button @click="viewDetails(assignment.id)" class="details-button">View Details</button>
                            <button @click="editDeadline(assignment.id)" class="edit-button">Edit Deadline</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script>
export default {
    name: 'AssignmentStatus',
    data() {
        return {
            assignments: [
                {
                    id: 1,
                    title: 'Introduction to Programming - Assignment 1',
                    course: 'Introduction to Programming',
                    deadline: '2024-08-30',
                    completedStudents: [
                        { id: 1, name: 'Alice Johnson' },
                        { id: 2, name: 'Bob Smith' }
                    ],
                    pendingStudents: [
                        { id: 3, name: 'Charlie Brown' },
                        { id: 4, name: 'David Wilson' }
                    ]
                },
                {
                    id: 2,
                    title: 'Advanced Python - Project',
                    course: 'Advanced Python',
                    deadline: '2024-09-05',
                    completedStudents: [
                        { id: 1, name: 'Eve Adams' },
                        { id: 2, name: 'Frank Taylor' }
                    ],
                    pendingStudents: [
                        { id: 3, name: 'Grace Hopper' },
                        { id: 4, name: 'Heidi Klum' }
                    ]
                }
            ]
        };
    },
    methods: {
        viewDetails(assignmentId) {
            alert(`Viewing details for assignment ID: ${assignmentId}`);
            // Logic to view detailed information about the assignment
        },
        editDeadline(assignmentId) {
            const newDeadline = prompt('Enter new deadline (YYYY-MM-DD):');
            if (newDeadline) {
                const assignment = this.assignments.find(a => a.id === assignmentId);
                if (assignment) {
                    assignment.deadline = newDeadline;
                }
            }
        }
    }
};
</script>
<style scoped>
.assignment-status-container {
    padding: 20px;
    background-color: #f4f4f4;
    min-height: 100vh;
}
.status-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #e0e0e0;
    padding: 15px;
    border-radius: 5px;
}
.status-header h1 {
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
.assignment-content {
    margin-top: 20px;
}
.assignment-content h2 {
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
.details-button,
.edit-button {
    background-color: #08a9ee;
    color: white;
    border: none;
    padding: 8px 12px;
    border-radius: 5px;
    cursor: pointer;
    margin-right: 10px;
}
</style>


  

