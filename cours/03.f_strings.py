#  F-STRING
# Permet de convertir une chaîne de caractère en chaîne formatée

mot = "world!"
chaine = "Hello " + mot
print(chaine) # Hello world!

python_version = 3.11
fstring = f"Hello {mot}, Python {python_version + 0.1}" 
print(fstring) # Hello world!, Python 3.21

habitants = 7_753_000_000
superficie = 149_000_000
print(f"Nb habitants par km2 : {habitants/superficie}") # Nb habitants par km2 : 52.033557046979865
print(f"Nb habitants par km2 : {round(habitants/superficie)}") # Nb habitants par km2 : 52
# round() permet d'arrondir les nombres