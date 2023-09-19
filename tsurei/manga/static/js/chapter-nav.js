document.addEventListener('DOMContentLoaded',function() {
    document.querySelector('select[select-option]').onchange=changeEventHandler;
},false);

function changeEventHandler(event) {
    value = this.options[this.selectedIndex].value;
    value = value.match(/\d+/g);
    window.location.href = value[0];
}