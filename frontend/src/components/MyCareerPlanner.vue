<template>
  <div style="font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px;">
    <h1 style="color: #2c3e50;">Plan Your Career</h1>
    <div style="margin-bottom: 20px;">
      <label for="level" style="display: block; margin-bottom: 5px;">Study Level:</label>
      <select id="level" v-model="level" style="width: 100%; padding: 8px; border-radius: 4px; border: 1px solid #ccc;">
        <option value="Beginner">Beginner</option>
        <option value="Intermediate">Intermediate</option>
        <option value="Advanced">Advanced</option>
      </select>
    </div>
    <div style="margin-bottom: 20px;">
      <label for="content_type" style="display: block; margin-bottom: 5px;">Content Type:</label>
      <select id="content_type" v-model="contentType" style="width: 100%; padding: 8px; border-radius: 4px; border: 1px solid #ccc;">
        <option value="Career Advice">Career Advice</option>
        <option value="Study Plan">Study Plan</option>
        <option value="Job Prospects">Job Prospects</option>
      </select>
    </div>
    <div style="margin-bottom: 20px;">
      <label for="query" style="display: block; margin-bottom: 5px;">Your Query:</label>
      <textarea id="query" v-model="query" style="width: 100%; padding: 8px; border-radius: 4px; border: 1px solid #ccc; height: 100px;"></textarea>
    </div>
    <button @click="submitQuery" style="background-color: #3498db; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">
      Get Advice
    </button>

    <div v-if="showResponse" style="position: fixed; top: 0; left: 0; right: 0; bottom: 0; background-color: rgba(0,0,0,0.8); display: flex; justify-content: center; align-items: center; z-index: 1000;">
      <div style="background-color: white; padding: 20px; border-radius: 8px; max-width: 800px; max-height: 80vh; overflow-y: auto; position: relative;">
        <button @click="showResponse = false" style="position: absolute; top: 10px; right: 10px; background: none; border: none; font-size: 20px; cursor: pointer;">&times;</button>
        <h2 style="color: #2c3e50; margin-bottom: 20px;">AI Response</h2>
        <div v-html="formattedResponse" style="line-height: 1.6; font-size: 16px;"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      level: 'Beginner',
      contentType: 'Career Advice',
      query: '',
      response: '',
      showResponse: false,
    };
  },
  computed: {
    formattedResponse() {
      if (!this.response) return '';
      
      let formatted = this.response.replace(/^> /gm, '');
      formatted = formatted.replace(/^###\s+(.*)$/gm, '<h3>$1</h3>');
      formatted = formatted.replace(/^##\s+(.*)$/gm, '<h2>$1</h2>');
      formatted = formatted.replace(/^#\s+(.*)$/gm, '<h1>$1</h1>');
      formatted = formatted.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
      formatted = formatted.replace(/\*(.+?)\*/g, '<em>$1</em>');
      formatted = formatted.replace(/\n/g, '<br>');
      
      return formatted;
    }
  },
  methods: {
    async submitQuery() {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/student-planner`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            student_id: localStorage.getItem('user_id'),
            level: this.level,
            content_type: this.contentType,
            gen_query: this.query,
          }),
        });

        if (response.ok) {
          const data = await response.json();
          this.response = data.response;
          this.showResponse = true;
        } else {
          console.error('Failed to get AI response');
        }
      } catch (error) {
        console.error('Error submitting query:', error);
      }
    }
  },
};
</script>
