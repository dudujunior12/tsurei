var search_box = document.querySelector(".search-box");

addFunctionEvent();

function addFunctionEvent() {
    for (var child of search_box.children) {
        if (child.tagName != "INPUT") {
            var input = document.createElement("input");
            input.className = "input";
            input.type = "text";
            search_box.appendChild(input);
        }
        if (search_box.childElementCount == 2) {
            if (child.tagName == "BUTTON") {
                child.addEventListener("click", function () {
                    toggleBF();
                });
            }
        }
    }
}

function toggleBF() {
    for (var child of search_box.children) {
        console.log(child);
        if (child.tagName == "BUTTON") {
            var btn = child;
            btn.classList.toggle("is-close");
        }

        if (child.tagName == "INPUT") {
            var input = child;
            input.classList.toggle("is-clicked");
        }
    }
}
