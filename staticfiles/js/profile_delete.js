/* jshint esversion: 11 */
/* global bootstrap */

const deleteButton = document.getElementById("delete");
const modalDelete = document.getElementById("modalDelete");
const modal = new bootstrap.Modal(modalDelete);

deleteButton.addEventListener("click", (e) => {
        modal.show();
});
