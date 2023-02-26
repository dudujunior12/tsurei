document.addEventListener("DOMContentLoaded", function () {
    let manga_id = document.querySelector(".manga-view-info").dataset.id;
    // Bookmark
    if (document.querySelector(".btn-bookmark") != null) {
        document.querySelector(".btn-bookmark").onclick = function () {
            fetch("/manga/" + manga_id + "/add-bookmark", {
                method: "POST",
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    bookmark = document.querySelector(".btn-bookmark");
                    if (data.bookmarked == true) {
                        console.log(bookmark);
                        bookmark.innerHTML = "Bookmarked";
                    } else {
                        bookmark.innerHTML = "Bookmark";
                    }
                })
                .catch((error) => {
                    console.log("Bookmark error: " + error);
                });
        };
    }

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
