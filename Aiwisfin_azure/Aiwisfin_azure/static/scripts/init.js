(function ($) {
    $(function () {

        $('.button-collapse').sideNav();
        $('.parallax').parallax();

    }); // end of document ready
})(jQuery); // end of jQuery name space

// Or with jQuery

$(document).ready(function () {
    $('.collapsible').collapsible();
});



$('a#question-button').bind('click', function () {
    request();
    submit_form();
});
