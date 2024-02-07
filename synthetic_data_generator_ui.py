import tkinter as tk
from tkinter import ttk, messagebox, Label
import threading
from data_storage_utils import generate_and_save_data


def on_complete(success_message="Dataset generation complete!"):
    messagebox.showinfo("Success", success_message)


class SyntheticDataGeneratorUI:
    def __init__(self, root_window):
        self.task = ""
        self.n_features = 0
        self.n_samples = 0
        self.progress_bar = None
        self.generate_button = None
        self.task_dropdown = None
        self.task_var = None
        self.features_entry = None
        self.samples_entry = None
        self.root_window = root_window
        self.root_window.title("Synthetic Data Generator")
        self.create_widgets()

    def create_widgets(self):
        self.root_window.configure(bg="white")
        style = ttk.Style()
        style.theme_use('clam')
        self.root_window.grid_columnconfigure(1, weight=1)

        Label(self.root_window, text="Generate Synthetic Datasets", font=("Helvetica", 16)).grid(
            row=0, column=0, columnspan=2, pady=10)
        Label(self.root_window, text="Number of samples:").grid(row=1, column=0, sticky="e")
        self.samples_entry = ttk.Entry(self.root_window)
        self.samples_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        Label(self.root_window, text="Number of features:").grid(row=2, column=0, sticky="e")
        self.features_entry = ttk.Entry(self.root_window)
        self.features_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        Label(self.root_window, text="Task:").grid(row=3, column=0, sticky="e")
        self.task_var = tk.StringVar(self.root_window)
        task_values = ["Classification", "Regression", "Clustering"]
        self.task_dropdown = ttk.Combobox(self.root_window, textvariable=self.task_var, values=task_values)
        self.task_dropdown.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
        self.generate_button = ttk.Button(self.root_window, text="Generate Dataset", command=self.generate_dataset)
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=15)
        self.progress_bar = ttk.Progressbar(self.root_window, orient='horizontal', mode='indeterminate')
        self.progress_bar.grid(row=5, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

    def validate_inputs(self):
        try:
            self.n_samples = int(self.samples_entry.get())
            self.n_features = int(self.features_entry.get())
            self.task = self.task_var.get().lower()
            if self.task not in ['regression', 'classification', 'clustering']:
                raise ValueError("Invalid task selected.")
            if self.n_samples <= 0 or self.n_features <= 0:
                raise ValueError("Number of samples and features must be positive.")
            return True
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))
            return False

    def generate_dataset(self):
        if self.validate_inputs():
            self.progress_bar.start()
            threading.Thread(target=self.call_main_logic).start()

    def call_main_logic(self):
        try:
            message = generate_and_save_data(self.n_samples, self.n_features, self.task, noise_level=0.1)
            self.root_window.after(0, on_complete, message)
        except Exception as e:
            self.root_window.after(0, messagebox.showerror, "Error", str(e))
        finally:
            self.progress_bar.stop()


if __name__ == "__main__":
    root = tk.Tk()
    app = SyntheticDataGeneratorUI(root)
    root.mainloop()
