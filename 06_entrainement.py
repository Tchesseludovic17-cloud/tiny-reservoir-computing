# Étape 6 : Entraînement du petit réseau de neurones
# Mix : Réservoir fixe + petit réseau qu'on entraîne

import numpy as np

# ====================== DONNÉES ======================
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
num_vers_char = {i: car for i, car in enumerate(caracteres)}

# ====================== RÉSERVOIR (FIXE) ======================
taille_reservoir = 50
np.random.seed(42)

poids_entree = np.random.randn(taille_reservoir, nombre_caracteres) * 0.5
poids_reservoir = np.random.randn(taille_reservoir, taille_reservoir) * 0.1

def faire_tourner_reservoir(texte):
    etats = []
    etat = np.zeros(taille_reservoir)
    for car in texte:
        vecteur = np.zeros(nombre_caracteres)
        vecteur[char_vers_num[car]] = 1.0
        etat = np.tanh(poids_entree @ vecteur + poids_reservoir @ etat)
        etats.append(etat.copy())
    return np.array(etats)

etats = faire_tourner_reservoir(texte)

# ====================== PETIT RÉSEAU DE NEURONES ======================
taille_cachee = 32

# Initialisation des poids
poids_1 = np.random.randn(taille_cachee, taille_reservoir) * 0.1
biais_1 = np.zeros(taille_cachee)
poids_2 = np.random.randn(nombre_caracteres, taille_cachee) * 0.1
biais_2 = np.zeros(nombre_caracteres)

# ====================== FONCTIONS UTILES ======================
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def forward(etat):
    # Passage avant dans le petit réseau
    cachee = np.tanh(poids_1 @ etat + biais_1)
    sortie = poids_2 @ cachee + biais_2
    probabilites = softmax(sortie)
    return probabilites, cachee

# ====================== ENTRAÎNEMENT TRÈS SIMPLE ======================
taux_apprentissage = 0.01
nombre_epochs = 200

print("Début de l'entraînement...")

for epoch in range(nombre_epochs):
    perte_totale = 0
    
    for i in range(len(texte) - 1):
        # État du réservoir à ce moment
        etat = etats[i]
        
        # Caractère suivant (cible)
        cible = char_vers_num[texte[i + 1]]
        
        # Passage avant
        probabilites, cachee = forward(etat)
        
        # Calcul de la perte (cross-entropy simple)
        perte = -np.log(probabilites[cible] + 1e-8)
        perte_totale += perte
        
        # Gradient très simplifié (version pédagogique)
        d_sortie = probabilites.copy()
        d_sortie[cible] -= 1
        
        # Mise à jour couche 2
        poids_2 -= taux_apprentissage * np.outer(d_sortie, cachee)
        biais_2 -= taux_apprentissage * d_sortie
        
        # Mise à jour couche 1 (approximation simple)
        d_cachee = poids_2.T @ d_sortie * (1 - cachee**2)
        poids_1 -= taux_apprentissage * np.outer(d_cachee, etat)
        biais_1 -= taux_apprentissage * d_cachee
    
    if (epoch + 1) % 50 == 0:
        print(f"Epoch {epoch+1}/{nombre_epochs} - Perte moyenne : {perte_totale / (len(texte)-1):.4f}")

print("\nEntraînement terminé !")
print("Le petit réseau a appris à lire le réservoir.")
