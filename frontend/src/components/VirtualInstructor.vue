<template>
    <div class="row m-4">
        <div class="mb-2">
            <InputText v-model="query" type="text" placeholder="Ask your question here" style="width: 100%" />
            <Button label="Ask" @click="askQuery" />
        </div>
        <div class="card">
            <Accordion :value="['0']" multiple>
                <AccordionPanel :value="query.id" v-for="query in myQueries" :key="query.id">
                    <AccordionHeader>{{ query.gen_query }}</AccordionHeader>
                    <AccordionContent>
                        <p class="m-0">
                            <div v-html="formatMarkdown(query.response)"></div>
                        </p>
                    </AccordionContent>
                </AccordionPanel>
            </Accordion>
        </div>
    </div>
</template>

<script>

import Accordion from 'primevue/accordion';
import AccordionPanel from 'primevue/accordionpanel';
import AccordionHeader from 'primevue/accordionheader';
import AccordionContent from 'primevue/accordioncontent';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import axios from 'axios';
import MarkdownIt from 'markdown-it'; 



export default {
    components: {
        Accordion,
        AccordionPanel,
        AccordionHeader,
        AccordionContent,
        InputText,
        Button
    },
    data() {
        return {
            query: '',
            myQueries: [],
            md: new MarkdownIt()
        }
    },
    methods: {
        async fetchQueries() {
            try {
                const questionResponse = await fetch(`http://127.0.0.1:8000/api/virtual_instructor_query/${localStorage.getItem('course_id')}/${localStorage.getItem('user_id')}`);
                this.myQueries = await questionResponse.json();
            } catch (error) {
                console.error("Failed to fetch question", error);
            }
        },
        async askQuery() {
            const response = await axios.post('http://127.0.0.1:8000/api/virtual_instructor_query', {
                gen_query: this.query,
                course_id: localStorage.getItem('course_id'),
                student_id: localStorage.getItem('user_id'),
            }, {
                headers: {
                    'Content-Type': 'application/json',
                }
            });

            // console.log('POST request response:', response.data);

            if (response.data.success === false) {
                alert(response.data.error);
            } else {
                location.reload();
            }

        },
        formatMarkdown(text) {
        return this.md.render(text); 
      }
    },
    mounted() {
        this.fetchQueries();
    },
    computed: {
    markdownText() {
      const html = marked(this.text);
      return DOMPurify.sanitize(html);
    },
  },
}
</script>