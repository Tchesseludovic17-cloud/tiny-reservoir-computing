# Étape 1 : Préparation des données
# Objectif : Créer un petit texte d'entraînement et lister les caractères uniques

texte = """emma
emmanuel
clara
lucas
lea
noah
chloe
louis
jade
gabriel"""

print("Texte d'entraînement :")
print(texte)

# Trouver tous les caractères uniques
caracteres = sorted(list(set(texte)))
print("\nCaractères uniques :")
print(caracteres)
print("\nNombre de caractères différents :", len(caracteres))
