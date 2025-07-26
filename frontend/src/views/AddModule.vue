<template>
    <div class="add-module-container">
      <h1>Add New Module</h1>
      <form @submit.prevent="saveModule">
        <div class="form-group">
          <label for="moduleTitle">Module Title</label>
          <input type="text" id="moduleTitle" v-model="module.title" required>
        </div>
        <div class="form-group">
          <label for="moduleDescription">Module Description</label>
          <textarea id="moduleDescription" v-model="module.description" required></textarea>
        </div>
        <div class="form-group">
          <label for="moduleWeek">Week</label>
          <input type="number" id="moduleWeek" v-model.number="module.week" required min="1">
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
        module: {
          title: '',
          description: '',
          week: 1,
          courseId: this.$route.params.courseId
        }
      };
    },
    methods: {
      saveModule() {
        fetch(`http://127.0.0.1:8000/modules`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            course_id: this.module.courseId,
            title: this.module.title,
            description: this.module.description,
            week: this.module.week
          })
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('Failed to create module');
          }
          alert('Module added successfully!');
          this.$router.push(`/course/${this.module.courseId}`);
        })
        .catch(error => {
          alert('Error adding module: ' + error.message);
        });
      },
      cancel() {
        this.$router.push(`/course/${this.module.courseId}`);
      }
    }
  }
  </script>
  
  <style scoped>
  .add-module-container {
    max-width: 500px;
    margin: 20px auto;
    padding: 20px;
    background-color: #f8e8e8;
    color: #300;
    font-family: 'Comic Sans MS', cursive, sans-serif;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input[type="text"], input[type="number"], textarea {
    width: 100%;
    padding: 8px;
    border: 1px solid #300;
    border-radius: 4px;
  }
  
  textarea {
    height: 100px;
  }
  
  button {
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-right: 10px;
  }
  
  .btn-save {
    background-color: #600;
    color: white;
  }
  
  .btn-cancel {
    background-color: #ccc;
    color: #333;
  }
  </style>
  