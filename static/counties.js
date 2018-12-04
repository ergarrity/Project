// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
// google.charts.setOnLoadCallback(drawChart);

function initMap() {
  console.log("hi i loaded");

    //specifies center of map
    let myLatLng = {lat: 43.921603, lng: -120.678400};

    // Create a map object and specify the DOM element for display.
    let map = new google.maps.Map(document.getElementById('counties-map'), {
        center: myLatLng,
        // scrollwheel: false,
        zoom: 6.5,
        zoomControl: true,
        // panControl: false,
        // streetViewControl: false,
        // styles: MAPSTYLES,
        // mapTypeId: google.maps.MapTypeId.TERRAIN
    });

    // --------------------------------------------------------------//
    // --------------------------------------------------------------//
    // If you want to create a StyledMapType to make a map type control
    // create it like this:

    // Create a new StyledMapType object, passing it the array of styles,
    // as well as the name to be displayed on the map type control.
    // let styledMap = new google.maps.StyledMapType(
    //     MAPSTYLES,
    //     {name: "Custom Style"}
    // );
    // You would then set 'styles' in the mapoptions to 'styledMap'

    // Associate the styled map with the MapTypeId and set it to display.
    // map.mapTypes.set('map_style', styledMap);
    // map.setMapTypeId('map_style');
    // --------------------------------------------------------------//
    // --------------------------------------------------------------//


    // Define global infoWindow
    let infoWindow = new google.maps.InfoWindow({
        width: 150
    });


    // Retrieving the information with AJAX
    $.get('/counties.json', function (counties) {

      let county, marker, html;

      for (let key in counties) {
        county = counties[key];
        
        marker = new google.maps.Marker({
          position: new google.maps.LatLng(county.latitude, county.longitude),
          map: map,
          title: county.county_name,
        });


        html = (
          '<div class="window-content">' +
                '<img src="/static/img/polarbear.jpg" alt="polarbear" style="width:150px;" class="thumbnail">' +
                '<p><b>County: </b>' + county.county_name + '</p>' +
          '</div>');

        bindInfoWindow(marker, map, infoWindow, html);
      }

    });

      function bindInfoWindow(marker, map, infoWindow, html) {
        google.maps.event.addListener(marker, 'click', function(){
          infoWindow.close();
          infoWindow.setContent(html);
          infoWindow.open(map, marker);
        });
      }
}

google.maps.event.addDomListener(window, 'load', initMap);
