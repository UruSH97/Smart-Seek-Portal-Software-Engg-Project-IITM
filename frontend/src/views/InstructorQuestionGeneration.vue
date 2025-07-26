<template>
    <div class="question-generation-container">
      <h1 class="header">Generate Instructor Questions</h1>
      <div class="chat-container">
        <div class="messages">
          <div v-for="message in messages" :key="message.id" class="message">
            <div :class="{ 'system': message.sender === 'system' }">
                {{ message.query }}
                <div v-html="formatMarkdown(message.text)"></div></div>
            <button @click="deleteQuestion(message.id)">Delete</button>
          </div>
        </div>
        <form @submit.prevent="generateQuestion" class="input-form">
          <input v-model="newQuestion" placeholder="Enter topic for new question" required>
          <select v-model="difficultyLevel">
            <option value="easy">Easy</option>
            <option value="medium">Medium</option>
            <option value="hard">Hard</option>
          </select>
          <button type="submit">Generate</button>
        </form>
      </div>
      <button @click="backToCourseDetail">Back to Course Detail</button>
    </div>
  </template>
  
  <script>
    import MarkdownIt from 'markdown-it'; // Import marked library
  
  export default {
    data() {
      return {
        messages: [],
        newQuestion: '',
          difficultyLevel: 'medium',
          md: new MarkdownIt()
      };
    },
    created() {
      this.fetchExistingQuestions();
    },
    methods: {
      fetchExistingQuestions() {
        const instructorId = localStorage.getItem('user-id');
            const courseId = this.$route.params.courseId;
            const content_type = 'question';
        const apiUrl = `http://127.0.0.1:8000/instructor_content/${instructorId}/${courseId}/${content_type}`;
  
        fetch(apiUrl)
          .then(response => response.json())
          .then(data => {
              this.messages = data.map(item => ({
                query: `Query: ${item.gen_query_text}- Difficulty: ${item.difficulty_level}`,
              text: `Question: ${item.gen_ai_questions}, Answer: ${item.gen_ai_answers}, Detail: ${item.gen_ai_question_detail}`,
              sender: 'system',
              id: item.id
            }));
          })
          .catch(error => {
            console.error('Failed to fetch questions:', error);
          });
      },
      generateQuestion() {
        const instructorId = localStorage.getItem('user-id');
        const courseId = this.$route.params.courseId;
        const apiUrl = `http://127.0.0.1:8000/instructor_content`;
        const postData = {
          instructor_id: instructorId,
          course_id: courseId,
          gen_query_text: this.newQuestion,
          content_type: 'question',
          difficulty_level: this.difficultyLevel
        };
  
        fetch(apiUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(postData)
        })
          .then(response => response.json())
          .then(data => {
              this.messages.push({
                query: `Query: ${data.gen_query_text}- Difficulty: ${data.difficulty_level}`,
              text: `Generated Question: ${data.gen_ai_questions}, Answer: ${data.gen_ai_answers}, Detail: ${data.gen_ai_question_detail}`,
              sender: 'system',
              id: data.id
            });
          })
          .catch(error => {
            console.error('Error:', error);
            this.messages.push({ text: `Failed to generate content: ${error.message}`, sender: 'system' });
          });
      },
      deleteQuestion(id) {
        const apiUrl = `http://127.0.0.1:8000/instructor_content/${id}`;
        fetch(apiUrl, { method: 'DELETE' })
          .then(() => {
            this.messages = this.messages.filter(message => message.id !== id);
          });
      },
      backToCourseDetail() {
        this.$router.push({ name: 'course-detail', params: { id: this.$route.params.courseId } });
      },
      formatMarkdown(text) {
        return this.md.render(text); 
      }
    }
  };
  </script>
  
  <style scoped>
  .question-generation-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background-color: #f8e8e8;
    color: #300;
    font-family: "Comic Sans MS", cursive, sans-serif;
  }
  
  .header {
    text-align: center;
  }
  
  .chat-container {
    width: 100%;
    background-color: #fff;
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 20px;
  }
  
  .messages {
    max-height: 300px;
    overflow-y: auto;
  }
  
  .message {
    margin: 5px;
    padding: 10px;
    background-color: #e8e8e8;
  }
  
  .system {
    background-color: #d8d8d8;
  }
  
  .input-form {
    display: flex;
    margin-top: 10px;
  }
  
  input, select, button {
    padding: 8px;
    margin-right: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    background-color: #600;
    color: white;
    border: none;
    cursor: pointer;
  }
  </style>
  