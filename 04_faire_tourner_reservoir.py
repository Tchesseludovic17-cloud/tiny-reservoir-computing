# Étape 4 : Faire tourner le réservoir et préparer les données
# Version Mix : Réservoir fixe + on prépare les états pour un petit réseau de neurones

import numpy as np

# --- Données ---
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

caracteres = sorted(list(set(texte)))
nombre_caracteres = len(caracteres)
char_vers_num = {car: i for i, car in enumerate(caracteres)}

# --- Paramètres du réservoir ---
taille_reservoir = 50
np.random.seed(42)

poids_entree = np.random.randn(taille_reservoir, nombre_caracteres) * 0.5
poids_reservoir = np.random.randn(taille_reservoir, taille_reservoir) * 0.1

# --- Fonction pour faire tourner le réservoir ---
def faire_tourner_reservoir(texte, poids_entree, poids_reservoir):
    etats = []
    etat = np.zeros(taille_reservoir)  # état de départ (tout à zéro)
    
    for car in texte:
        # Convertir le caractère en vecteur (one-hot simple)
        vecteur = np.zeros(nombre_caracteres)
        vecteur[char_vers_num[car]] = 1.0
        
        # Mise à jour de l'état du réservoir
        etat = np.tanh(poids_entree @ vecteur + poids_reservoir @ etat)
        etats.append(etat.copy())
    
    return np.array(etats)

# --- Exécution ---
etats_reservoir = faire_tourner_reservoir(texte, poids_entree, poids_reservoir)

print("Réservoir a bien tourné !")
print("Nombre d'états produits :", len(etats_reservoir))
print("Forme des états :", etats_reservoir.shape)
print("\nChaque ligne est l'état du réservoir après avoir vu un caractère.")
print("Ces états serviront d'entrée au petit réseau de neurones (le mix).")
