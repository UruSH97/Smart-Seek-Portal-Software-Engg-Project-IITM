<script >
import NavBar from './NavBar.vue';
import SideBar from './SideBar.vue';
import QuestionsList from '../layouts/QuestionsList.vue';
import LayoutSplitter from '../layouts/LayoutSplitter.vue';
export default {
    components: {
        NavBar,
        SideBar,
        QuestionsList,
        LayoutSplitter
    },
    data() {
        return {
            assignmentId: null
        }
    },
    methods: {
        assignmentChanged(assginId) {
            this.assignmentId = assginId
        }
    }
}
</script>

<template>
    <!-- main content -->
    <div class="row">
        <!-- sidebar -->
        <!-- scrollable sidebar  -->
        <div class="col-2 mt-1">
            <SideBar @assignment-changed="assignmentChanged" />
        </div>
        <!-- lecturs or assignments section  -->
        <div class="col-5 mt-1">
            <QuestionsList :assgnId="assignmentId"/>
        </div>
        <div class="col-5 mt-1">
            <LayoutSplitter :assgnId="assignmentId" />
        </div>
    </div>
</template>

<style scoped>
</style>
