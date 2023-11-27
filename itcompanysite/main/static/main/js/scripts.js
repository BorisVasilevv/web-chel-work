//var element1 = document.getElementById("categories-item_details__1");
//element1.addEventListener("click", (event) => showDescription(event, "categories-item_details__1", "categories-item__1"));
//
//var element2 = document.getElementById("categories-item_details__2");
//element2.addEventListener("click", (event) => showDescription(event, "categories-item_details__2", "categories-item__2"));
//
//var element3 = document.getElementById("categories-item_details__3");
//element3.addEventListener("click", (event) => showDescription(event, "categories-item_details__3", "categories-item__3"));
//
//var element4 = document.getElementById("categories-item_details__4");
//element4.addEventListener("click", (event) => showDescription(event, "categories-item_details__4", "categories-item__4"));
//
//var element5 = document.getElementById("categories-item_details__5");
//element5.addEventListener("click", (event) => showDescription(event, "categories-item_details__5", "categories-item__5"));
//
//var element6 = document.getElementById("categories-item_details__6");
//element6.addEventListener("click", (event) => showDescription(event, "categories-item_details__6", "categories-item__6"));
//
//var element7 = document.getElementById("categories-item_details__7");
//element7.addEventListener("click", (event) => showDescription(event, "categories-item_details__7", "categories-item__7"));
//
//var element8 = document.getElementById("categories-item_details__8");
//element8.addEventListener("click", (event) => showDescription(event, "categories-item_details__8", "categories-item__8"));
//
//function showDescription(event, categoriesItemDetailsId ,categoriesItemId) {
//    let categoriesItemDetails = document.getElementById(categoriesItemDetailsId);
//    let categoriesItem = document.getElementById(categoriesItemId);
//    if (categoriesItemDetails.open){
//    categoriesItem.style.width = "250px"; // скрыть div при открытии details
//    } else {
//    categoriesItem.style.width = "500px"; // показать div при закрытии details
//    }
//}
//$(document).ready(function() {
//    $( "#main-page-map-container").load( "map/" );
//});
<!-- скриптик для карты -->
ymaps.ready(init);
    function init(){
        var myMap = new ymaps.Map ('map', {
            center: [55.161997, 61.401485], //координаты центра
            zoom: 15 //уровень приближения
        });

        /*экземпляр*/
        var myPlacemark = new ymaps.Placemark([55.161997, 61.401485], {
            iconContent: 'Чилик', //текст на иконке
            balloonContent: 'Взрывной город' /*текст появляющийся после нажатия*/
        }, {
            preset: 'twirl#blueStretchyIcon' //тип иконки
        });

        /*добавление кнопочки*/
        myMap.geoObjects.add(myPlacemark);
    }