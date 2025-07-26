<template>
    <!-- Left Card -->
    <div class="card text-center">
        <div class="card-header">
            Due Date:
        </div>
        <div class="card-body">
            <ul class="nav nav-tabs">
                <li class="nav-item">
                    <a class="nav-link active" @click="view = 'question'">Programming Question</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" @click="view = 'testcases'">Test Cases</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" @click="view = 'solution'">Solution</a>
                </li>
            </ul>

            <div v-if="view === 'question' && question">
                <h5>Question ID: {{ question.id }}</h5>
                <p>{{ question.editor_content }}</p>
            </div>

            <div v-if="view === 'testcases' && testCases.length > 0">
                <div v-for="testcase in testCases" :key="testcase.id">
                    <h6>Test Case {{ testcase.id }}</h6>
                    <p><strong>Input:</strong> {{ testcase.input }}</p>
                    <p><strong>Expected Output:</strong> {{ testcase.output }}</p>
                </div>
            </div>

            <div v-if="view === 'solution'">
                <p>Solution will be provided here...</p>
            </div>
        </div>
        <div class="card-footer text-body-secondary">
            2 days ago
        </div>
    </div>
</template>

<script>
export default {
    props: {
        assgnId: String
    },
    data() {
        return {
            question: null,
            testCases: [],
            view: 'question',
            editorContent: '',
            output: null,
            testResults: [],
            passedTestCases: 0,
            totalTestCases: 0,
            selectedLanguage: 'python3'
        }
    },
    methods: {
        async runCode() {
            try {
                const response = await fetch(`/api/submissions/compile`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        content: this.editorContent,
                        programming_assignment_id: this.programmingAssignment.id,
                        student_id: 1, // Replace with actual student ID
                    })
                });
                this.output = await response.json();
                this.testResults = this.output.test_results;
                this.passedTestCases = this.output.passed_test_cases;
                this.totalTestCases = this.output.total_test_cases;
            } catch (error) {
                console.error("Failed to run code", error);
                alert('Failed to run code.');
            }
        },
        async submitCode() {
            try {
                const response = await fetch(`/api/submissions`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        content: this.editorContent,
                        programming_assignment_id: this.programmingAssignment.id,
                        student_id: 1, // Replace with actual student ID
                    })
                });
                const data = await response.json();
                alert(data['feedback']);
            } catch (error) {
                console.error("Failed to submit code", error);
                alert('Failed to save submission.');
            }
        }
    },
    watch: {
        assgnId: {
            handler: async function (newValue, oldValue) {
                try {
                    const questionResponse = await fetch(`http://127.0.0.1:8000/api/programming_assignments/${newValue}`);
                    this.question = await questionResponse.json();
                } catch (error) {
                    console.error("Failed to fetch question", error);
                }

                // Fetch test cases
                if (this.question) {
                    try {
                        const testCasesResponse = await fetch(`http://127.0.0.1:8000/api/test_cases/${this.question.id}`);
                        this.testCases = await testCasesResponse.json();
                    } catch (error) {
                        console.error("Failed to fetch test cases", error);
                    }
                }
            },
            immediate: true
        }
    }
}
</script>

<style></style>