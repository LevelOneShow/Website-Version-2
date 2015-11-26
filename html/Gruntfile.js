module.exports = function(grunt){

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        clean: {
            dist: ['bower_components/*/*', '!bower_components/*/dist'],
            font: ['bower_components/materialize/dist/font/'],
            mincss: ['bower_components/materialize/dist/css/*.css', '!bower_components/materialize/dist/css/*.min.css'],
            minjs: ['bower_components/materialize/dist/js/*.js', '!bower_components/materialize/dist/js/*.min.js'],
            minq: ['bower_components/jquery/dist/*.js', '!bower_components/jquery/dist/*.min.js']
        }
    });

    // Install modules
    grunt.loadNpmTasks('grunt-contrib-clean'); // clean unused directories.

    // Register Tasks
    grunt.registerTask('default', ['clean']);

};
