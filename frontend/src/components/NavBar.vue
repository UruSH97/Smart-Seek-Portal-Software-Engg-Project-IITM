<template>
    <div>
        <Menubar :model="items">
            <template #start>
                <img width="100" height="40" src="../assets/iitm-logo@3x.png" alt="iitm logo">
                <span class="m-2"> &#124;</span>
                <strong>January 2022: Python
                </strong>
            </template>
            <template #end>
                <div class="gap-2">
                    <span class="me-2"> &#124;</span>
                    <span>21f2000143@ds.study.iitm.ac.in<i class="pi pi-sign-out mx-3"></i></span>
                </div>
            </template>
        </Menubar>
    </div>
</template>

<script>

import InputText from 'primevue/inputtext';
import Menubar from 'primevue/menubar';
import Badge from 'primevue/badge';

export default {
    name: 'NavBar',
    components: {
        InputText,
        Menubar,
        Badge
    },
    data() {
        return {
            items: [
                {
                    label: 'Home',
                    icon: 'pi pi-home',
                    command: () => {
                        this.$router.push('/my-current-courses');
                    }
                },
                {
                    label: 'V-Instructor',
                    icon: 'pi pi-face-smile',
                    command: () => {
                        this.$router.push('/my-current-courses/dashboard/virtual/instructor');
                    }
                }
            ]
        };
    }
};
</script>
