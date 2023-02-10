function enableFieldset(fieldsetId) {
    var fieldset = document.getElementById(fieldsetId);
    fieldset.removeAttribute("disabled");
}

document.querySelector("form").addEventListener("submit", function(event) {
    console.log("Form submit event triggered");
    event.preventDefault();
  });
  