
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.add-fav').forEach(function (button) {
        button.addEventListener('click', function () {

            const companyId = button.getAttribute('data-company-id');

            addToFavorites(companyId);
        });
    });

    function addToFavorites(companyId) {
        fetch(`add_to_favorites/${companyId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            },
        })
        .then(response => {
            if (response.ok) {
                console.log(response);
                if(response.redirected){
                    alert('Пожалуйста, зайдите в систему.');
                }
                else {
                    changeDisplayButton(companyId);
                }

            }
        })
        .catch(error => console.error('Ошибка:', error));
    }

    document.querySelectorAll('.remove-fav').forEach(function (button) {
        button.addEventListener('click', function () {
            const companyId = button.getAttribute('data-company-id');
            removeFromFavorites(companyId);
        });
    });

    function removeFromFavorites(companyId) {
        // Отправить запрос на сервер для удаления компании из избранного
        fetch(`/accounts/remove_from_favorites/${companyId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'), // добавьте токен CSRF
            },
            body: JSON.stringify({
                company_id: companyId,
            })
        })
        .then(response => {
            if (response.ok) {
                add_container = document.getElementById('add-to-favorites-container-' + companyId);
                if (add_container === null){
                    company_card = document.getElementById('company-' + companyId);
                    company_card.classList.toggle("hidden");
                     company_card.classList.toggle("companies-item");
                }
                else{
                    changeDisplayButton(companyId);
                }
            }
        })
        .catch(error => console.error('Ошибка:', error));
    }

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }


    function changeDisplayButton(companyId){
        add_container = document.getElementById('add-to-favorites-container-' + companyId)
        remove_container = document.getElementById('remove-to-favorites-container-' + companyId);

        remove_container.classList.toggle("hidden");
        add_container.classList.toggle("hidden");
    }
});


