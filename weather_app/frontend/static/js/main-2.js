(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();

    // timedate
    var timedate = function () {
        setTimeout(function () {
            if ($('#timedate').innerHTML > 0) {
                $('#timedate').addClass('wow slideInLeft');
                $('#timedate').removeClass('hide');
                $('#divider').removeClass('hide');
            }
        }, 1);
    };
    timedate();
    
    
    // Initiate the wowjs
    new WOW().init();

})(jQuery);