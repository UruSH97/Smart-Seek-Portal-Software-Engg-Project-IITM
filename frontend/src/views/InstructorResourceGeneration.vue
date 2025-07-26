<template>
    <div class="resource-generation-container">
      <h1>Generate Instructor Resources</h1>
      <div class="chat-container">
        <div class="messages">
          <div class="message" v-for="(message, index) in messages" :key="index">
            <div :class="`message-content ${message.sender}`" >
                {{ message.query }}
                <div v-html="formatMarkdown(message.text)">
                    </div>
              <button v-if="message.sender === 'system' && message.id" @click="deleteContent(message.id)">Delete</button>
            </div>
          </div>
        </div>
        <form @submit.prevent="submitQuery" class="input-area">
          <input type="text" v-model="genQuery" placeholder="Enter your resource topic..." required>
          <select v-model="difficultyLevel">
            <option value="easy">Easy</option>
            <option value="medium">Medium</option>
            <option value="hard">Hard</option>
          </select>
          <button type="submit">Generate Resource</button>
        </form>
      </div>
      <button @click="backToCourseDetail" class="back-button">Back to Course Detail</button>
    </div>
</template>

<script>
import MarkdownIt from 'markdown-it';

export default {
  data() {
    return {
      genQuery: '',
      difficultyLevel: 'easy',
      messages: [],
      md: new MarkdownIt()
    };
  },
  created() {
    this.fetchPreviousContents();
  },
  methods: {
    fetchPreviousContents() {
      const instructorId = localStorage.getItem('user-id');
      const courseId = this.$route.params.courseId;
      const content_type = 'resource';
      fetch(`http://127.0.0.1:8000/instructor_content/${instructorId}/${courseId}/${content_type}`, {
        method: "GET"
      })
      .then(response => response.json())
      .then(data => {
        data.forEach(content => {
            this.messages.push({
            query: `Query: ${content.gen_query_text}- Difficulty: ${content.difficulty_level}`,
            text: `Resource: ${content.gen_ai_resources}`,
            sender: 'system',
            id: content.id
          });
        });
      });
    },
    submitQuery() {
      const message = {
        text: `Query: ${this.genQuery} - Difficulty: ${this.difficultyLevel}`,
        sender: 'user'
      };
      this.messages.push(message);
      this.generateContent();
    },
    generateContent() {
      const instructorId = localStorage.getItem('user-id');
      const apiUrl = `http://127.0.0.1:8000/instructor_content`;
      const postData = {
        instructor_id: instructorId,
        course_id: this.$route.params.courseId,
        gen_query_text: this.genQuery,
        content_type: 'resource',
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
          text: `Generated Resource: ${data.gen_ai_resources}`,
          sender: 'system',
          id: data.id
        });
      })
      .catch(error => {
        console.error('Error:', error);
        this.messages.push({ text: `Failed to generate content: ${error.message}`, sender: 'system' });
      });
    },
    deleteContent(queryId) {
      fetch(`http://127.0.0.1:8000/instructor_content/${queryId}`, {
        method: 'DELETE'
      })
      .then(() => {
        this.messages = this.messages.filter(message => message.id !== queryId);
        alert('Resource deleted successfully');
      })
      .catch(error => {
        alert('Error deleting resource: ' + error.message);
      });
    },
    backToCourseDetail() {
      this.$router.push(`/course/${this.$route.params.courseId}`);
    },
    formatMarkdown(text) {
      return this.md.render(text);
    }
  }
}
</script>

<style scoped>
.resource-generation-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f8e8e8;
  color: #600;
  text-align: center;
  font-family: 'Comic Sans MS', cursive, sans-serif;
}
.chat-container {
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.messages {
  overflow-y: auto;
  max-height: 400px;
  margin-bottom: 20px;
}
.message-content {
  background-color: #fff;
  padding: 10px;
  border-radius: 10px;
  margin: 5px;
  word-break: break-word;
}
.message-content.system {
  background-color: #ddd;
}
.input-area {
  display: flex;
  justify-content:center;
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background: #f8e8e8;
}
input, select, button {
  padding: 10px;
  margin-right: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
  text-align: center;
}
button {
  background-color: #600;
  color: #fff;
  cursor: pointer;
}
.back-button {
  margin-top: 20px;
}
</style>
