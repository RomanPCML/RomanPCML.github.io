BASECOORDS = [48.1, 11.8];



var start_lat
var start_lon



const promise1 = new Promise(function(resolve, reject) {

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(position){
                start_lat = position.coords.latitude
                start_lon = position.coords.longitude

                console.log(position.coords.latitude, position.coords.longitude)
                resolve([start_lat, start_lon])
            }
        );
    } else {
        console.log("no position");
        reject()
    }

    

});


promise1.then(function(latlon) {

    console.log(latlon[0],latlon[1])
    document.getElementById("mydiv").innerHTML = "You can now join. Take care!" + latlon[0].toString() + latlon[1].toString();
    renderPosition(latlon[0],latlon[1])
    user_id = "1"
    $.post( "/users/<string:user_id>", {
        user_id:  {"lat": start_lat, "lon": start_lon}
    });
});


/*


function get_name(){


    var person = prompt("Please enter your name:", "Harry Potter");

    if (person == null || person == "") {
      console.log("User cancelled the prompt.");
    } else {
      var name = person;

    } 

    open_map(start_lat, start_lon, name)
    console.log("map should be there", start_lat, start_lon, name)
    return name



};

*/


function makeMap() {
    var TILE_URL = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
    var MB_ATTR = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
    mymap = L.map('llmap').setView(BASECOORDS, 20);
    L.marker(BASECOORDS).addTo(mymap)
    L.tileLayer(TILE_URL, {attribution: MB_ATTR}).addTo(mymap);
}

var layer = L.layerGroup();

function renderData() {
    $.getJSON("/points" , function(obj) {

    
    var markers = obj.data.map(function(arr) {
            return L.marker([arr[0], arr[1]]);
        });

        mymap.removeLayer(layer);
        layer = L.layerGroup(markers);
        mymap.addLayer(layer);
    });
}


function renderPosition(lat, lon) {

    L.marker([start_lat, start_lon]).addTo(mymap)

}









$(function() {
    makeMap();
    renderData();



    

   
})
