$(document).ready(function() {
        $("#testjq").mouseenter(function() {
            $("#testjq").fadeTo("fast", 1);
        });
        $("#testjq").mouseleave(function() {
            $("#testjq").fadeTo("fast", 0.5);
        });
    });