<template>
  <div class="module-detail-page">
    <header>
      <h1 class="center-text">{{ module.week }} - {{ module.title }}</h1>
    </header>
    <div class="center-text actions">
      <button @click="goToAddNewLecture">Add New Lecture</button>
      <button @click="goToAddProgrammingAssignment">Add New Programming Assignment</button>
      <button @click="goToAddNonProgrammingAssignment">Add New Non-Programming Assignment</button>
      <button @click="generateNewQuestion">Generate New Question</button>
    </div>
    <div class="grid-container">
      <section class="lectures">
        <h2>Lectures</h2>
        <ul>
          <li v-for="lecture in lectures" :key="lecture.id">
            {{ lecture.title }}
            <button @click="updateLecture(lecture.id)">Update</button>
            <button @click="deleteLecture(lecture.id)">Delete</button>
          </li>
        </ul>
      </section>
      <section class="programming-assignments">
        <h2>Programming Assignments</h2>
        <ul>
          <li v-for="assignment in programmingAssignments" :key="assignment.id">
            {{ assignment.title }}
            <button @click="updateProgrammingAssignment(assignment.id)">Update</button>
            <button @click="deleteAssignment(assignment.id)">Delete</button>
          </li>
        </ul>
      </section>
      <section class="non-programming-assignments">
        <h2>Non-Programming Assignments</h2>
        <ul>
          <li v-for="question in questions" :key="question.id">
            {{ question.question_text }}
            <button @click="updateQuestion(question.id)">Update</button>
            <button @click="deleteQuestion(question.id)">Delete</button>
          </li>
        </ul>
      </section>
    </div>
    <footer class="center-text">
      <button @click="goToCourseDetail">Back to Course Detail</button>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'ModuleDetail',
  data() {
    return {
      module: {},
      lectures: [],
      programmingAssignments: [],
      questions: [] // Now using questions for non-programming assignments
    };
  },
  methods: {
    fetchModuleDetails() {
      fetch(`http://127.0.0.1:8000/modules/${this.$route.params.moduleId}`)
        .then(response => response.json())
        .then(data => {
          this.module = data;
          this.fetchLectures();
          this.fetchProgrammingAssignments();
          this.fetchQuestions();
        })
        .catch(error => console.error('Error fetching module details:', error));
    },
    fetchLectures() {
      fetch(`http://127.0.0.1:8000/lectures`)
        .then(response => response.json())
        .then(data => this.lectures = data)
        .catch(error => console.error('Error fetching lectures:', error));
    },
    fetchProgrammingAssignments() {
      fetch(`http://127.0.0.1:8000/programming_assignments`)
        .then(response => response.json())
        .then(data => this.programmingAssignments = data)
        .catch(error => console.error('Error fetching programming assignments:', error));
    },
    fetchQuestions() {
      fetch(`http://127.0.0.1:8000/questions/`)
        .then(response => response.json())
        .then(data => this.questions = data)
        .catch(error => console.error('Error fetching questions:', error));
    },
    goToAddNewLecture() {
      this.$router.push({ name: 'add-lecture', params: { moduleId: this.module.id } });
    },
    goToAddProgrammingAssignment() {
      this.$router.push({ name: 'add-programming-assignment', params: { moduleId: this.module.id } });
    },
    goToAddNonProgrammingAssignment() {
      this.$router.push({ name: 'add-non-programming-assignment', params: { moduleId: this.module.id } });
    },
    generateNewQuestion() {
      this.$router.push({ name: 'generate-questions', params: { courseId: this.module.course_id } });
    },
    updateLecture(lectureId) {
      this.$router.push({ name: 'update-lecture', params: { lectureId: lectureId } });
    },
    deleteLecture(lectureId) {
      fetch(`http://127.0.0.1:8000/lectures/${lectureId}`, { method: 'DELETE' })
        .then(() => this.fetchLectures())
        .catch(error => console.error('Error deleting the lecture:', error));
    },
    updateProgrammingAssignment(assignmentId) {
      this.$router.push({ name: 'update-programming-assignment', params: { assignmentId: assignmentId } });
    },
    deleteAssignment(assignmentId) {
      fetch(`http://127.0.0.1:8000/programming_assignments/${assignmentId}`, { method: 'DELETE' })
        .then(() => this.fetchProgrammingAssignments())
        .catch(error => console.error('Error deleting the assignment:', error));
    },
    updateQuestion(questionId) {
      this.$router.push({ name: 'update-question', params: { questionId: questionId } });
    },
    deleteQuestion(questionId) {
      fetch(`http://127.0.0.1:8000/questions/${questionId}`, { method: 'DELETE' })
        .then(() => this.fetchQuestions())
        .catch(error => console.error('Error deleting the question:', error));
    },
    goToCourseDetail() {
      this.$router.push({ name: 'course-detail', params: { id: this.module.course_id } });
    }
  },
  created() {
    this.fetchModuleDetails();
  }
}
</script>

<style scoped>
.module-detail-page {
  font-family: 'Comic Sans MS', cursive;
  color: #800000; /* light maroon */
  text-align: center;
}

.center-text {
  text-align: center;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

button {
  background-color: #ffdddd; /* light pink for contrast */
  border: none;
  padding: 8px;
  margin: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #ffcccc;
}
</style>
