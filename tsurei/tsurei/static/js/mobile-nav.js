const header = document.querySelector('.header');

const btnNav = document.querySelector('.btn-mobile-nav')
btnNav.addEventListener('click', function(){
    header.classList.toggle('nav-open');
})