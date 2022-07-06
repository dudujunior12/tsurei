var swiper1 = new Swiper(".swiper1", {
    slidesPerView: 5,
    slidesPerGroup: 5,
    spaceBetween: 50,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});

var swiper2 = new Swiper(".swiper2", {
    slidesPerView: 5,
    slidesPerGroup: 5,
    spaceBetween: 50,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});

document.addEventListener("DOMContentLoaded", function(){
    document.querySelector('.btn-follow').onclick = function(){
        fetch(window.location.pathname + '/follow', {
            method: "POST",
            body: JSON.stringify({
                "follow": this.innerHTML
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if(data['follow'] == "Follow"){
                this.innerHTML = data['follow'];
            }
            else{
                this.innerHTML = data['follow'];
            }
        })
        .catch(error => {
            console.log("Error: " + error);
        })
    };
});