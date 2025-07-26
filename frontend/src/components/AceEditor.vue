<script>
export default {
    name: "AceEditor",
    mounted() {
        var editor = ace.edit("editor");
        editor.setTheme("ace/theme/twilight");
        editor.session.setMode("ace/mode/python");
        editor.setOptions({
            autoScrollEditorIntoView: true,
            copyWithEmptySelection: true,
        });
        editor.resize();
        editor.setHighlightActiveLine(false);
    },
    methods: {
        submit() {
            console.log(editor.getValue());
        }
    }
}

</script>

<template>
    <div id="editor"></div>
</template>

<style scoped>
#editor {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
}
</style>