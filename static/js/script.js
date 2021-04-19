var mymap = L.map('mapid').setView([51.208, 4.425], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    maxZoom: 18,
    id: 'mapbox/dark-v10',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibmNwd2xzIiwiYSI6ImNrbmx1YTR1ejBha2gybmt4cDVrcDN6OWgifQ.wmt7OvrQdw7yqsgvK5h_xg'
}).addTo(mymap);