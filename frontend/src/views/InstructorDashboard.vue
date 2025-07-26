<template>
  <div class="instructor-dashboard">
    <header>
      <h1>{{ instructor.first_name }} {{ instructor.last_name }}</h1>
      <p>{{ instructor.email }}</p>
      <button @click="logout">Logout</button>
    </header>
    <main>
      <button class="create-course-btn" @click="navigateToCreateCourse">Create New Course</button>
      <ul class="courses-list">
        <li v-for="course in filteredCourses" :key="course.id"><center>
          {{ course.title }} </center>
          <br>
          <div class="button-group">
            <button @click="navigateToCourseDetails(course.id)">View</button>
            <button @click="navigateToUpdateCourse(course.id)">Update</button>
            <button @click="confirmDeleteCourse(course.id)">Delete</button>
          </div>
        </li>
      </ul>
    </main>
  </div>
</template>

<script>
export default {
  name: 'InstructorDashboard',
  data() {
    return {
      instructor: {
        first_name: '',
        last_name: '',
        email: '',
      },
      instructorId: null, // Separate variable for instructor ID
      courses: [],
    };
  },
  computed: {
    filteredCourses() {
      // Filter courses by instructor ID
      return this.courses.filter(course => course.instructor_id === this.instructorId);
    },
  },
  mounted() {
    const userDetails = JSON.parse(localStorage.getItem('userDetails')); // Parse the stored user details
    this.instructorId = Number(localStorage.getItem('user-id'));// Retrieve the instructor ID

    if (userDetails) {
      this.instructor = { ...userDetails };
      this.fetchCourses(); // Fetch courses after setting instructor details
    }
  },
  methods: {
    fetchCourses() {
      fetch('http://127.0.0.1:8000/courses', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then(response => {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error('Failed to fetch courses');
          }
        })
        .then(data => {
          this.courses = data;
        })
        .catch(error => {
          console.error('Error fetching courses:', error);
        });
    },
    navigateToCreateCourse() {
      this.$router.push('/course/create');
    },
    navigateToCourseDetails(id) {
      this.$router.push({ name: 'course-detail', params: { id: id } });
    },
    navigateToUpdateCourse(id) {
      this.$router.push({ name: 'update-course', params: { id: id } });
    },
    confirmDeleteCourse(id) {
      if (confirm('Are you sure you want to delete this course?')) {
        fetch(`http://127.0.0.1:8000/courses/${id}`, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json',
          },
        })
          .then(response => {
            if (response.ok) {
              this.courses = this.courses.filter(course => course.id !== id);
              alert('Course deleted successfully.');
            } else {
              throw new Error('Failed to delete course');
            }
          })
          .catch(error => {
            console.error('Error deleting course:', error);
          });
      }
    },
    logout() {
      localStorage.removeItem('token');
      this.$router.push('/');
    },
  },
};
</script>


<style scoped>
.instructor-dashboard {
  display: flex;
  flex-direction: column;
  height: 100%; /* ensures it covers full viewport height */
  background-color: #fdf4f4; /* Light maroon background */
  color: white; /* For text inside the component */
  border: none; /* Removes any border */
  margin: 0; /* Removes margin */
  padding: 0; /* Removes padding */
  box-sizing: border-box; /* Includes padding and border in the width and height */
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #a3333d; /* Maroon for header */
  padding: 1rem;
}

button {
  background-color: #c04851; /* Button background */
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #da6868; /* Lighter maroon on hover */
}

main {
  flex-grow: 1;
  display: flex;
  flex-direction: column; /* Aligns child elements vertically */
  align-items: center; /* Center aligns all child elements horizontally */
  overflow-y: auto; /* Allows scrolling inside main if content overflows */
}

.create-course-btn {
  align-self: center; /* Centers the button */
  padding: 10px 15px;
  margin-top: 20px;
}

.courses-list {
  list-style-type: none;
  width: 100%; /* Ensures list uses full width */
  padding: 0;
}

.courses-list li {
  background-color: rgba(176, 1, 1, 0.518); /* Light color for list items */
  padding: 10px;
  font-size: 2rem;
  align-items: center;
  margin-bottom: 10px;
  border-radius: 5px;
  width: 90%; /* Ensures list items do not extend too far */
  margin-left: auto;
  margin-right: auto;
}

.button-group {
  display: flex;
  justify-content: space-around; /* Distributes buttons evenly */
}

header p {
  margin: 0;
  font-size: 1.2rem; /* Adjusts email font size */
}

header button {
  background-color: #c04851; /* Button background */
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  display: block; /* Ensures the button is visible */
}
</style>
