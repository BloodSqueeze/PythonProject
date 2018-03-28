var script = document.createElement('script');
script.src = 'http://code.jquery.com/jquery-1.11.0.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);


$(document).ready(function(){
    $('.sidenav').sidenav();
  });

  /* Carousel Image*/
  $(document).ready(function(){
    $('.carousel').carousel();
  });

  /* audio Player*/
  $(document).ready(function(){
    $("#jquery_jplayer_1").jPlayer({
     ready: function () {
      $(this).jPlayer("setMedia", {
       m4a: "/media/mysound.mp4",
       oga: "/media/mysound.ogg"
      });
     },
     swfPath: "/js",
     supplied: "m4a, oga"
    });
   });