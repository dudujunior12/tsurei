document.addEventListener("DOMContentLoaded", function(){
// Edit comment
    // Button edit on click opens edit form
    let manga_id = document.querySelector('.manga-info').dataset.id;
    document.querySelectorAll('#btn-edit').forEach(button => {
        button.onclick = function(){
            console.log(this.dataset.id);
            let form_edit = document.querySelector('#form_edit_' + this.dataset.id );
            form_edit.style.display = "block";
            let comment = document.querySelector('#comment_' + this.dataset.id);
            comment.style.display = "none";
        }
    });

    // Update comment and displays it
    document.querySelectorAll('.form-edit').forEach(form => {
        form.onsubmit = function(event){
            event.preventDefault();
            
            fetch("/manga/" + manga_id + '/edit-comment/' + this.dataset.id, {
                method: "POST",
                body: JSON.stringify({
                    comment_text: document.querySelector('#txtarea_edit_' + this.dataset.id).value,
                })
            })
            .then(response => response.json())
            .then(data => {
                this.style.display = "none";
                let comment = document.querySelector('#comment_' + this.dataset.id);
                comment.style.display = "block";
                comment.innerHTML = data.comment_text;
            })
            .catch(error => {
                console.log("Error: ", error);
            });

            return false;
        }
    })

// Like
});