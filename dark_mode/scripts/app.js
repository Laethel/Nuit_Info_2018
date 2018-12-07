$(document).ready(function() {
    let darkMode = false;

    $('#moon-container').on('click', function() {
        if (darkMode) {
            $('body').removeClass('dark-mode');
            $('body').addClass('white-mode');
            darkMode = false;
        } else {
            $('body').removeClass('white-mode');
            $('body').addClass('dark-mode');
            darkMode = true;
        }
    });

});