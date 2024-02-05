import tkinter as tk
from tkinter import messagebox
from synthetic_data_generator_ui import SyntheticDataGeneratorUI


def main():
    try:
        root = tk.Tk()
        app = SyntheticDataGeneratorUI(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
