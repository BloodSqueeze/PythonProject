

var script = document.createElement('script');
script.src = 'http://code.jquery.com/jquery-1.11.0.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);


$(document).ready(function(){
    $('.parallax').parallax();
});

$(document).ready(function() {
    $('input#input_text, textarea#textarea2').characterCounter();
  });

    /* Carousel Image*/
    $(document).ready(function(){
        $('.carousel').carousel();
      });