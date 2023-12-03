
<!-- скриптик для карты -->
ymaps.ready(init);
    function init(){
        var myMap = new ymaps.Map ('map', {
            center: [55.161997, 61.401485], //координаты центра
            zoom: 12 //уровень приближения
        });

        /*экземпляр*/
        var chelgy = new ymaps.Placemark([55.177640451171285, 61.31967316313907], {
            hintContent: 'ЧелГУ', //текст на иконке
            balloonContent: 'Комфортное место'
        }, {
        iconColor: '#ff0000' //тип иконки
            });

        var enigma = new ymaps.Placemark([55.162322563924604, 61.37485434686038], {
            hintContent: 'Энигма', //текст на иконке
            balloonContent: 'Кибербезопасность'
        }, {
        iconColor: '#94D377' //тип иконки
            });

        var flab = new ymaps.Placemark([55.156877627170346, 61.30099144042235], {
            hintContent: 'F-LAB', //текст на иконке
            balloonContent: 'Кибербезопасность'
        }, {
        iconColor: '#94D377' //тип иконки
            });

        var intersvyaz = new ymaps.Placemark([55.17315000190367, 61.365313565575164], {
            hintContent: 'Интерсвязь', //текст на иконке
            balloonContent: 'Собственная разработка'
        }, {
        iconColor: '#ff0495' //тип иконки
            });

        var inovationKids = new ymaps.Placemark([55.15493100593255, 61.40023052271539], {
            hintContent: 'Инновации детям', //текст на иконке
            balloonContent: 'Собственная разработка'
        }, {
        iconColor: '#ff0495' //тип иконки
            });

        var novaGames = new ymaps.Placemark([55.16207655138783, 61.43051607119092], {
            hintContent: 'Nova Games', //текст на иконке
            balloonContent: 'GameDev'
        }, {
        iconColor: '#FF8A00' //тип иконки
            });

        var tapclap = new ymaps.Placemark([55.164874685353645, 61.401122082826944], {
            hintContent: 'TAPCLAP', //текст на иконке
            balloonContent: 'GameDev'
        }, {
        iconColor: '#FF8A00' //тип иконки
            });

        var playrix = new ymaps.Placemark([55.170745197135254, 61.413583227009354], {
            hintContent: 'Playrix', //текст на иконке
            balloonContent: 'GameDev'
        }, {
        iconColor: '#FF8A00' //тип иконки
            });

        var odinGames = new ymaps.Placemark([55.169148746093036, 61.378706984682104], {
            hintContent: 'Odin Games', //текст на иконке
            balloonContent: 'GameDev'
        }, {
        iconColor: '#FF8A00' //тип иконки
            });

        var threeDivi = new ymaps.Placemark([55.16480844266152, 61.401059942354664], {
            hintContent: '3 Divi', //текст на иконке
            balloonContent: 'IT-Стартап'
        }, {
        iconColor: '#ff0495' //тип иконки
            });

        var skbContur = new ymaps.Placemark([55.15576413484781, 61.370867812263874], {
            hintContent: 'СКБ-Контур', //текст на иконке
            balloonContent: 'IT-Стартап'
        }, {
        iconColor: '#fff700' //тип иконки
            });

        var ASPRO = new ymaps.Placemark([55.190730814944175, 61.33353100555804], {
            hintContent: 'АСПРО', //текст на иконке
            balloonContent: 'Заказная разработка'
        }, {
        iconColor: '#94D377' //тип иконки
            });

        var dextra = new ymaps.Placemark([55.14926455931064, 61.385146816169396], {
            hintContent: 'Dextra', //текст на иконке
            balloonContent: 'Заказная разработка'
        }, {
        iconColor: '#94D377' //тип иконки
            });

        var digitalElement = new ymaps.Placemark([55.16501443448449, 61.37425512082958], {
            hintContent: 'Цифровой элемент', //текст на иконке
            balloonContent: 'Заказная разработка'
        }, {
        iconColor: '#94D377' //тип иконки
            });

        var napoleon = new ymaps.Placemark([55.162085806673836, 61.397694811663214], {
            hintContent: 'Napoleon IT', //текст на иконке
            balloonContent: 'Заказная разработка'
        }, {
        iconColor: '#94D377' //тип иконки
            });

        var unitSix = new ymaps.Placemark([55.15688962758773, 61.302039981860936], {
            hintContent: 'Unit6', //текст на иконке
            balloonContent: 'Заказная разработка'
        }, {
        iconColor: '#94D377' //тип иконки
            });

        var byndyusoft = new ymaps.Placemark([55.16849278757826, 61.40638978282713], {
            hintContent: 'Byndyusoft', //текст на иконке
            balloonContent: 'Заказная разработка'
        }, {
        iconColor: '#94D377' //тип иконки
            });

        var Xpage = new ymaps.Placemark([55.15369593760404, 61.364913353990026], {
            hintContent: 'Xpage', //текст на иконке
            balloonContent: 'Заказная разработка'
        }, {
        iconColor: '#94D377' //тип иконки
            });

        var fuse8 = new ymaps.Placemark([55.164439229950894, 61.30143849817261], {
            hintContent: 'fuse8', //текст на иконке
            balloonContent: 'Заказная разработка'
        }, {
        iconColor: '#94D377' //тип иконки
            });

        var engineDevelopment = new ymaps.Placemark([55.191764377931044, 61.35612132701031], {
            hintContent: 'Прикладные технологии', //текст на иконке
            balloonContent: 'Заказная разработка'
        }, {
        iconColor: '#94D377' //тип иконки
            });

        var idScan = new ymaps.Placemark([55.17738374482536, 61.40015691351884], {
            hintContent: 'ID Scan', //текст на иконке
            balloonContent: 'Заказная разработка'
        }, {
        iconColor: '#94D377' //тип иконки
            });

        var antidaSoft = new ymaps.Placemark([55.16584563980339, 61.4095245116634], {
            hintContent: 'Antida software', //текст на иконке
            balloonContent: 'Заказная разработка'
        }, {
        iconColor: '#94D377' //тип иконки
            });

        var lanit = new ymaps.Placemark([55.1645905438025, 61.40106692329928], {
            hintContent: 'Ланит', //текст на иконке
            balloonContent: 'Заказная разработка'
        }, {
        iconColor: '#94D377' //тип иконки
            });

        var infinnity = new ymaps.Placemark([55.15672528689525, 61.30157939817233], {
            hintContent: 'Infinnity solution', //текст на иконке
            balloonContent: 'Заказная разработка'
        }, {
        iconColor: '#94D377' //тип иконки
            });

        var consomSks = new ymaps.Placemark([53.35964069213474, 58.97011004310974], {
            hintContent: 'Консом СКС', //текст на иконке
            balloonContent: 'Заказная разработка'
        }, {
        iconColor: '#94D377' //тип иконки
            });


        /*добавление кнопочки*/
        myMap.geoObjects.add(chelgy);
        myMap.geoObjects.add(enigma);
        myMap.geoObjects.add(flab);
        myMap.geoObjects.add(intersvyaz);
        myMap.geoObjects.add(inovationKids);
        myMap.geoObjects.add(novaGames);
        myMap.geoObjects.add(tapclap);
        myMap.geoObjects.add(playrix);
        myMap.geoObjects.add(odinGames);
        myMap.geoObjects.add(threeDivi);
        myMap.geoObjects.add(ASPRO);
        myMap.geoObjects.add(dextra);
        myMap.geoObjects.add(digitalElement);
        myMap.geoObjects.add(napoleon);
        myMap.geoObjects.add(unitSix);
        myMap.geoObjects.add(byndyusoft);
        myMap.geoObjects.add(Xpage);
        myMap.geoObjects.add(fuse8);
        myMap.geoObjects.add(engineDevelopment);
        myMap.geoObjects.add(lanit);
        myMap.geoObjects.add(infinnity);
        myMap.geoObjects.add(consomSks);

    }