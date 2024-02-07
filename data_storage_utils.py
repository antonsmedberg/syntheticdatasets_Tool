import pandas as pd
from synthetic_data_generator import SyntheticDataGenerator
from typing import Optional
from tkinter import filedialog
import logging

logger = logging.getLogger(__name__)


def ask_save_location() -> Optional[str]:
    """Ask user to select save location for the generated dataset."""
    filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    return filename if filename else None  # Return None if the user cancels the dialog


def generate_and_save_data(n_samples: int, n_features: int, task: str, noise_level: float,
                           filename: str = 'generated_data') -> str:
    """
    Generate synthetic data based on provided parameters and save it to a CSV file.

    Args:
        n_samples (int): Number of samples to generate.
        n_features (int): Number of features per sample.
        task (str): Type of task for the generated data (classification, regression, clustering).
        noise_level (float): Level of noise to add to the generated data.
        filename (str, optional): Name of the output CSV file. Defaults to 'generated_data'.

    Returns:
        str: Message indicating the status of the operation.
    """
    try:
        generator = SyntheticDataGenerator(n_samples=n_samples, n_features=n_features,
                                           task=task, noise_level=noise_level)
        X, y = generator.generate_data()

        data = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
        if y is not None:
            data['target'] = y

        data.to_csv(f'{filename}.csv', index=False)
        return f"Dataset saved as {filename}.csv"
    except Exception as e:
        logger.exception("Error occurred during data generation and saving.")
        return f"Error occurred: {str(e)}"


def main():
    """Main function."""
    print("Welcome to the Synthetic Data Generator!")
    print("Please provide the following information to generate synthetic data.")

    try:
        n_samples = int(input("Enter the number of samples: "))
        n_features = int(input("Enter the number of features: "))
        task = input("Enter the type of task (classification, regression, clustering): ")
        noise_level = float(input("Enter the noise level: "))

        message = generate_and_save_data(n_samples, n_features, task, noise_level)
        print(message)
    except ValueError:
        print("Error: Please enter valid numerical values.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()


