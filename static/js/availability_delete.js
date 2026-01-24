const deleteSlot = document.getElementById("delete-slot");
const modalDeleteAvailability = document.getElementById("modalDeleteAvailability");
const modalDelete= new bootstrap.Modal(modalDeleteAvailability);
const confirmDelete = document.getElementById("availability-delete-confirm");

/**
* Initializes delete functionality for availability slot.
* 
* - Retrieves the slot Id from delete button on click.
* - Dynamically generates URL for that slot 
* - Updates href of modal confirmation button to generated url
* - Opens the Modal
*/

deleteSlot.addEventListener("click", (e) => {
    const slotId = deleteSlot.dataset.slotId;
    confirmDelete.href = `/delete-availability/${slotId}`;
    modalDelete.show();
  });
