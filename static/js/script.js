// leaflet map

var mymap = L.map('mapid').setView([51.208, 4.425], 13);

mymap.zoomControl.setPosition('topright');

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    maxZoom: 18,
    id: 'mapbox/dark-v10',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibmNwd2xzIiwiYSI6ImNrbmx1YTR1ejBha2gybmt4cDVrcDN6OWgifQ.wmt7OvrQdw7yqsgvK5h_xg'
}).addTo(mymap);

// check whether inputdate is bigger than now

function checkDate() {
  var inputdate = new Date(document.getElementById('date').value);
  var today = new Date();
  if(inputdate.getDate() < today.getDate()) {
    console.log("Input date is in the past.")
  }
}

// add run form distance slider

function updateTextInput(val) {
  document.getElementById('distance').value=val + " km"; 
}