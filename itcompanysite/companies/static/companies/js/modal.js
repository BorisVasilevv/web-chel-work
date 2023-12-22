

// Находим тег html и сохраняем его
let html = document.documentElement;
//сохраним текущую прокрутку:
let scrollPosition = window.pageYOffset;
//установим свойство top у html равное прокрутке
html.style.top = -scrollPosition + "px";
html.classList.add("register_modal__opened");


html.classList.remove("register_modal__opened");
//прокручиваем окно туда где оно было
window.scrollTo(0, scrollPosition);
html.style.top = "";