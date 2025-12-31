
document.addEventListener('DOMContentLoaded', function () {
    //warning for application deletion 
    const deleteForm = document.querySelectorAll('.delete-form');
    deleteForm.forEach(function (form) {
        form.addEventListener('submit', function (event) {
            const confirmed = confirm("Are you sure you want to delete this application?");
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });

    //toggle read more for notes
    document.querySelectorAll('.toggle-notes').forEach(button => {
        button.addEventListener('click', function () {
            const cardBody = this.closest('.card-body');
            const shortNotes = cardBody.querySelector('.notes-short');
            const fullNotes = cardBody.querySelector('.notes-full');

            const isHidden = fullNotes.classList.contains('d-none');

            shortNotes.classList.toggle('d-none');
            fullNotes.classList.toggle('d-none');

            this.textContent = isHidden
                ? 'Show less'
                : 'Show more';
        });
    });
});