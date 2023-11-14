import folium

map = folium.Map(location=(55.16523510061088, 61.427102328027054), zoom_start=14)
mark_ch = folium.Marker(
    location=[55.17810281780689, 61.31967807545179],
    tooltip="IT компания",
    popup="ЧелГУ",
    icon=folium.Icon(color="red")
)
mark_ch.add_to(map)

folium.Marker(
    location=[55.162322563924604, 61.37485434686038],
    tooltip="Кибербезопасность",
    popup="ИТ Энигма",
    icon=folium.Icon(color="green")
).add_to(map)

folium.Marker(
    location=[55.156877627170346, 61.30099144042235],
    tooltip="Кибербезопасность",
    popup="F-LAB",
    icon=folium.Icon(color="green")
).add_to(map)

folium.Marker(
    location=[55.17315000190367, 61.365313565575164],
    tooltip="Собственная разработка",
    popup="Интерсвязь",
    icon=folium.Icon(color="pink")
).add_to(map)

folium.Marker(
    location=[55.15493100593255, 61.40023052271539],
    tooltip="Собственная разработка",
    popup="Инновации детям",
    icon=folium.Icon(color="pink")
).add_to(map)

folium.Marker(
    location=[55.16207655138783, 61.43051607119092],
    tooltip="GameDev",
    popup="Nova Games",
    icon=folium.Icon(color="orange")
).add_to(map)

folium.Marker(
    location=[55.164874685353645, 61.401122082826944],
    tooltip="GameDev",
    popup="TAPCLAP",
    icon=folium.Icon(color="orange")
).add_to(map)

folium.Marker(
    location=[55.170745197135254, 61.413583227009354],
    tooltip="GameDev",
    popup="Playrix",
    icon=folium.Icon(color="orange")
).add_to(map)

folium.Marker(
    location=[55.169148746093036, 61.378706984682104],
    tooltip="GameDev",
    popup="Odin Games",
    icon=folium.Icon(color="orange")
).add_to(map)

# folium.Marker(
#     location=[],
#     tooltip="IT-Стартап",
#     popup="Zayzev.net",
#     icon=folium.Icon(color="pink")
# ).add_to(map)
#
# folium.Marker(
#     location=[],
#     tooltip="IT-Стартап",
#     popup="EveryPixel",
#     icon=folium.Icon(color="pink")
# ).add_to(map)

folium.Marker(
    location=[55.16480844266152, 61.401059942354664],
    tooltip="IT-Стартап",
    popup="3 Divi",
    icon=folium.Icon(color="pink")
).add_to(map)

folium.Marker(
    location=[55.15576413484781, 61.370867812263874],
    tooltip="IT-Стартап",
    popup="СКБ-Контур",
    icon=folium.Icon(color="pink")
).add_to(map)

folium.Marker(
    location=[55.190730814944175, 61.33353100555804],
    tooltip="Заказная разработка",
    popup="АСПРО",
    icon=folium.Icon(color="green")
).add_to(map)

folium.Marker(
    location=[55.14926455931064, 61.385146816169396],
    tooltip="Заказная разработка",
    popup="Dextra",
    icon=folium.Icon(color="green")
).add_to(map)

folium.Marker(
    location=[55.16501443448449, 61.37425512082958],
    tooltip="Заказная разработка",
    popup="Цифровой элемент",
    icon=folium.Icon(color="green")
).add_to(map)

mark_ch = folium.Marker(
    location=[55.162085806673836, 61.397694811663214],
    tooltip="Заказная разработка",
    popup="Napoleon IT",
    icon=folium.Icon(color="green")
)
mark_ch.add_to(map)

folium.Marker(
    location=[55.15688962758773, 61.302039981860936],
    tooltip="Заказная разработка",
    popup="Unit6",
    icon=folium.Icon(color="green")
).add_to(map)

folium.Marker(
    location=[55.16849278757826, 61.40638978282713],
    tooltip="Заказная разработка",
    popup="Byndyusoft",
    icon=folium.Icon(color="green")
).add_to(map)

mark_xp = folium.Marker(
    location=[55.15369593760404, 61.364913353990026],
    tooltip="Заказная разработка",
    popup="Xpage",
    icon=folium.Icon(color="green")
)
mark_xp.add_to(map)

folium.Marker(
    location=[55.164439229950894, 61.30143849817261],
    tooltip="Заказная разработка",
    popup="fuse8",
    icon=folium.Icon(color="green")
).add_to(map)

folium.Marker(
    location=[55.191764377931044, 61.35612132701031],
    tooltip="Заказная разработка",
    popup="Прикладные технологии",
    icon=folium.Icon(color="green")
).add_to(map)

folium.Marker(
    location=[55.17738374482536, 61.40015691351884],
    tooltip="Заказная разработка",
    popup="ID Scan",
    icon=folium.Icon(color="green")
).add_to(map)

folium.Marker(
    location=[55.16584563980339, 61.4095245116634],
    tooltip="Заказная разработка",
    popup="Antida software",
    icon=folium.Icon(color="green")
).add_to(map)

folium.Marker(
    location=[55.1645905438025, 61.40106692329928],
    tooltip="Заказная разработка",
    popup="Ланит",
    icon=folium.Icon(color="green")
).add_to(map)

folium.Marker(
    location=[55.15672528689525, 61.30157939817233],
    tooltip="Заказная разработка",
    popup="Инфиннити",
    icon=folium.Icon(color="green")
).add_to(map)

folium.Marker(
    location=[53.35964069213474, 58.97011004310974],
    tooltip="Заказная разработка",
    popup="Консом СКС",
    icon=folium.Icon(color="green")
).add_to(map)

map.save("templates/main/map.html")
