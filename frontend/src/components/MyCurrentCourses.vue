<template>
    <div style="font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px;">
        <h1 style="color: #2c3e50; margin: 0;">My Current Courses</h1>
        <div>
          <router-link to="/my-current-courses/career-planner" class="career-button">
            <i class="fas fa-briefcase" style="margin-right: 5px;"></i> Plan Your Career
          </router-link>
        </div>
        <div style="font-size: 1.1em; color: #555; text-align: right;">
          <div>{{ currentDate }}</div>
          <div style="font-weight: bold; margin-top: 5px;">{{ currentTerm }} Term</div>
        </div>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px;">
        <div
          v-for="course in courses"
          :key="course.id"
          style="border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); transition: transform 0.3s ease;"
        >
          <div style="background-color: #ff4444; color: white; padding: 15px; font-size: 1.3em; font-weight: bold;">
            {{ course.title }}
          </div>
          <div style="background-color: white; padding: 15px;">
            <div style="margin-bottom: 15px;">
              <p style="margin: 5px 0; color: #555;">Week 1 Assignment: 98</p>
              <p style="margin: 5px 0; color: #555;">Week 1 Programming Assignment 1: 84</p>
              <p style="margin: 5px 0; color: #555;">Quiz 1: 76</p>
            </div>
            <Button label="Go to course page" @click="$router.push(`/my-current-courses/dashboard`)" />
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import Button from 'primevue/button';
  export default {
    components: {
      Button
    },
    data() {
      return {
        courses: [],
        currentDate: '',
        currentTerm: ''
      };
    },
  
    created() {
      this.fetchCourses();
      this.setDateAndTerm();
    },
  
    methods: {
      async fetchCourses() {
        try {
          const response = await fetch(`http://127.0.0.1:8000/api/enrollments/${localStorage.getItem('user_id')}`);
          if (response.ok) {
            const data = await response.json();
            this.courses = Array.isArray(data) ? data : [data];
          } else {
            console.error('Failed to fetch courses');
          }
        } catch (error) {
          console.error('Error fetching courses:', error);
        }
      },
  
      getCurrentUserId() {
        // Implement this method to return the current user's ID
        return '1'; // Placeholder
      },
  
      setDateAndTerm() {
        const now = new Date();
        this.currentDate = now.toLocaleDateString('en-US', {
          year: 'numeric',
          month: 'long',
          day: 'numeric',
        });
  
        const month = now.getMonth();
        if (month >= 0 && month <= 4) {
          this.currentTerm = 'JANUARY 2024';
        } else if (month >= 5 && month <= 8) {
          this.currentTerm = 'MAY 2024';
        } else {
          this.currentTerm = 'SEPTEMBER 2024';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .career-button {
    display: inline-block;
    padding: 12px 24px;
    background-color: #ff4444;
    color: white;
    text-decoration: none;
    border-radius: 30px;
    font-weight: bold;
    font-size: 16px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(255, 68, 68, 0.3);
    border: 2px solid #ff4444;
  }
  
  .career-button:hover {
    background-color: #ff6666;
    transform: translateY(-2px);
    box-shadow: 0 6px 8px rgba(255, 68, 68, 0.4);
  }
  
  .career-button:active {
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(255, 68, 68, 0.2);
  }
  </style>
  