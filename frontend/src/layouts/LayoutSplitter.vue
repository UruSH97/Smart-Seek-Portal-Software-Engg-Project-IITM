<template>
    <div class="card text-center">
        <div class="card-header">
            Python3
        </div>
        <div class="card-body">
            <v-ace-editor v-model:value="content" @init="editorInit" lang="python" theme="chrome" class="h-screen" />
        </div>
        <div class="card-footer d-flex justify-content-between">
            <div class="col">
                <Button label="run" @click="run" />
            </div>
            <div class="col">
                <Button label="submit" severity="secondary" />
            </div>
        </div>
    </div>
</template>

<script>
import Button from 'primevue/button';


export default {
    name: 'LayoutSplitter',
    data() {
        return {
            content: '',
            programmingAssignment: null,
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
    components: {
        Button
    },
    methods: {
        run() {
            console.log(this.content);
            alert(this.content);
        }
    }
}

</script>

<style scoped>
.h-screen {
    height: 70vh;
}
</style>