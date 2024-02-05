# synthetic_data_generator_ui.py
import tkinter as tk
from tkinter import ttk, messagebox
import threading
from main import main_logic  # Import the main logic function


class SyntheticDataGeneratorUI:
    def __init__(self, root):
        self.samples_entry = None
        self.features_entry = None
        self.task_var = None
        self.task_dropdown = None
        self.generate_button = None
        self.progress_bar = None
        self.root = root
        self.root.title("Synthetic Data Generator")
        self.create_widgets()

    def create_widgets(self):
        # Styling
        self.root.configure(bg="white")
        style = ttk.Style()
        style.theme_use('clam')

        # Grid configuration
        self.root.grid_columnconfigure(1, weight=1)

        # Number of samples
        ttk.Label(self.root, text="Number of samples:").grid(row=0, column=0, sticky="e")
        self.samples_entry = ttk.Entry(self.root)
        self.samples_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Number of features
        ttk.Label(self.root, text="Number of features:").grid(row=1, column=0, sticky="e")
        self.features_entry = ttk.Entry(self.root)
        self.features_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # Task type
        ttk.Label(self.root, text="Task (regression, classification, clustering):").grid(row=2, column=0,
                                                                                         sticky="e")
        self.task_var = tk.StringVar(self.root)
        self.task_var.set("regression")  # Default value
        self.task_dropdown = ttk.Combobox(self.root, textvariable=self.task_var,
                                          values=["regression", "classification", "clustering"])
        self.task_dropdown.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        # Generate button
        self.generate_button = ttk.Button(self.root, text="Generate Dataset", command=self.generate_dataset)
        self.generate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Progress Bar
        self.progress_bar = ttk.Progressbar(self.root, orient='horizontal', mode='indeterminate')
        self.progress_bar.grid(row=4, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

    def generate_dataset(self):
        n_samples = self.samples_entry.get()
        n_features = self.features_entry.get()
        task = self.task_var.get()

        # Validate input
        if not n_samples.isdigit() or not n_features.isdigit():
            messagebox.showerror("Error", "Please enter valid integers for the number of samples and features.")
            return

        # Start progress bar and generate dataset in a separate thread
        self.progress_bar.start()
        threading.Thread(target=self.call_main_logic, args=(int(n_samples), int(n_features), task)).start()

    def call_main_logic(self, n_samples, n_features, task):
        try:
            main_logic(n_samples, n_features, task)
            self.on_complete()
        except Exception as e:
            self.progress_bar.stop()
            messagebox.showerror("Error", str(e))

    def on_complete(self):
        self.progress_bar.stop()
        messagebox.showinfo("Success", "Dataset generation complete!")
        self.root.deiconify()  # Show the main window
