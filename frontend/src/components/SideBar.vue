<template>
    <div class="card">
        <Accordion value="0">
            <AccordionPanel v-for="tab in tabs" :key="tab.id" :value="tab.title">
                <AccordionHeader>{{ tab.title }}</AccordionHeader>
                <AccordionContent>
                    <RadioSelect :module_id="tab.id" @category-changed="passAsginId"></RadioSelect>
                </AccordionContent>
            </AccordionPanel>
        </Accordion>
    </div>
</template>

<script>

import Accordion from 'primevue/accordion';
import AccordionPanel from 'primevue/accordionpanel';
import AccordionHeader from 'primevue/accordionheader';
import AccordionContent from 'primevue/accordioncontent';
import RadioSelect from './RadioSelect.vue';
import axios from 'axios';

export default {
    components: {
        Accordion,
        AccordionPanel,
        AccordionHeader,
        AccordionContent,
        RadioSelect
    },
    data() {
        return {
            tabs: []
        };
    },
    methods: {
        async fetchModules() {
            const response = await axios.get('http://127.0.0.1:8000/api/modules/1', {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('Token')}`
                }
            });
            if (response.data.success === false) {
                alert(response.data.error)
            } else {
                console.log(response.data)
                this.tabs = response.data
                localStorage.setItem('course_id', response.data[0].course_id)
            }

        },
        passAsginId(categoryId) {
            const assginId = categoryId
            this.$emit('assignment-changed', assginId)
        }
    },
    mounted() {
        this.fetchModules();
    }
};
</script>