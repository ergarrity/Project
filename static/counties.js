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
    // $.get('/counties.json', function (response) {
    //   debugger;
    //   let counties = response.counties;
    //   // Attach markers to each bear location in returned JSON
    //   // JSON looks like:
    //   // {
    //   //  "1": {
    //   //    "bearId": "1737",
    //   //    "birthYear": "1970",
    //   //    "capLat": "70.71139573",
    //   //    "capLong": "-147.8381939",
    //   //    "capYear": "2001",
    //   //    "collared": "true",
    //   //    "gender": "F"
    //   //   },...
    //   // }
    //   let county, marker, html;

    //   for (let key in counties) {
    //         county = counties[key];

    //         // Define the marker
    //             marker = new google.maps.Marker({
    //                 position: new google.maps.LatLng(county.capLat, county.capLong),
    //                 map: map,
    //                 title: county.county_name + ' County',
    //                 // icon: '/static/img/polar.png'
    //             });

    //         // Define the content of the infoWindow
    //         html = (
    //           '<div class="window-content">' +
    //                 '<img src="/static/img/polarbear.jpg" alt="polarbear" style="width:150px;" class="thumbnail">' +
    //                 // '<p><b>Bear gender: </b>' + bear.gender + '</p>' +
    //                 // '<p><b>Bear birth year: </b>' + bear.birthYear + '</p>' +
    //                 // '<p><b>Year captured: </b>' + bear.capYear + '</p>' +
    //                 // '<p><b>Collared: </b>' + bear.collared + '</p>' +
    //                 // '<p><b>Location: </b>' + marker.position + '</p>' +
    //           '</div>');

    //         // Inside the loop we call bindInfoWindow passing it the marker,
    //         // map, infoWindow and contentString
    //         bindInfoWindow(marker, map, infoWindow, html);
    //   }

    // });

    // This function is outside the for loop.
    // When a marker is clicked it closes any currently open infowindows
//     // Sets the content for the new marker with the content passed through
//     // then it open the infoWindow with the new content on the marker that's clicked
//     function bindInfoWindow(marker, map, infoWindow, html) {
//         google.maps.event.addListener(marker, 'click', function () {
//             infoWindow.close();
//             infoWindow.setContent(html);
//             infoWindow.open(map, marker);
//         });
//     }
}

google.maps.event.addDomListener(window, 'load', initMap);
