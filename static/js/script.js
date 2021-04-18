var token ="pk.eyJ1IjoibmNwd2xzIiwiYSI6ImNrbmx1YTR1ejBha2gybmt4cDVrcDN6OWgifQ.wmt7OvrQdw7yqsgvK5h_xg"; // replace with your Mapbox API Access token. Create a Mapbox account and find it on https://account.mapbox.com/

var map = L.map('map').setView([38.912753, -77.032194], 15);
L.marker([38.912753, -77.032194])
    .bindPopup("Hello <b>Leaflet GL</b>!<br>Whoa, it works!")
    .addTo(map)
    .openPopup();
var gl = L.mapboxGL({
    accessToken: token,
    style: 'mapbox://styles/mapbox/bright-v8'
}).addTo(map);