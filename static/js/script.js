/*chowa wszystkie wpisy w hobby*/
$(document).ready(function() {
    $("#hobbyopis1, #hobbyopis4").hide();
});


/*obsługa zdarzen dla pól hobby */
$(document).ready(function(){
$( ".kaf" ).click(function() {
  $( ".kaf" ).not( this ).toggleClass( "notclass", 1, "easeOutSine" );
  $( "#hobbyopis1, #hobbyopis4" ).toggle( "slide", 1 );
  $( this ).toggleClass( "kafopen", 1, "easeOutSine" );
  $("#kaf1").toggleClass("kaf1",1, "easeOutSine" );
  $("#kaf2").toggleClass("kaf2",1, "easeOutSine" );
  $("#kaf3").toggleClass("kaf3",1, "easeOutSine" );
  $("#kaf4").toggleClass("kaf4",1, "easeOutSine" );

});
});

/* obsluga zdarzen dla naglowkow*/

$(document).ready(function(){
$( "#narty" ).click(function() {
  $( ".kaf" ).not( "#kaf1" ).toggleClass( "notclass", 1, "easeOutSine" );
  $( "#hobbyopis1, #hobbyopis4" ).toggle( "slide", 1 );
  $( "#kaf1" ).toggleClass( "kafopen", 1, "easeOutSine" );
  $("#kaf1").toggleClass("kaf1",1, "easeOutSine" );
  $("#kaf2").toggleClass("kaf2",1, "easeOutSine" );
  $("#kaf3").toggleClass("kaf3",1, "easeOutSine" );
  $("#kaf4").toggleClass("kaf4",1, "easeOutSine" );
});
});

$(document).ready(function(){
$( "#rower" ).click(function() {
  $( ".kaf" ).not( "#kaf2" ).toggleClass( "notclass", 1, "easeOutSine" );
  $( "#hobbyopis1, #hobbyopis4" ).toggle( "slide", 1 );
  $( "#kaf2" ).toggleClass( "kafopen", 1, "easeOutSine" );
  $("#kaf1").toggleClass("kaf1",1, "easeOutSine" );
  $("#kaf2").toggleClass("kaf2",1, "easeOutSine" );
  $("#kaf3").toggleClass("kaf3",1, "easeOutSine" );
  $("#kaf4").toggleClass("kaf4",1, "easeOutSine" );
});
});

$(document).ready(function(){
$( "#gory" ).click(function() {
  $( ".kaf" ).not( "#kaf3" ).toggleClass( "notclass", 1, "easeOutSine" );
  $( "#hobbyopis1, #hobbyopis4" ).toggle( "slide", 1 );
  $( "#kaf3" ).toggleClass( "kafopen", 1, "easeOutSine" );
  $("#kaf1").toggleClass("kaf1",1, "easeOutSine" );
  $("#kaf2").toggleClass("kaf2",1, "easeOutSine" );
  $("#kaf3").toggleClass("kaf3",1, "easeOutSine" );
  $("#kaf4").toggleClass("kaf4",1, "easeOutSine" );
});
});

$(document).ready(function(){
$( "#hydepark" ).click(function() {
  $( ".kaf" ).not( "#kaf4" ).toggleClass( "notclass", 1, "easeOutSine" );
  $( "#hobbyopis1, #hobbyopis4" ).toggle( "slide", 1 );
  $( "#kaf4" ).toggleClass( "kafopen", 1, "easeOutSine" );
  $("#kaf1").toggleClass("kaf1",1, "easeOutSine" );
  $("#kaf2").toggleClass("kaf2",1, "easeOutSine" );
  $("#kaf3").toggleClass("kaf3",1, "easeOutSine" );
  $("#kaf4").toggleClass("kaf4",1, "easeOutSine" );
});
});



$(document).ready(function() {
    $( ".progressbar" ).progressbar({
      value: 1
    });
  });


$(document).ready(function() {
$( ".cvbod" ).mouseenter(function() {
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
    $( "#tog, #toglek" ).click(function() {
    $("#toglek").toggle( "blind", 1000 );
        });
  });

$(document).ready(function() {
    $( "#tog2, #toglek2" ).click(function() {
    $("#toglek2").toggle( "blind", 1000 );
        });
  });




$(document).ready(function() {
    $( ".togi" ).hide();
});


$(function() {
    $( "#tabs" ).tabs().addClass( "ui-tabs-vertical ui-helper-clearfix" );
    $( "#tabs li" ).removeClass( "ui-corner-top" ).addClass( "ui-corner-left" );
});



/* POP UP*/

$(function() {
    $('.link').click(function(e) {
        //jeżeli popup nie jest widoczny to go pokaż
        if (!$('.popup:visible').length) {
            $('.popup').fadeIn();
        }
        e.preventDefault();
        return false;
    });

    //zdarzenie zamknięcia podpinamy pod przycisk close i pod tło popupa
    $('.popup .close, .popup .bg').click(function() {
        $(this).parents('.popup').fadeOut();
    });
})




$(function() {
    $( document ).tooltip({

      items: "img, [data-geo], [title]",
      content: function() {
        var element = $( this );

        if ( element.is( "[data-geo]" ) ) {
          var text = element.text();
          return "<img class='map' alt='" + text +
            "' src='http://maps.google.com/maps/api/staticmap?" +
            "zoom=11&size=350x350&maptype=terrain&sensor=false&center=" +
            text + "'>";
        }
        if ( element.is( "[title]" ) ) {
          return element.attr( "title" );
        }
        if ( element.is( "img" ) ) {
          return element.attr( "alt" );
        }
      }
    });
  });


