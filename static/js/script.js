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
        $("#kaf1").css("background-image","none");

    });
});


$(document).ready(function() {
    $("#hobbyopis1, #square").hide();
});



$(document).ready(function(){
    $("#kaf1, #narty").click(function(){
        var div = $("#kaf1");
        $("#kaf2, #kaf3, #kaf4").hide();
        /*div.animate({right: '-10vw'}, "fast");*/
        div.animate({width: '80vw'}, "slow");
        $("#hobbyopis1, #square").show();
        div.animate({height: "700%"}, "slow");
        div.css("background-image", "url('https://lh3.googleusercontent.com/-ljSpSKrgJK4/URjxaynkJzI/AAAAAAAAF28/0Qe68qWNkRA/s640-Ic42/06022013098.jpg')");
        div.css("background-size", "80vw");
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
        $("#kaf2").css("background-image","none");

    });
});


$(document).ready(function() {
    $("#hobbyopis2, #square").hide();
});



$(document).ready(function(){
    $("#kaf2, #rower").click(function(){
        var div = $("#kaf2");
        $("#kaf1, #kaf3, #kaf4").hide();
        div.css("margin-left","10vw");
        div.animate({width: '80vw'}, "slow");
        $("#hobbyopis2, #square").show();
        div.animate({height: "700%"}, "slow");
        div.css("background-image", "url('http://www.visitnorway.com/ImageVaultFiles/id_20367/cf_1174/the-atlantic-road-national-tourist-route-norway_74.JPG')");
        div.css("background-size", "80vw");
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
        $("#kaf3").css("background-image","none");

    });
});


$(document).ready(function() {
    $("#hobbyopis3, #square").hide();
});



$(document).ready(function(){
    $("#kaf3, #gory").click(function(){
        var div = $("#kaf3");
        $("#kaf1, #kaf2, #kaf4").hide();
        div.css("margin-left","10vw");
        div.animate({width: '80vw'}, "slow");
        $("#hobbyopis3, #square").show();
        div.animate({height: "700%"}, "slow");
        div.css("background-image", "url('https://scontent-ams2-1.xx.fbcdn.net/hphotos-xfp1/v/t1.0-9/923179_4889005586940_87398359_n.jpg?oh=78bcce097dc059724e7dbe7418bd1104&oe=5624BC39')");
        div.css("background-size", "80vw");
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
        $("#kaf4").css("background-image","none");

    });
});


$(document).ready(function() {
    $("#hobbyopis4, #square").hide();
});



$(document).ready(function(){
    $("#kaf4, #hydepark").click(function(){
        var div = $("#kaf4");
        $("#kaf1, #kaf2, #kaf3").hide();
        div.css("margin-left","10vw");
        div.animate({width: '80vw'}, "slow");
        $("#hobbyopis4, #square").show();
        div.animate({height: "700%"}, "slow");
        div.css("background-image", "url('https://lh3.googleusercontent.com/-LysLjIsAW7c/S9HoGXheDOI/AAAAAAAAEGE/cXWcwmqGGU8/s640-Ic42/DSC08963.JPG')");
        div.css("background-position", "0px -160px");
        div.css("background-size", "80vw");
    });
});












/*CV animation */
/*paski umiejetnosci skill */
















/*
$(document).ready(function(){
    $(".cvbody").click(function(){
        $("#cecha2").animate({width: '19%'}, "slow");
        $("#cecha1").animate({width: '80%'}, "slow");
        $("#cecha1").animate({width: '81%'}, "fast");


    });
});
*/






$(document).ready(function() {
    $( ".progressbar" ).progressbar({
      value: 1
    });
  });

/*
$(document).ready(function() {
    $( ".cvbod" ).click(function() {
    $( "#Arc" ).progressbar({value: 70});
    $( "#Micro" ).progressbar({value: 80});
    $( "#Faro" ).progressbar({value: 60});
    $( "#Qgis" ).progressbar({value: 50});
    $( "#Cad" ).progressbar({value: 70});
    $( "#Agi" ).progressbar({value: 40});

    });
  });
*/
$(document).ready(function() {
$( ".cvbod" ).click(function() {
$("#Arc .ui-progressbar-value").animate({width: "70%"}, {queue: false});
$("#Micro .ui-progressbar-value").animate({width: "80%"}, {queue: false});
$("#Faro .ui-progressbar-value").animate({width: "60%"}, {queue: false});
$("#Qgis .ui-progressbar-value").animate({width: "50%"}, {queue: false});
$("#Cad .ui-progressbar-value").animate({width: "70%"}, {queue: false});
$("#Agi .ui-progressbar-value").animate({width: "40%"}, {queue: false});
    });
 });


$(document).ready(function() {
$(".progressbar").css({ 'background': '#444444' });
});



$(document).ready(function() {
    function latlong() {
      return new google.maps.LatLng( $("#lat").val(), $("#lng").val() );
    }
    function position() {
      map.setCenter( latlong() );
    }
    $( "#lat, #lng" ).spinner({
      step: .001,
      change: position,
      stop: position
    });

    var map = new google.maps.Map( $("#map")[0], {
      zoom: 19,
      center: latlong(),
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });
  });



$(document).ready(function() {
    $( "#tog" ).click(function() {
    $( "#toglek" ).toggle( "explode", 1000 );
        });
  });


/*
$(document).ready(function() {
$( "#tog" ).click(function () {
  if ( $( "#toglek" ).is( ":hidden" ) ) {
    $( "#toglek" ).slideDown( "slow" );
  } else {
    $( "#toglek" ).hide();
  }
});
});
  */



$(function() {
    $( "#tabs" ).tabs().addClass( "ui-tabs-vertical ui-helper-clearfix" );
    $( "#tabs li" ).removeClass( "ui-corner-top" ).addClass( "ui-corner-left" );
});

