<template>
    <div class="card flex justify-center">
        <div class="flex flex-col gap-4">
            <div v-for="category in categories" :key="category.id" class="flex items-center">
                <RadioButton v-model="selectedCategory" :inputId="category.title" name="dynamic"
                    :value="category.title" />
                <label :for="category.key" class="ml-2">{{ category.title }}</label>
            </div>
        </div>
    </div>
</template>

<script>

import RadioButton from 'primevue/radiobutton';
import axios from 'axios';

export default {
    components: {
        RadioButton
    },
    props: {
        module_id: String
    },
    data() {
        return {
            selectedCategory: 'PPA 1 - Not Graded',
            categories: []
        }
    },
    methods: {
        async fetchAssignments() {
            const response = await axios.get('http://127.0.0.1:8000/api/assignments/' + this.module_id, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('Token')}`
                }
            });
            if (response.data.success === false) {
                alert(response.data.error)
            } else {
                console.log(response.data)
                this.categories = response.data
            }

        }
    },
    watch: {
        selectedCategory(newValue) {
            const categoryId = this.categories.find(category => category.title === newValue).id;
            this.$emit('category-changed', categoryId);
        }
    },
    mounted() {
        this.fetchAssignments();
    }
};
</script>