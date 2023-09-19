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
});
