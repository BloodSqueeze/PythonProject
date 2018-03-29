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

/*Accordion*/

$(document).ready(function(){
  $('.collapsible').collapsible();
});
    





/* Javascript for Napster API */

const tracksTemplateSource = document.getElementById('tracks-template').innerHTML;
const tracksTemplate = Handlebars.compile(tracksTemplateSource);

const $tracks = $('#tracks-container');

const getTopTracks = $.get('https://api.napster.com/v2.1/tracks/top?apikey=ZTk2YjY4MjMtMDAzYy00MTg4LWE2MjYtZDIzNjJmMmM0YTdm');

getTopTracks
  .then((response) => {
    $tracks.html(tracksTemplate(response));
  });
      

            