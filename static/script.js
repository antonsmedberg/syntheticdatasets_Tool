document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("dataForm");
    const numSamplesInput = document.getElementById("numSamples");
    const numFeaturesInput = document.getElementById("numFeatures");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const numSamples = parseInt(numSamplesInput.value);
        const numFeatures = parseInt(numFeaturesInput.value);
        const task = document.getElementById("task").value;

        if (!validateInputs(numSamples, numFeatures)) {
            displayError("Please enter valid values for number of samples and features.");
            return;
        }

        try {
            displayLoading(true);

            const response = await generateData(numSamples, numFeatures, task);

            if (response.success) {
                displaySuccess(response.message);
                downloadDataset(response.data);
            } else {
                displayError("Error: " + response.error);
            }
        } catch (error) {
            console.error('Error:', error);
            displayError("An error occurred while processing the request. Please try again later.");
        } finally {
            displayLoading(false);
        }
    });

    numSamplesInput.addEventListener("input", function () {
        if (!validateInputValue(numSamplesInput)) {
            numSamplesInput.classList.add("error");
            document.getElementById("numSamplesError").style.display = "block";
        } else {
            numSamplesInput.classList.remove("error");
            document.getElementById("numSamplesError").style.display = "none";
        }
    });

    numFeaturesInput.addEventListener("input", function () {
        if (!validateInputValue(numFeaturesInput)) {
            numFeaturesInput.classList.add("error");
            document.getElementById("numFeaturesError").style.display = "block";
        } else {
            numFeaturesInput.classList.remove("error");
            document.getElementById("numFeaturesError").style.display = "none";
        }
    });

    function validateInputs(numSamples, numFeatures) {
        return numSamples > 0 && numFeatures > 0 && numSamples <= 10000 && numFeatures <= 1000;
    }

    function validateInputValue(input) {
        const value = parseInt(input.value);
        return !isNaN(value) && value > 0;
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
});










