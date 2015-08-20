
$(document).ready(function() {
    $( ".progressbar" ).progressbar({
      value: 1
    });
  });



$(document).ready(function() {
$(".progressbar").css({ 'background': '#444444' });
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




(function($) {

         // DOM Ready
        $(function() {

            // Binding a click event
            // From jQuery v.1.7.0 use .on() instead of .bind()
            $('#my-button1').bind('click', function(e) {

                // Prevents the default action to be triggered.
                e.preventDefault();

                // Triggering bPopup when click event is fired
                $('#kaf1').bPopup({easing: 'easeOutBack', //uses jQuery easing plugin
            speed: 450,
            transition: 'slideDown'});

            });

        });

    })(jQuery);

(function($) {

         // DOM Ready
        $(function() {

            // Binding a click event
            // From jQuery v.1.7.0 use .on() instead of .bind()
            $('#my-button2').bind('click', function(e) {

                // Prevents the default action to be triggered.
                e.preventDefault();

                // Triggering bPopup when click event is fired
                $('#kaf2').bPopup({easing: 'easeOutBack', //uses jQuery easing plugin
            speed: 450,
            transition: 'slideDown'});

            });

        });

    })(jQuery);
    (function($) {

         // DOM Ready
        $(function() {

            // Binding a click event
            // From jQuery v.1.7.0 use .on() instead of .bind()
            $('#my-button3').bind('click', function(e) {

                // Prevents the default action to be triggered.
                e.preventDefault();

                // Triggering bPopup when click event is fired
                $('#kaf3').bPopup({easing: 'easeOutBack', //uses jQuery easing plugin
            speed: 450,
            transition: 'slideDown'});

            });

        });

    })(jQuery);
    (function($) {

         // DOM Ready
        $(function() {

            // Binding a click event
            // From jQuery v.1.7.0 use .on() instead of .bind()
            $('#my-button4').bind('click', function(e) {

                // Prevents the default action to be triggered.
                e.preventDefault();

                // Triggering bPopup when click event is fired
                $('#kaf4').bPopup({easing: 'easeOutBack', //uses jQuery easing plugin
            speed: 450,
            transition: 'slideDown',
            modalColor: 'grey'});

            });

        });

    })(jQuery);