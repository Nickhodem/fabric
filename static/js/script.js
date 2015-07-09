$(document).ready(function(){
    $("#przycisk").click(function(){
        var div = $("#port");
        $('#opis').append('<p> Jeżeli Twój poziom zaawansowania jest wyższy  CSS ogłębny opis wszystkich znaczników wraz z bardzo licznymi przykładami ich użycia w praktyce. Zdobędziesz nie tylko wiedzę teoretyczną, ale i praktyczną. Szczególnie </p>')
        div.animate({width: '100%', opacity: '0.8'}, "fast");
        div.animate({height: '100%', opacity: '0.4'}, "fast");
    });
});






$(document).ready(function(){
    $("#square").click(function(){
        $("#kaf1").height("15vw");
        $("#kaf1").width("15vw");
        $("#hobbyopis1, #square").hide();
        $("#kaf2, #kaf4, #kaf3").show();

    });
});


$(document).ready(function() {
    $("#hobbyopis1, #square").hide();
});



$(document).ready(function(){
    $("#kaf1").click(function(){
        var div = $(this);
        $("#kaf2, #kaf3, #kaf4").hide();
        /*div.animate({right: '-10vw'}, "fast");*/
        div.animate({width: '80vw'}, "slow");
        $("#hobbyopis1, #square").show();
        div.animate({height: "700%"}, "slow");
    });
});














$(document).ready(function(){
    $("#square").click(function(){
        var div = $("#kaf2");
        div.height("100%");
        div.width("15vw");
        div.css("margin-left","0px");
        div.css("height","15vw")
        $("#hobbyopis2, #square").hide();
        $("#kaf1, #kaf4, #kaf3").show();

    });
});


$(document).ready(function() {
    $("#hobbyopis2, #square").hide();
});



$(document).ready(function(){
    $("#kaf2").click(function(){
        var div = $(this);
        $("#kaf1, #kaf3, #kaf4").hide();
        div.css("margin-left","10vw");
        div.animate({width: '80vw'}, "slow");
        $("#hobbyopis2, #square").show();
        div.animate({height: "700%"}, "slow");
    });
});







$(document).ready(function(){
    $("#square").click(function(){
        var div = $("#kaf3");
        div.height("15vw");
        div.width("15vw");
        div.css("margin-left","0px");
        $("#hobbyopis3, #square").hide();
        $("#kaf1, #kaf4, #kaf2").show();

    });
});


$(document).ready(function() {
    $("#hobbyopis3, #square").hide();
});



$(document).ready(function(){
    $("#kaf3").click(function(){
        var div = $(this);
        $("#kaf1, #kaf2, #kaf4").hide();
        div.css("margin-left","10vw");
        div.animate({width: '80vw'}, "slow");
        $("#hobbyopis3, #square").show();
        div.animate({height: "700%"}, "slow");
    });
});











$(document).ready(function(){
    $("#square").click(function(){
        var div = $("#kaf4");
        div.height("15vw");
        div.width("15vw");
        div.css("margin-left","0px");
        $("#hobbyopis4, #square").hide();
        $("#kaf1, #kaf3, #kaf2").show();

    });
});


$(document).ready(function() {
    $("#hobbyopis4, #square").hide();
});



$(document).ready(function(){
    $("#kaf4").click(function(){
        var div = $(this);
        $("#kaf1, #kaf2, #kaf3").hide();
        div.css("margin-left","10vw");
        div.animate({width: '80vw'}, "slow");
        $("#hobbyopis4, #square").show();
        div.animate({height: "700%"}, "slow");
    });
});




