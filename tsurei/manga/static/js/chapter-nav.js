document.addEventListener('DOMContentLoaded',function() {
    document.querySelector('select[select-option]').onchange=changeEventHandler;
},false);

function changeEventHandler(event) {
    let value = this.options[this.selectedIndex].value;
    let match = value.match(/^\d+$/);
    if (match) {
        window.location.href = encodeURIComponent(match[0]);
    } else {
        console.error('Invalid value selected');
    }
}