// Set current year
const year = document.querySelector(".year");
const currentYear = new Date().getFullYear();
year.textContent = currentYear;


const btnNav = document.querySelector('.btn-mobile-nav');
const header = document.querySelector('.header');

btnNav.addEventListener('click', function(){
    header.classList.toggle('nav-open');
})