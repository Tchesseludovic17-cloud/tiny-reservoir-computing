# Étape 3 : Création du réservoir (version très simple)
# On crée un petit réservoir aléatoire et on ne le modifiera plus jamais

import numpy as np

# --- Paramètres très simples ---
taille_reservoir = 50          # Nombre de neurones dans le réservoir (tout petit)
nombre_caracteres = 12         # On a 12 caractères différents (d'après l'étape précédente)

# --- Création des poids d'entrée (aléatoires) ---
# Ces poids relient les caractères au réservoir
np.random.seed(42)  # Pour avoir toujours les mêmes nombres aléatoires (reproductible)
poids_entree = np.random.randn(taille_reservoir, nombre_caracteres) * 0.5

# --- Création des poids internes du réservoir (aléatoires) ---
# Ce sont les connexions entre les neurones du réservoir
poids_reservoir = np.random.randn(taille_reservoir, taille_reservoir) * 0.1

print("Réservoir créé avec succès !")
print("Taille du réservoir :", taille_reservoir)
print("Forme des poids d'entrée :", poids_entree.shape)
print("Forme des poids internes :", poids_reservoir.shape)
print("\nOn ne touchera plus jamais à ces poids. Ils restent fixes.")
