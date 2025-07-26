<template>
    <div class="add-notes-container">
      <h1>Add New Note</h1>
      <form @submit.prevent="saveNote">
        <div class="form-group">
          <label for="noteTitle">Note Title</label>
          <input type="text" id="noteTitle" v-model="note.title" required>
        </div>
        <div class="form-group">
          <label for="pdflink">PDF Link</label>
          <input type="text" id="pdflink" v-model="note.pdflink" required>
        </div>
        <div class="form-group">
          <label for="noteContent">Content</label>
          <textarea id="noteContent" v-model="note.content" required></textarea>
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
        note: {
          title: '',
          pdflink: '',
          content: '',
          course_id: this.$route.params.courseId
        }
      };
    },
    methods: {
      saveNote() {
        fetch(`http://127.0.0.1:8000/notes`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ ...this.note})
        })
        .then(response => {
          if (response.ok) {
            this.$router.push(`/course/${this.$route.params.courseId}`);
          } else {
            throw new Error('Failed to save the note');
          }
        })
        .catch(error => {
          alert(error.message);
        });
      },
      cancel() {
        const courseId = this.$route.params.courseId;
        this.$router.push(`/course/${courseId}/notes`);
      }
    }
  }
  </script>
  
  <style scoped>
  .add-notes-container {
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
  
  input[type="text"],
  input[type="url"],
  textarea {
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
  