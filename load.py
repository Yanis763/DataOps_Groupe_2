import pandas as pd

file_path = "data.csv"

try:
    data = pd.read_csv(file_path)
    print(data.head())
except FileNotFoundError:
    print(f"Erreur : Le fichier '{file_path}' est introuvable.")
except pd.errors.EmptyDataError:
    print("Erreur : Le fichier est vide.")