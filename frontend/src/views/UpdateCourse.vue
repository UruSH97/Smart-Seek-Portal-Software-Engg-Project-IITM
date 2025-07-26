<template>
  <div class="course-container">
    <h1>Update Course</h1>
    <form @submit.prevent="updateCourse">
      <div class="form-group">
        <label for="courseTitle">Course Title</label>
        <input type="text" id="courseTitle" v-model="course.title" required />
      </div>
      <div class="form-group">
        <label for="courseDescription">Description</label>
        <textarea
          id="courseDescription"
          v-model="course.description"
          required></textarea>
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
        id: this.$route.params.id, // assuming the courseId is passed via route params
        title: '',
        description: ''
      }
    };
  },
  created() {
    this.fetchCourseDetails();
  },
  methods: {
      fetchCourseDetails() {
        console.log(this.course.id)
          fetch(`http://127.0.0.1:8000/courses/${this.course.id}`,
          {
            method: 'GET',
            headers: {
          'Content-Type': 'application/json',
        }
          }
      )
        .then(response => response.json())
        .then(data => {
          this.course.title = data.title;
          this.course.description = data.description;
        })
        .catch(error => {
          alert('Error fetching course details: ' + error.message);
        });
    },
    updateCourse() {
      fetch(`http://127.0.0.1:8000/courses/${this.course.id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: this.course.title,
          description: this.course.description
        })
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to update course');
        }
        this.$router.push('/instructordashboard'); // Redirect after update
      })
      .catch(error => {
        alert('Error updating course: ' + error.message);
      });
    },
    cancel() {
      this.$router.push('/instructordashboard'); // Return to dashboard without saving
    }
  }
}
</script>

<style scoped>
.course-container {
  padding: 20px;
  background-color: #f8e8e8; /* Light maroon theme */
  color: #300;
  font-family: "Comic Sans MS", cursive, sans-serif;
  max-width: 600px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 10px;
  font-size: 16px;
}

input[type="text"],
textarea {
  width: 100%;
  padding: 10px;
  border: 2px solid #300;
  border-radius: 5px;
  font-size: 14px;
}

textarea {
  height: 100px;
}

button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 10px;
}

.btn-save {
  background-color: #600;
  color: #fff;
  margin-right: 20px;
}

.btn-cancel {
  background-color: #ccc;
  color: #333;
}
</style>
