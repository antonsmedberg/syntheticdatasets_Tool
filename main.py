from tkinter import simpledialog, messagebox
import pandas as pd
from synthetic_data_generator import SyntheticDataGenerator


def main_logic(n_samples, n_features, task):
    try:
        # Skapa en instans av SyntheticDataGenerator med angivna parametrar
        generator = SyntheticDataGenerator(n_samples, n_features, task)
        # Generera data
        X, y = generator.generate_data()

        # Skapa en DataFrame från genererade data
        data = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
        # Lägg till målvariabeln om den finns
        if y is not None:
            data['target'] = y

        # Fråga användaren efter ett filnamn för att spara datasetet
        filename = simpledialog.askstring("Save As", "Enter the filename to save the dataset:")
        # Spara datasetet till en CSV-fil
        if filename:
            data.to_csv(filename + '.csv', index=False)
            messagebox.showinfo("Success", f"Dataset saved as {filename}.csv")
    except Exception as e:
        # Visa felmeddelande om något går fel
        messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    # Detta anropas när scriptet körs direkt
    pass
