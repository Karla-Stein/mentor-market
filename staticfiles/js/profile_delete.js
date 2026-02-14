/* jshint esversion: 11 */
/* global bootstrap */

const deleteButton = document.getElementById("delete");
const modalDelete = document.getElementById("modalDelete");
const modal = new bootstrap.Modal(modalDelete);

deleteButton.addEventListener("click", (e) => {
        modal.show();
});

/* 
 defuse focus before hiding kicks in to fix the console warning for the modal.
 Reused from previous project.
*/
modalDelete.addEventListener("hide.bs.modal", () => {
    if (modalDelete.contains(document.activeElement)) {
        document.activeElement.blur();
    }
});
