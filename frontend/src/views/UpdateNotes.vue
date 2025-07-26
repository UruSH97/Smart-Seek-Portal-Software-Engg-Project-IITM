<template>
  <div class="update-note-container">
    <h1>Update Note</h1>
    <form @submit.prevent="updateNote">
      <div class="form-group">
        <label for="noteTitle">Note Title</label>
        <input type="text" id="noteTitle" v-model="note.title" required />
      </div>
      <div class="form-group">
        <label for="noteContent">Content</label>
        <textarea id="noteContent" v-model="note.content" required></textarea>
      </div>
      <div class="form-group">
        <label for="notePdfLink">PDF Link</label>
        <input type="text" id="notePdfLink" v-model="note.pdflink" />
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
        id: this.$route.params.noteId,
        course_id: this.$route.params.courseId,
        title: "",
        content: "",
        pdflink: "",
      },
    };
  },
  created() {
    this.fetchNoteDetails();
  },
  methods: {
    fetchNoteDetails() {
      fetch(`http://127.0.0.1:8000/notes/${this.note.id}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          this.note.title = data.title;
          this.note.content = data.content;
          this.note.pdflink = data.pdflink || "";
        })
        .catch((error) => console.error("Error:", error));
    },
    updateNote() {
      fetch(`http://127.0.0.1:8000/notes/${this.note.id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.note),
      })
        .then((response) => {
          if (response.ok) {
            this.$router.push(`/course/${this.$route.params.courseId}`);
          } else {
            throw new Error("Failed to update note");
          }
        })
        .catch((error) => {
          alert(error.message);
        });
    },
    cancel() {
      this.$router.push(`/course/${this.$route.params.courseId}`);
    },
  },
};
</script>

<style scoped>
.update-note-container {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  background-color: #f8e8e8;
  color: #600;
  text-align: center;
  font-family: "Comic Sans MS", cursive, sans-serif;
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
  font-family: "Comic Sans MS", cursive, sans-serif;
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
