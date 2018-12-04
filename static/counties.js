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
    // If you do this inside the loop where you retrieve the json,
    // the windows do not automatically close when a new marker is clicked
    // and you end up with a bunch of windows opened at the same time.
    // What this does is create one infowindow and we replace the content
    // // inside for each marker.
    let infoWindow = new google.maps.InfoWindow({
        width: 150
    });

    // Retrieving the information with AJAX
    $.get('/counties.json', function (counties) {
    // //   // Attach markers to each bear location in returned JSON
    // //   // JSON looks like:
    // //   // {
    // //   //  "1": {
    // //   //    "bearId": "1737",
    // //   //    "birthYear": "1970",
    // //   //    "capLat": "70.71139573",
    // //   //    "capLong": "-147.8381939",
    // //   //    "capYear": "2001",
    // //   //    "collared": "true",
    // //   //    "gender": "F"
    // //   //   },...
    // //   // }
      
      // let counties = response.counties;

      // counties = {
      //   "1": {
      //     "county_name": "Baker",
      //     "latitude": "44.776800",
      //     "longitude": "-117.83383"
      //   },
      //   "2": {
      //     "county_name": "Benton",
      //     "latitude" : "44.56541",
      //     "longitude": "-123.26214"
      //   },
      //   "3": {
      //     "county_name": "Clackamas",
      //     "latitude": "45.359449",
      //     "longitude": "-122.60234"
      //   }
      // }

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
