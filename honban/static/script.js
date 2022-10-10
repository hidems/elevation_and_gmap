var marker = null;
var lng = 16.373469829559326;
var lat = 48.20841626078853;

function init() {
  //initialize map
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 18, center: { lat: lat, lng: lng }
  });

  document.getElementById('lat').value = lat;
  document.getElementById('lng').value = lng;

  //initial marker
  marker = new google.maps.Marker({
    map: map, position: new google.maps.LatLng(lat, lng),
  });

  //Click event
  map.addListener('click', function (e) {
    clickMap(e.latLng, map);
  });
}

function clickMap(geo, map) {
  lat = geo.lat();
  lng = geo.lng();

  document.getElementById('lat').value = lat;
  document.getElementById('lng').value = lng;

  //Move marker to center
  map.panTo(geo);

  //Update marker position
  marker.setMap(null);
  marker = null;
  marker = new google.maps.Marker({
    map: map, position: geo
  });

}