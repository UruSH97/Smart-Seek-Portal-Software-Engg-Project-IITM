import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import('../components/HelloWorld.vue')
        },
        {
            path: '/dashboard',
            name: 'dashboard',
            component: () => import('../views/Dashboard.vue')
        },
        {
            path: '/instructordashboard',
            name: 'instructor-dashboard',
            component: () => import('../views/InstructorDashboard.vue')
        },
        {
            path: '/course/create',
            name: 'create-course',
            component: () => import('../views/CreateCourse.vue')
        },
        {
            path: '/course/update/:id?',
            name: 'update-course',
            component: () => import('../views/UpdateCourse.vue')
        },
        {
            path: '/course/:id?',
            name: 'course-detail',
            component: () => import('../views/CourseDetail.vue')
        },
        {
            path: '/course/:courseId?/module/create',
            name: 'add-module',
            component: () => import('../views/AddModule.vue')
        },
        {
            path: '/course/:courseId?/module/:moduleId?',
            name: 'module-detail',
            component: () => import('../views/ModuleDetail.vue')
        },
        {
            path: '/course/:courseId?/module/:moduleId?/update',
            name: 'update-module',
            component: () => import('../views/UpdateModule.vue')
        },
        {
            path: '/course/:moduleId?/lecture/create',
            name: 'add-lecture',
            component: () => import('../views/AddLecture.vue')
        },
        // {
        //     path: '/course/:courseId/module/:moduleId/lecture/:lectureId',
        //     name: 'view-lecture',
        //     component: () => import('../views/ViewLecture.vue')
        // },
        // {
        //     path: '/course/:courseId/module/:moduleId/lecture/:lectureId/update',
        //     name: 'update-lecture',
        //     component: () => import('../views/UpdateLecture.vue')
        // },
        // {
        //     path: '/course/:courseId/module/:moduleId/programming-assignment/create',
        //     name: 'add-programming-assignment',
        //     component: () => import('../views/AddProgrammingAssignment.vue')
        // },
        // {
        //     path: '/course/:courseId/module/:moduleId/programming-assignment/:assignmentId',
        //     name: 'view-programming-assignment',
        //     component: () => import('../views/ViewProgrammingAssignment.vue')
        // },
        // {
        //     path: '/course/:courseId/module/:moduleId/programming-assignment/:assignmentId/update',
        //     name: 'update-programming-assignment',
        //     component: () => import('../views/UpdateProgrammingAssignment.vue')
        // },
        // {
        //     path: '/course/:courseId/module/:moduleId/non-programming-assignment/create',
        //     name: 'add-non-programming-assignment',
        //     component: () => import('../views/AddNonProgrammingAssignment.vue')
        // },
        // {
        //     path: '/course/:courseId/module/:moduleId/non-programming-assignment/:assignmentId',
        //     name: 'view-non-programming-assignment',
        //     component: () => import('../views/ViewNonProgrammingAssignment.vue')
        // },
        // {
        //     path: '/course/:courseId/module/:moduleId/non-programming-assignment/:assignmentId/update',
        //     name: 'update-non-programming-assignment',
        //     component: () => import('../views/UpdateNonProgrammingAssignment.vue')
        // },
        // {
        //     path: '/course/:courseId/students',
        //     name: 'list-enrolled-students',
        //     component: () => import('../views/ListEnrolledStudents.vue')
        // },
        // {
        //     path: '/course/:courseId/students/:studentId/statistics',
        //     name: 'student-course-statistics',
        //     component: () => import('../views/StudentCourseStatistics.vue')
        // },
        // {
        //     path: '/course/:courseId/statistics',
        //     name: 'course-statistics',
        //     component: () => import('../views/CourseStatistics.vue')
        // },
        {
            path: '/course/:courseId/generate-questions',
            name: 'generate-questions',
            component: () => import('../views/InstructorQuestionGeneration.vue')
        },
        {
            path: '/course/:courseId/generate-resources',
            name: 'generate-resources',
            component: () => import('../views/InstructorResourceGeneration.vue')
        },
        {
            path: '/course/:courseId?/notes/create',
            name: 'add-notes',
            component: () => import('../views/AddNotes.vue')
        },
        {
            path: '/course/:courseId?/:noteId?/update',
            name: 'update-notes',
            component: () => import('../views/UpdateNotes.vue')
        },
        // {
        //     path: '/course/:courseId/module/:moduleId/notes/:noteId/view',
        //     name: 'view-notes',
        //     component: () => import('../views/ViewNotes.vue')
        // }
    ]
});

export default router;
