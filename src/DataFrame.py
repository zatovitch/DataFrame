import pandas as pd

# Créer un DataFrame
data = {
    "Nom": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack"],
    "Âge": [25, 30, 35, 40, 28, 33, 38, 45, 50, 55],
    "Salaire": [50000, 60000, 70000, 80000, 55000, 65000, 75000, 85000, 90000, 95000]
}
df = pd.DataFrame(data)

# Afficher le DataFrame
print(df)

# Calculer la moyenne des salaires
print("Salaire moyen:", df["Salaire"].mean())

# Trouver le salaire max
print("Salaire max:", df["Salaire"].max())
print("Salaire max:", df["Salaire"].min())

