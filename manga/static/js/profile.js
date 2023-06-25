var swiper1 = new Swiper(".swiper1", {
    slidesPerView: 5,
    slidesPerGroup: 5,
    spaceBetween: 10,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});

if ("matchMedia" in window) {
    if (window.matchMedia("(max-width: 46em)").matches) {
        swiper1.params.slidesPerView = 3;
        swiper1.params.slidesPerGroup = 3;
        swiper1.params.spaceBetween = 10;
    } 

    else{
        swiper1.params.slidesPerView = 5;
        swiper1.params.slidesPerGroup = 5;
        swiper1.params.spaceBetween = 10;
    }
}