# ui.py
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


def call_main_logic(n_samples, n_features, task):
    from main import main_logic  # Import the main logic function
    main_logic(n_samples, n_features, task)


class SyntheticDataGeneratorUI:
    def __init__(self, root):
        self.generate_button = None
        self.task_dropdown = None
        self.task_var = None
        self.features_entry = None
        self.samples_entry = None
        self.root = root
        self.root.title("Synthetic Data Generator")
        self.create_widgets()

    def create_widgets(self):
        # Number of samples
        tk.Label(self.root, text="Number of samples:").grid(row=0, column=0, sticky="e")
        self.samples_entry = tk.Entry(self.root)
        self.samples_entry.grid(row=0, column=1)

        # Number of features
        tk.Label(self.root, text="Number of features:").grid(row=1, column=0, sticky="e")
        self.features_entry = tk.Entry(self.root)
        self.features_entry.grid(row=1, column=1)

        # Task type
        tk.Label(self.root, text="Task (regression, classification, clustering):").grid(row=2, column=0, sticky="e")
        self.task_var = tk.StringVar(self.root)
        self.task_var.set("regression")  # default value
        self.task_dropdown = ttk.Combobox(self.root, textvariable=self.task_var,
                                          values=["regression", "classification", "clustering"])
        self.task_dropdown.grid(row=2, column=1)

        # Generate button
        self.generate_button = tk.Button(self.root, text="Generate Dataset", command=self.generate_dataset)
        self.generate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def generate_dataset(self):
        n_samples = self.samples_entry.get()
        n_features = self.features_entry.get()
        task = self.task_var.get()

        # Validate input
        if not n_samples.isdigit() or not n_features.isdigit():
            messagebox.showerror("Error", "Please enter valid integers for the number of samples and features.")
            return

        # Call the main logic with the provided parameters
        self.root.withdraw()  # Hide the main window
        self.root.quit()  # Close the main window
        call_main_logic(int(n_samples), int(n_features), task)


if __name__ == "__main__":
    root = tk.Tk()
    app = SyntheticDataGeneratorUI(root)
    root.mainloop()
