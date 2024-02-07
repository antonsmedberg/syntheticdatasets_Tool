document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("dataForm");
    const numSamplesInput = document.getElementById("numSamples");
    const numFeaturesInput = document.getElementById("numFeatures");
    const resultDiv = document.getElementById("result");
    const taskSelect = document.getElementById("task");
    const taskError = document.getElementById("taskError");

    // Set focus on the first input field
    numSamplesInput.focus();

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const numSamples = parseInt(numSamplesInput.value);
        const numFeatures = parseInt(numFeaturesInput.value);
        const task = taskSelect.value;

        if (!validateInputs(numSamples, numFeatures)) {
            displayError(validateErrorMessage(numSamples, numFeatures));
            return;
        }

        if (!task) {
            taskError.classList.add("active");
            return;
        } else {
            taskError.classList.remove("active");
        }

        try {
            displayLoading(true);
            const response = await generateData(numSamples, numFeatures, task);
            handleResponse(response);
        } catch (error) {
            console.error('Error:', error);
            displayError("An error occurred while processing the request. Please try again later.");
        } finally {
            displayLoading(false);
        }
    });

    numSamplesInput.addEventListener("input", function () {
        handleInputValidation(numSamplesInput);
    });

    numFeaturesInput.addEventListener("input", function () {
        handleInputValidation(numFeaturesInput);
    });

    taskSelect.addEventListener("change", function () {
        taskError.classList.remove("active");
    });

    function handleInputValidation(input) {
        if (!validateInputValue(input)) {
            input.classList.add("error");
            document.getElementById(input.id + "Error").classList.add("active");
        } else {
            input.classList.remove("error");
            document.getElementById(input.id + "Error").classList.remove("active");
        }
    }

    function validateInputs(numSamples, numFeatures) {
        return numSamples > 0 && numFeatures > 0 && numSamples <= 10000 && numFeatures <= 1000;
    }

    function validateInputValue(input) {
        const value = parseInt(input.value);
        return !isNaN(value) && value > 0;
    }

    function validateErrorMessage(numSamples, numFeatures) {
        if (numSamples <= 0 || numFeatures <= 0) {
            return "Please enter a positive integer for both number of samples and features.";
        } else {
            if (numSamples > 10000) {
                return "The number of samples should not exceed 10,000.";
            }
            if (numFeatures > 1000) {
                return "The number of features should not exceed 1,000.";
            }
        }
    }

    async function generateData(samples, features, task) {
        const response = await fetch('/generate_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                samples,
                features,
                task
            }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        return await response.json();
    }

    function handleResponse(response) {
        if (response.success) {
            displaySuccess(response.message);
            downloadDataset(response.data);
            showConfirmation("Dataset generated successfully and downloaded.");
        } else {
            displayError("Error: " + response.error);
        }
    }

    function displaySuccess(message) {
        resultDiv.innerText = message;
        resultDiv.classList.remove('error');
    }

    function displayError(message) {
        resultDiv.innerText = message;
        resultDiv.classList.add('error');
    }

    function displayLoading(isLoading) {
        const generateButton = document.getElementById("generateButton");
        generateButton.disabled = isLoading;
        generateButton.innerText = isLoading ? "Generating..." : "Generate Dataset";
    }

    function downloadDataset(data) {
        const csvContent = "data:text/csv;charset=utf-8," + data;
        const encodedUri = encodeURI(csvContent);
        const link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", "generated_dataset.csv");
        document.body.appendChild(link);
        link.click();
    }

    function showConfirmation(message) {
        const confirmationMessage = document.getElementById("confirmation");
        confirmationMessage.innerText = message;
        confirmationMessage.classList.add("active");
        setTimeout(function () {
            confirmationMessage.classList.remove("active");
        }, 3000); // Hide after 3 seconds
    }
});














