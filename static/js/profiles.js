const editButtons = document.getElementsByClassName("btn-edit");
const profileName = document.getElementById("id_name");
const profileExcerpt = document.getElementById("id_excerpt");
const profileBio = document.getElementById("id_bio");
const profileExperience = document.getElementById("id_experience");
const profileSpecialism = document.getElementById("id_specialism");
const profileForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let profileId = e.target.getAttribute("data-profile_id");
    let profileContent = document.getElementById(`profile${profileId}`).innerText;
    profileText.value = profileContent;
    submitButton.innerText = "Update";
    profileForm.setAttribute("action", `edit_profile/${profileId}`);
  });
}