var swiper1 = new Swiper(".swiper1", {
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});

var swiper2 = new Swiper(".swiper2", {
    slidesPerView: 5,
    slidesPerGroup: 5,
    spaceBetween: 30,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});



if ("matchMedia" in window) {
    if (window.matchMedia("(max-width: 46em)").matches) {
        swiper2.params.slidesPerView = 3;
        swiper2.params.slidesPerGroup = 3;
        swiper2.params.spaceBetween = 10;
    } 

    else{
        swiper2.params.slidesPerView = 5;
        swiper2.params.slidesPerGroup = 5;
        swiper2.params.spaceBetween = 30;
    }
}

swiper1.on("slideChangeTransitionEnd", function () {
    let current_manga = document.querySelector(".swiper-slide-active");
    change_manga_info(current_manga.dataset.id);
});

function change_manga_info(current_manga_id) {
    fetch("manga/get/" + current_manga_id, {
        method: "GET",
    })
        .then((response) => response.json())
        .then((data) => {
            document.querySelector(".manga-title").innerHTML =
                "<a href='manga/" +
                data.manga_id +
                "'>" +
                data.manga_title +
                "</a>";
            document.querySelector(".manga-summary").innerHTML =
                data.manga_summary;
            document.querySelector(".manga-author").innerHTML =
                "<strong>Author: </strong>" + data.manga_author;
            document.querySelector(".manga-status").innerHTML =
                "<strong>Status: </strong>" + data.manga_status;
        })
        .catch((error) => {
            console.log("Error: ", error);
        });
}

