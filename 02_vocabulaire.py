# Étape 2 : Création du vocabulaire
# On donne un numéro à chaque caractère

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

# Liste des caractères uniques (triés)
caracteres = sorted(list(set(texte)))
print("Caractères uniques :", caracteres)
print("Nombre de caractères :", len(caracteres))

# Dictionnaire caractère → numéro
char_vers_num = {car: i for i, car in enumerate(caracteres)}
print("\nDictionnaire caractère → numéro :")
print(char_vers_num)

# Dictionnaire numéro → caractère (utile plus tard pour générer du texte)
num_vers_char = {i: car for i, car in enumerate(caracteres)}
print("\nDictionnaire numéro → caractère :")
print(num_vers_char)
