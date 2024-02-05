# main.py
from tkinter import simpledialog, messagebox

import numpy as np
import pandas as pd
from synthetic_data_generator import SyntheticDataGenerator


def main_logic(n_samples, n_features, task):
    generator = SyntheticDataGenerator(n_samples, n_features, task)
    X, y = generator.generate_data()

    data = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
    if y is not None:
        data['target'] = y
    filename = simpledialog.askstring("Save As", "Enter the filename to save the dataset:")
    if filename:
        data.to_csv(filename + '.csv', index=False)
        messagebox.showinfo("Success", f"Dataset saved as {filename}.csv")


if __name__ == "__main__":
    # This will be called when the script is run directly
    # You can add a command-line interface or other entry points here if needed
    pass
