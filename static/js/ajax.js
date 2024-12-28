function showReplayForm(button){
    const openForm = document.querySelector('.comments__form#replies__form') ;
    if (openForm){
        openForm.innerHTML = '' ;
        openForm.className = '' ;
    } ;
    const contentArea = button.parentNode.parentNode.nextElementSibling ;
    const htmlTags = `	
        <div class="sign__group">
        <textarea id="reply_input" name="comment" class="sign__textarea" placeholder="پاسخ شما ..."></textarea>
        </div>
        <button type="submit" class="sign__btn">ارسال</button>
    ` ;
    contentArea.classList.add('comments__form') ;
    contentArea.innerHTML = htmlTags ;
    contentArea.addEventListener('submit' ,
        function(event){
            event.preventDefault() ;
            const input = document.getElementById('reply_input') ;
            const commentContent = input.value ;
            const id = contentArea.getAttribute('data-id') ;
            const baseUrl = window.location.origin ;
            const url = `${baseUrl}/comments/adding-reply/${id}`;   
            fetch(url, {
                method: 'POST' ,
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                } ,
                body : JSON.stringify({content : commentContent})
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Network response was not ok: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                if (data.status === 'success') {
                    if (data.has_content){
                        const ul = document.getElementById('replies') ;
                        const newLi = document.createElement('li') ;
                        newLi.setAttribute('class' , 'comments__item comments__item--quote') ;
                        if (data.is_comment_user_admin){
                        newLi.innerHTML = `
                                        <div class="comments__autor">
                                        <img class="comments__avatar" src="/static/img/admin.jpg" alt="">
                                        <span style = "color: #B3FF80; "class="comments__name"><b>${data.comment_user_name}</b></span>
                                        <span class="comments__time">${data.comment_time} , ${data.comment_date}</span>
                                    </div>
                                    <p class="comments__text"><span>${data.replied_to_json.content}</span>${data.comment.content}</p>
                                    <div class="comments__actions">
                                        <div class="comments__rate">
                                        </div>
                                        <button style="color: #c0c0c0 ; margin-left: 15px;" onclick="delComment(${data.comment.id} , this)">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-trash2" viewBox="0 0 16 16">
                                                <path d="M14 3a.7.7 0 0 1-.037.225l-1.684 10.104A2 2 0 0 1 10.305 15H5.694a2 2 0 0 1-1.973-1.671L2.037 3.225A.7.7 0 0 1 2 3c0-1.105 2.686-2 6-2s6 .895 6 2M3.215 4.207l1.493 8.957a1 1 0 0 0 .986.836h4.612a1 1 0 0 0 .986-.836l1.493-8.957C11.69 4.689 9.954 5 8 5s-3.69-.311-4.785-.793"/>
                                              </svg>
                                            </button>
                                    
                                    </div>
                        `  } else {
                            newLi.innerHTML = `
                                        <div class="comments__autor">
                                        <img class="comments__avatar" src="/static/img/avatar.svg" alt="">
                                        <span "class="comments__name"><b>${data.comment_user_name}</b></span>
                                        <span class="comments__time">${data.comment_time} , ${data.comment_date}</span>
                                    </div>
                                    <p class="comments__text"><span>${data.replied_to_json.content}</span>${data.comment.content}</p>
                                    <div class="comments__actions">
                                        <div class="comments__rate">
                                        </div>
                                        <button style="color: #c0c0c0 ; margin-left: 15px;" onclick="delComment(${data.comment.id} , this)">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-trash2" viewBox="0 0 16 16">
                                                <path d="M14 3a.7.7 0 0 1-.037.225l-1.684 10.104A2 2 0 0 1 10.305 15H5.694a2 2 0 0 1-1.973-1.671L2.037 3.225A.7.7 0 0 1 2 3c0-1.105 2.686-2 6-2s6 .895 6 2M3.215 4.207l1.493 8.957a1 1 0 0 0 .986.836h4.612a1 1 0 0 0 .986-.836l1.493-8.957C11.69 4.689 9.954 5 8 5s-3.69-.311-4.785-.793"/>
                                              </svg>
                                            </button>
                                    
                                    </div>
                            ` 
                        };
                        ul.insertBefore(newLi , ul.firstChild) ;
                        contentArea.classList.remove('comments__form')
                        contentArea.innerHTML = ''
                        len_comments = document.getElementById('len_comments') ;
                        len_comments.innerHTML = Number(len_comments.innerHTML) + 1 ; 
                        const notifcation = document.getElementById('notification2') ;
                        notifcation.classList.add('show') ;
                        setTimeout(() => {
                        notifcation.classList.remove('show') ;
                        } , 7000 ) ;                 
                    } ;
                } else {
                    console.error('Error saving data:', data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        } , {once : true}
        
    ) };
const commentsForm = document.querySelector('.comments__form')
commentsForm.addEventListener('submit' ,
    function(event){
        event.preventDefault() ;
        const input = document.getElementById('comment_input') ;
        const commentContent = input.value ;
        const slug = commentsForm.getAttribute('data-slug') ;
        const baseUrl = window.location.origin ;
        const url = `${baseUrl}/comments/adding-comment/${slug}`;   
        fetch(url, {
            method: 'POST' ,
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            } ,
            body : JSON.stringify({content : commentContent})
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Network response was not ok: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.status === 'success') {
                if (data.has_content){
                    const ul = document.getElementById('comments_list_') ;
                    const newLi = document.createElement('li') ;
                    newLi.setAttribute('class' , 'comments__item') ;
                    if (data.is_comment_user_admin){
                    newLi.innerHTML = `
                        <div class="comments__autor">
                                        <img class="comments__avatar" src="/static/img/admin.jpg" alt="">
                                        <span style = "color: #B3FF80; "class="comments__name"><b>${data.comment_user_name}</b></span>
                                        <span class="comments__time">${data.comment_time} , ${data.comment_date}</span>
                                    </div>
                                    <p class="comments__text">${data.comment.content}</p>
                                    <div class="comments__actions">
                                        <div class="comments__rate">
    
                                        </div>
                                        <button style="color: #c0c0c0 ; margin-left: 15px;" onclick="delComment(${data.comment.id} , this)">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-trash2" viewBox="0 0 16 16">
                                            <path d="M14 3a.7.7 0 0 1-.037.225l-1.684 10.104A2 2 0 0 1 10.305 15H5.694a2 2 0 0 1-1.973-1.671L2.037 3.225A.7.7 0 0 1 2 3c0-1.105 2.686-2 6-2s6 .895 6 2M3.215 4.207l1.493 8.957a1 1 0 0 0 .986.836h4.612a1 1 0 0 0 .986-.836l1.493-8.957C11.69 4.689 9.954 5 8 5s-3.69-.311-4.785-.793"/>
                                          </svg>
                                        </button>
                                        <button onclick="showReplayForm(this)" style="margin-right: 10px;" type="button"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M21.707,11.293l-8-8A.99991.99991,0,0,0,12,4V7.54492A11.01525,11.01525,0,0,0,2,18.5V20a1,1,0,0,0,1.78418.62061,11.45625,11.45625,0,0,1,7.88672-4.04932c.0498-.00635.1748-.01611.3291-.02588V20a.99991.99991,0,0,0,1.707.707l8-8A.99962.99962,0,0,0,21.707,11.293ZM14,17.58594V15.5a.99974.99974,0,0,0-1-1c-.25488,0-1.2959.04932-1.56152.085A14.00507,14.00507,0,0,0,4.05176,17.5332,9.01266,9.01266,0,0,1,13,9.5a.99974.99974,0,0,0,1-1V6.41406L19.58594,12Z"/></svg><span>پاسخ</span></button>
                                    </div>
                    `  } else {
                        newLi.innerHTML = `
                                            <div class="comments__autor">      
                                        <img class="comments__avatar" src="/static/img/avatar.svg" alt="">
                                        <span class="comments__name">${data.comment_user_name}</span>
                                        <span class="comments__time">${data.comment_time} , ${data.comment_date}</span>
                                    </div>
                                    <p class="comments__text">${data.comment.content}</p>
                                    <div class="comments__actions">
                                        <div class="comments__rate">
    
                                        </div>
                                    <button style="color: #c0c0c0 ; margin-left: 15px;" onclick="delComment(${data.comment.id} , this)">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-trash2" viewBox="0 0 16 16">
                                            <path d="M14 3a.7.7 0 0 1-.037.225l-1.684 10.104A2 2 0 0 1 10.305 15H5.694a2 2 0 0 1-1.973-1.671L2.037 3.225A.7.7 0 0 1 2 3c0-1.105 2.686-2 6-2s6 .895 6 2M3.215 4.207l1.493 8.957a1 1 0 0 0 .986.836h4.612a1 1 0 0 0 .986-.836l1.493-8.957C11.69 4.689 9.954 5 8 5s-3.69-.311-4.785-.793"/>
                                          </svg>
                                        </button>
                                        <button onclick="showReplayForm(this)" style="margin-right: 10px;" type="button"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M21.707,11.293l-8-8A.99991.99991,0,0,0,12,4V7.54492A11.01525,11.01525,0,0,0,2,18.5V20a1,1,0,0,0,1.78418.62061,11.45625,11.45625,0,0,1,7.88672-4.04932c.0498-.00635.1748-.01611.3291-.02588V20a.99991.99991,0,0,0,1.707.707l8-8A.99962.99962,0,0,0,21.707,11.293ZM14,17.58594V15.5a.99974.99974,0,0,0-1-1c-.25488,0-1.2959.04932-1.56152.085A14.00507,14.00507,0,0,0,4.05176,17.5332,9.01266,9.01266,0,0,1,13,9.5a.99974.99974,0,0,0,1-1V6.41406L19.58594,12Z"/></svg><span>پاسخ</span></button>
                                    </div>
                        ` 
                    };
                    ul.insertBefore(newLi , ul.firstChild) ;              
                    input.value = '' ;
                    len_comments = document.getElementById('len_comments') ;
                    len_comments.innerHTML = Number(len_comments.innerHTML) + 1 ; 
                    newLi.insertAdjacentHTML('afterend' , `<form data-id = "${data.comment.id}" class = "replies__form" method = "post" action="{% url 'comments:adding_reply' id=comment.id %}"></form><div id="replies"></div>`) ;
                    const notifcation = document.getElementById('notification2') ;
                    notifcation.classList.add('show') ;
                    setTimeout(() => {
                    notifcation.classList.remove('show') ;
                    } , 7000 ) ; 
                } ;
            } else {
                console.error('Error saving data:', data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
    
) ;
function delComment(id , button) {
    const baseUrl = window.location.origin ;
    const url = `${baseUrl}/comments/delete-comment/${id}`;
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
            const li = button.closest('li') ;
            if (data.len_replies !== 0){
                li.nextElementSibling.nextElementSibling.remove() ;
            } ;
            if (data.is_a_reply === false){
                li.nextElementSibling.remove() 
            }
            li.classList.replace('comments__item' , 'comments__form') ;
            li.remove() ;
            const notifcation = document.getElementById('notification1') ;
            notifcation.classList.add('show') ;
            setTimeout(() => {
                notifcation.classList.remove('show') ;
            } , 7000 ) ;
            len_comments = document.getElementById('len_comments') ;
            amount_of_remove = 1 + data.len_replies ;
            len_comments.innerHTML = Number(len_comments.innerHTML) - amount_of_remove ; 
        } else {
            console.error('Error saving data:', data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
} ;
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
} ;
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
} ;
