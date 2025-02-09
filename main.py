import pandas as pd

# Exemple : Fusion de deux tables avec des jointures et opérations
table1 = pd.DataFrame({
    "Nom": ["Alice", "Bob", "Charlie"],
    "Score": [85, 90, 78]
})

table2 = pd.DataFrame({
    "Nom": ["Bob", "Charlie", "David"],
    "Score2": [88, 82, 95]
})

# Effectuer une jointure
fusion_table = pd.merge(table1, table2, on="Nom", how="outer")

# Remplace les NaN par 0 avant la somme
fusion_table[["Score", "Score2"]] = fusion_table[["Score", "Score2"]].fillna(0)

# Recalcule le total
fusion_table["Total"] = fusion_table["Score"] + fusion_table["Score2"]

print(fusion_table)


# Exporter le résultat
fusion_table.to_csv("Fusion_Tables.csv", sep=";", encoding="utf-8", index=False)
