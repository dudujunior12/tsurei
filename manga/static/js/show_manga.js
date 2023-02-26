document.addEventListener("DOMContentLoaded", function () {
    // Bookmark
    if (document.querySelector(".btn-bookmark") != null) {
        document.querySelector(".btn-bookmark").onclick = function () {
            fetch("/manga/" + manga_id + "/add-bookmark", {
                method: "POST",
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    bookmark_text = document.querySelector(".bookmark-text");
                    if (data.bookmarked == true) {
                        bookmark_text.innerHTML = "Bookmarked";
                    } else {
                        bookmark_text.innerHTML = "Bookmark";
                    }
                })
                .catch((error) => {
                    console.log("Error: " + error);
                });
        };
    }

    // Edit comment
    // Button edit on click opens edit form
    if (document.querySelector(".manga-info") != null) {
        let manga_id = document.querySelector(".manga-info").dataset.id;

        document.querySelectorAll("#btn-edit").forEach((button) => {
            button.onclick = function () {
                console.log(this.dataset.id);
                let form_edit = document.querySelector(
                    "#form_edit_" + this.dataset.id
                );
                form_edit.style.display = "block";
                let comment = document.querySelector(
                    "#comment_" + this.dataset.id
                );
                comment.style.display = "none";
            };
        });
    }

    // Update comment and displays it
    if (document.querySelectorAll(".form-edit") != null) {
        document.querySelectorAll(".form-edit").forEach((form) => {
            form.onsubmit = function (event) {
                event.preventDefault();

                fetch(
                    "/manga/" + manga_id + "/edit-comment/" + this.dataset.id,
                    {
                        method: "POST",
                        body: JSON.stringify({
                            comment_text: document.querySelector(
                                "#txtarea_edit_" + this.dataset.id
                            ).value,
                        }),
                    }
                )
                    .then((response) => response.json())
                    .then((data) => {
                        this.style.display = "none";
                        let comment = document.querySelector(
                            "#comment_" + this.dataset.id
                        );
                        comment.style.display = "block";
                        comment.innerHTML = data.comment_text;
                    })
                    .catch((error) => {
                        console.log("Error: ", error);
                    });

                return false;
            };
        });
    }

    // Like
    if (document.querySelectorAll(".btn-like") != null) {
        document.querySelectorAll(".btn-like").forEach((button) => {
            button.onclick = function () {
                fetch(
                    "/manga/" + manga_id + "/like-comment/" + this.dataset.id,
                    {
                        method: "POST",
                    }
                )
                    .then((response) => response.json())
                    .then((data) => {
                        if (data.liked == true) {
                            this.style.fill = "red";
                        } else {
                            this.style.fill = "grey";
                        }
                    })
                    .catch((error) => {
                        console.log("Error: " + error);
                    });
            };
        });
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
