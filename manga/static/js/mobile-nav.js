// Set current year
const yearEl = document.querySelector(".year");
console.log(yearEl);
const currentYear = new Date().getFullYear();
yearEl.textContent = currentYear;
