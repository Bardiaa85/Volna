function addToFav(slug) {
    const baseUrl = window.location.origin ;
    const url = `${baseUrl}/favorites/add-to-favorites/${slug}`;
    const addToFavContainer = document.getElementById('addToFavContainer');   
    fetch(url, {
        method: 'GET' ,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.status === 'success') {
            console.log('Data saved successfully:', data.message);
            addToFavContainer.innerHTML = `
                  <button style="width: 40px; height: 40px;" onclick="delFromFav('${slug}')" class="single-item__add">
                            <svg style="width: 23px; height: 23px;" xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-file-earmark-x" viewBox="0 0 16 16">
                                <path d="M6.854 7.146a.5.5 0 1 0-.708.708L7.293 9l-1.147 1.146a.5.5 0 0 0 .708.708L8 9.707l1.146 1.147a.5.5 0 0 0 .708-.708L8.707 9l1.147-1.146a.5.5 0 0 0-.708-.708L8 8.293z"/>
                                <path d="M14 14V4.5L9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2M9.5 3A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h5.5z"/>
                              </svg>
                            </button>
                        <p style="color: #c0c0c0; margin-top: 5px; cursor: default; ">پاک کردن از لیست علاقه‌مندی ها</p>`
            ;
        } else {
            console.error('Error saving data:', data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
function delFromFav(slug) {
    const baseUrl = window.location.origin ;
    const url = `${baseUrl}/favorites/delete-from-favorites/${slug}`;
    const addToFavContainer = document.getElementById('addToFavContainer');   
    fetch(url, {
        method: 'GET' ,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.status === 'success') {
            console.log('Data saved successfully:', data.message);
            addToFavContainer.innerHTML = `
                <button id="addToFav" style="width: 40px; height: 40px;" onclick="addToFav('${slug}')" class="single-item__add">
                <svg style="width: 25px; height: 25px;" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19,11H13V5a1,1,0,0,0-2,0v6H5a1,1,0,0,0,0,2h6v6a1,1,0,0,0,2,0V13h6a1,1,0,0,0,0-2Z"/></svg>
                </button>
                <p  style="color: #c0c0c0; margin-top: 5px; cursor: default; ">افزودن به لیست علاقه‌مندی ها</p>
                `
            ;
        } else {
            console.error('Error saving data:', data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
