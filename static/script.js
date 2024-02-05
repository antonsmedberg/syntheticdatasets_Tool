// script.static

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const generateButton = document.getElementById("generateButton");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        // Perform form validation (e.g., check if input fields are not empty)
        const numSamples = document.getElementById("numSamples").value;
        const numFeatures = document.getElementById("numFeatures").value;
        const task = document.getElementById("task").value;

        // You can add more validation logic here

        // If validation passes, submit data to the server
        // Update the DOM with results or display error messages
    });
});

