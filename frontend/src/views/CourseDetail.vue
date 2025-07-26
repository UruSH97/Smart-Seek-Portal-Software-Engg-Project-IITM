<template>
  <div class="course-detail-container">
    <h1>{{ course.title }}</h1>
    <p>{{ course.description }}</p>

    <div class="actions">
      <button @click="goToAddModule(course.id)">Add New Module</button>
      <button @click="goToAddNotes(course.id)">Add New Notes</button>
      <button @click="goToCourseStatistics">Course Statistics</button>
      <button @click="goToListEnrolledStudents">List of Enrolled Students</button>
      <button @click="goToResourceGeneration">Generate Resources</button>
      <button @click="backToDashboard">Back to Dashboard</button>
    </div>

    <div class="content">
      <div class="modules">
        <h2>Modules</h2>
        <ul>
          <li v-for="module in filteredModules" :key="module.id">
            Weeks- {{ module.week }} - {{ module.title }}
            <button @click="goToModuleDetail(module.id)">View</button>
            <button @click="goToUpdateModule(module.id)">Update</button>
            <button @click="deleteModule(module.id)">Delete</button>
          </li>
        </ul>
      </div>

      <div class="notes">
        <h2>Notes</h2>
        <ul>
          <li v-for="note in filteredNotes" :key="note.id">
            {{ note.title }}
            <button @click="updateNote(note.id)">Update</button>
            <button @click="deleteNote(note.id)">Delete</button>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      course: {
        id: this.$route.params.id,
        title: '',
        description: '',
      },
      allModules: [],
      notes: [],
    };
  },
  computed: {
    filteredModules() {
      return this.allModules.filter(module => module.course_id === this.course.id);
    },
    filteredNotes() {
      return this.notes.filter(note => note.course_id === this.course.id);
    },
  },
  created() {
    this.fetchCourseDetails();
    this.fetchModules();
    this.fetchNotes();
  },
  methods: {
    fetchCourseDetails() {
      fetch(`http://127.0.0.1:8000/courses/${this.course.id}`)
        .then(response => response.json())
        .then(data => {
          this.course.title = data.title;
          this.course.description = data.description;
        })
        .catch(error => alert('Error fetching course details: ' + error.message));
    },
    fetchModules() {
      fetch('http://127.0.0.1:8000/modules')
        .then(response => response.json())
        .then(data => {
          this.allModules = data;
        })
        .catch(error => alert('Error fetching modules: ' + error.message));
    },
    fetchNotes() {
      fetch(`http://127.0.0.1:8000/notes`)
        .then(response => response.json())
        .then(data => {
          this.notes = data;
        })
        .catch(error => alert('Error fetching notes: ' + error.message));
    },
    goToAddModule(id) {
      this.$router.push({ name: 'add-module', params: { courseId: id } });
    },
    goToAddNotes(id) {
      this.$router.push({ name: 'add-notes', params: { courseId: id } });
    },
    goToCourseStatistics() {
      this.$router.push(`/course/${this.course.id}/statistics`);
    },
    goToListEnrolledStudents() {
      this.$router.push(`/course/${this.course.id}/students`);
    },
    goToResourceGeneration() {
      this.$router.push({ name: 'generate-resources', params: { courseId: this.course.id} });
    },
    goToModuleDetail(moduleId) {
      this.$router.push({ name: 'module-detail', params: { courseId: this.course.id,  moduleId: moduleId } });
    },
    goToUpdateModule(moduleId) {
      this.$router.push({ name: 'update-module', params: { courseId: this.course.id,  moduleId: moduleId } });

    },
    deleteModule(moduleId) {
      if (confirm('Are you sure you want to delete this module?')) {
        fetch(`http://127.0.0.1:8000/modules/${moduleId}`, {
          method: 'DELETE'
        }).then(() => {
          this.allModules = this.allModules.filter(module => module.id !== moduleId);
        }).catch(error => alert('Error deleting module: ' + error.message));
      }
    },
    updateNote(noteId) {
      this.$router.push({ name: 'update-notes', params: { courseId: this.course.id, noteId: noteId } });
    },
    deleteNote(noteId) {
      if (confirm('Are you sure you want to delete this note?')) {
        fetch(`http://127.0.0.1:8000/notes/${noteId}`, {
          method: 'DELETE'
        }).then(() => {
          this.notes = this.notes.filter(note => note.id !== noteId);
        }).catch(error => alert('Error deleting note: ' + error.message));
      }
    },
    backToDashboard() {
      this.$router.push('/instructordashboard');
    },
  },
};
</script>

<style scoped>
.course-detail-container {
  width: 100%;
  margin: 20px auto;
  padding: 20px;
  background-color: #f8e8e8;
  color: #300;
  font-family: "Comic Sans MS", cursive, sans-serif;
  text-align: center;
}

.actions button,
.content button {
  margin-right: 10px;
  padding: 8px 16px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
  font-family: "Comic Sans MS", cursive, sans-serif;
}

.actions button {
  background-color: #600;
  color: white;
}

.content {
  display: flex;
  justify-content: space-between;
}

.modules,
.notes {
  flex: 1;
  margin-right: 20px;
}

ul {
  list-style: none;
  padding: 0;
}

h1,
h2 {
  color: #600;
  text-align: center;
}
</style>
