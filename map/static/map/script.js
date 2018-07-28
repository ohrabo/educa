// function loadJSON(url) {
//   var jhr = new XMLHttpRequest();
//   jhr.open("GET", url, false);
//   jhr.send(null);
//   var jsonObject = JSON.parse(jhr.responseText);
//   return jsonObject;
// }
//
// var markers = loadJSON("markers.json");


// var map = L.map('map').setView([49.8397, 24.0297], 2);
// //Add OpenStreetMap layer
// L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     attribution: '&copy; <a rel="nofollow" href="http://osm.org/copyright">OpenStreetMap</a> contributors'
// }).addTo(map);


function addMarker() {
    for (i = 0; i < markers.length; i++) {
        for (j = 0; j < markers[i].details.length; j++) {
            if (markers[i].category === category.value) {
                L.marker([markers[i].details[j].lat, markers[i].details[j].lon]).addTo(map)

            }
        }
    }
    return (document.getElementById("category"))
}


//
// function addnewmarker(){
// var markers = {{locations|safe}}
//     for (i = 0; i < Object.keys(markers).length; i++) {
//         L.marker([parseFloat(Object.keys(markers)[i]),Object.value(markers)[i]]).addTo(map)
//         }
    // return (document.getElementById("category"))
// }
