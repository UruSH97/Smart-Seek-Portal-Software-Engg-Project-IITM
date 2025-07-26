<template>
    <div class="create-course-container">
      <h1>Create New Course</h1>
      <form @submit.prevent="saveCourse">
        <div class="form-group">
          <label for="courseTitle">Course Title</label>
          <input type="text" id="courseTitle" v-model="course.title" required>
        </div>
        <div class="form-group">
          <label for="courseDescription">Description</label>
          <textarea id="courseDescription" v-model="course.description" required></textarea>
        </div>
        <button type="submit" class="btn-save">Save</button>
        <button type="button" class="btn-cancel" @click="cancel">Cancel</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        course: {
          title: '',
          description: '',
          instructorId: null  // Add this field to store the instructor ID
        }
      };
    },
    mounted() {
      this.course.instructorId = localStorage.getItem('user-id'); // Retrieve instructor ID on component mount
    },
    methods: {
      async saveCourse() {
        try {
          const response = await fetch('http://127.0.0.1:8000/courses', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.course)
          });
          if (!response.ok) {
            throw new Error('Failed to save course');
          }
          this.$router.push('/instructordashboard'); // Redirect to dashboard after save
        } catch (error) {
          alert('Error saving course: ' + error.message);
        }
      },
      cancel() {
        this.$router.push('/instructordashboard'); // Redirect to instructor dashboard without saving
      }
    }
  }
  </script>
  
  <style scoped>
.create-course-container {
  padding: 20px;
  background-color: #f8e8e8; /* Light maroon theme */
  color: #300;
  font-family: 'Comic Sans MS', cursive, sans-serif;
  max-width: 600px; /* Restricts form width for better layout */
  margin: 0 auto; /* Centers the form on the page */
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 10px;
  font-size: 16px; /* Larger font size for better readability */
}

input[type="text"], textarea {
  width: 100%;
  padding: 10px;
  border: 2px solid #300; /* Slightly thicker border for better visual structure */
  border-radius: 5px; /* Rounded corners */
  font-size: 14px; /* Suitable font size for inputs */
}

textarea {
  height: 100px; /* Fixed height for the textarea */
}

button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px; /* Larger font size for buttons */
  margin-top: 10px; /* Spacing above the buttons */
}

.btn-save {
  background-color: #600; /* Darker shade of maroon */
  color: #fff;
  margin-right: 20px; /* Spacing between buttons */
}

.btn-cancel {
  background-color: #ccc;
  color: #333;
}
</style>