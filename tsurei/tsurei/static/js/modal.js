document.addEventListener("DOMContentLoaded", function () {
    // Get the modal
    if (document.getElementById("new-chapter-modal") != null) {
        var modal = document.getElementById("new-chapter-modal");
    }

    // Get the button that opens the modal
    if (document.getElementById("btn-new-chapter") != null) {
        var btn = document.getElementById("btn-new-chapter");
    }
    console.log(modal);

    // Get the <span> element that closes the modal
    if (document.getElementsByClassName("close")[0]) {
        var span = document.getElementsByClassName("close")[0];
    }

    if (btn != null) {
        // When the user clicks on the button, open the modal
        btn.onclick = function () {
            modal.style.display = "block";
        };

        // When the user clicks on <span> (x), close the modal
        span.onclick = function () {
            modal.style.display = "none";
        };

        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function (event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        };
    }
});
