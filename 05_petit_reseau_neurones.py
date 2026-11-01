# Étape 5 : Création du petit réseau de neurones (le mix)
# Le réservoir reste fixe, ce petit réseau apprend à le lire

import numpy as np

# --- Paramètres ---
taille_reservoir = 50
nombre_caracteres = 12
taille_cachee = 32          # Taille de la couche cachée du petit réseau

np.random.seed(42)

# --- Poids du petit réseau de neurones ---
# Couche 1 : du réservoir vers la couche cachée
poids_1 = np.random.randn(taille_cachee, taille_reservoir) * 0.1
biais_1 = np.zeros(taille_cachee)

# Couche 2 : de la couche cachée vers les caractères (sortie)
poids_2 = np.random.randn(nombre_caracteres, taille_cachee) * 0.1
biais_2 = np.zeros(nombre_caracteres)

print("Petit réseau de neurones créé avec succès !")
print("Couche cachée :", taille_cachee, "neurones")
print("Forme poids_1 (réservoir → cachée) :", poids_1.shape)
print("Forme poids_2 (cachée → caractères) :", poids_2.shape)
print("\nC'est CE réseau qu'on va entraîner.")
print("Le réservoir, lui, reste complètement fixe.")
