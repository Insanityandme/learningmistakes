var gulp = require('gulp')
var postcss = require('gulp-postcss')

gulp.task('css', function() {
    return(
        gulp.src('./mysite/gulp-assets/css/main.css') 
         .pipe(postcss([
            require("postcss-import")(),
            require("postcss-cssnext")(),
            require("cssnano")(),
         ]))
         .pipe(gulp.dest('./mysite/build/css'))
    )
})


gulp.task('watch', function() {
    gulp.watch('./mysite/gulp-assets/css/**/*.css', ['css'])
})
