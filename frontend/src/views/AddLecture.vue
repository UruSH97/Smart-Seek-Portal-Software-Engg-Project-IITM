<template>
    <div class="add-lecture-page">
      <header>
        <h1 class="center-text">Add New Lecture</h1>
      </header>
      <form @submit.prevent="saveLecture">
        <div class="form-group">
          <label for="title">Lecture Title:</label>
          <input id="title" v-model="lecture.title" type="text" required>
        </div>
        <div class="form-group">
          <label for="content">Content:</label>
          <textarea id="content" v-model="lecture.content" rows="5" required></textarea>
        </div>
        <div class="actions">
          <button type="submit" class="save-btn">Save</button>
          <button type="button" @click="cancel">Cancel</button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AddLecture',
    data() {
      return {
        lecture: {
          module_id: this.$route.params.moduleId,
          title: '',
          content: ''
        }
      };
    },
    methods: {
      saveLecture() {
        fetch('http://127.0.0.1:8000/lectures', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.lecture)
        })
        .then(response => response.json())
        .then(() => {
          this.$router.push({ name: 'module-detail', params: { moduleId: this.lecture.moduleId } });
        })
        .catch(error => {
          console.error('Error adding the lecture:', error);
        });
      },
      cancel() {
        this.$router.push({ name: 'module-detail', params: { moduleId: this.lecture.moduleId } });
      }
    }
  }
  </script>
  
  <style scoped>
  .add-lecture-page {
    font-family: 'Comic Sans MS', cursive;
    color: #800000; /* light maroon */
    max-width: 600px;
    margin: 20px auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
  }
  
  .center-text {
    text-align: center;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 5px;
  }
  
  .form-group input, .form-group textarea {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
  }
  
  .actions {
    text-align: right;
  }
  
  .save-btn {
    background-color: #ffdddd; /* light pink */
    color: #800000;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .save-btn:hover {
    background-color: #ffcccc;
  }
  
  button {
    margin-left: 10px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    background-color: #f0f0f0;
    border: none;
  }
  
  button:hover {
    background-color: #e0e0e0;
  }
  </style>
  