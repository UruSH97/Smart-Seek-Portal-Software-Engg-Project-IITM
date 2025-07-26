<template>
    <div class="update-module-container">
      <h1>Update Module</h1>
      <form @submit.prevent="updateModule">
        <div class="form-group">
          <label for="moduleTitle">Module Title</label>
          <input type="text" id="moduleTitle" v-model="module.title" required>
        </div>
        <div class="form-group">
          <label for="moduleDescription">Description</label>
          <textarea id="moduleDescription" v-model="module.description" required></textarea>
        </div>
        <div class="form-group">
          <label for="moduleWeek">Week</label>
          <input type="number" id="moduleWeek" v-model.number="module.week" required>
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
          id: this.$route.params.moduleId,
          title: '',
          description: '',
          week: ''
        }
      };
    },
    created() {
      this.fetchModuleDetails();
    },
    methods: {
      fetchModuleDetails() {
        fetch(`http://127.0.0.1:8000/modules/${this.module.id}`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(response => response.json())
        .then(data => {
          this.module.title = data.title;
          this.module.description = data.description;
          this.module.week = data.week;
        })
        .catch(error => console.error('Error:', error));
      },
      updateModule() {
        fetch(`http://127.0.0.1:8000/modules/${this.module.id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.module)
        })
        .then(response => {
          if (response.ok) {
            this.$router.push(`/course/${this.$route.params.courseId}`);
          } else {
            throw new Error('Failed to update module');
          }
        })
        .catch(error => {
          alert(error.message);
        });
      },
      cancel() {
        this.$router.push(`/course/${this.$route.params.courseId}`);
      }
    }
  }
  </script>
  
  <style scoped>
  .update-module-container {
    max-width: 600px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f8e8e8;
    color: #600;
    text-align: center;
    font-family: 'Comic Sans MS', cursive, sans-serif;
    border-radius: 8px;
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
    border: 1px solid #d3d3d3;
    border-radius: 4px;
  }
  
  button {
    padding: 10px 20px;
    margin-top: 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-family: 'Comic Sans MS', cursive, sans-serif;
  }
  
  .btn-save {
    background-color: #800020; /* Maroon */
    color: white;
  }
  
  .btn-cancel {
    background-color: #ccc;
    margin-left: 10px;
  }
  </style>
  