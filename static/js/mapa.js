(function(){
    "use strict";

      document.addEventListener('DOMContentLoaded', function(){

        var map = L.map('mapa').setView([-34.5617, -58.4113], 15);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        L.marker([-34.5617, -58.4113]).addTo(map)
            .bindPopup('Aeroparque Jorge Newbery')
            .openPopup();

      }); //Contenido del DOM cargado
})()
