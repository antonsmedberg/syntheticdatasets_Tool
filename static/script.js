// script.static

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const numSamples = document.getElementById("numSamples").value;
        const numFeatures = document.getElementById("numFeatures").value;
        const task = document.getElementById("task").value;

        if (!validateInputs(numSamples, numFeatures)) {
            displayResult("Please enter valid values for number of samples and features.");
            return;
        }

        try {
            displayLoading(true);

            const response = await generateData(numSamples, numFeatures, task);

            if (response.success) {
                displayResult(response.message);
            } else {
                displayResult("Error: " + response.error);
            }
        } catch (error) {
            console.error('Error:', error);
            displayResult("An error occurred while processing the request. Please try again later.");
        } finally {
            displayLoading(false);
        }
    });

    function validateInputs(numSamples, numFeatures) {
        return numSamples > 0 && numFeatures > 0 && numSamples <= 10000 && numFeatures <= 1000;
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

    function displayResult(message) {
        resultDiv.innerText = message;
    }

    function displayLoading(isLoading) {
        const generateButton = document.getElementById("generateButton");
        generateButton.disabled = isLoading;
        generateButton.innerText = isLoading ? "Generating..." : "Generate Dataset";
    }
});






