# LISTES

eleves = ["Camille", "Thomas", "Luc", "Elisa", "Franck"]
print(eleves)

notes = [10.5, 18.0, 16.0, 20.0, 8.0]
print(notes)

dates = []
print(dates)

print(type(dates)) # <class 'list'>
print(type(notes) == list) # True
print(type(notes) == int) # False

# MANIPULER DES LISTES

# len() = affiche la longueur de la liste

longueur = len(notes)
print(longueur) # 5

# LES INDICES DES LISTES COMMENCENT À 0 !!!
# 0, 1, 2, 3, etc...
# Le dernier élément est toujours n-1

print(eleves[0]) # Camille
print(eleves[len(eleves) - 1]) # Franck

# equivalent à 
print(eleves[- 1]) # Franck

# On peut imbriquer des tableaux dans des tableaux

liste_wtf = [
    [123, 12, 789],
    [345, 789, 467],
    [...]
]

# Afficher les premiers et derniers résultats d'une liste

print(eleves[0])
print(eleves[len(eleves) - 1])
# équivalent
print(eleves[- 1])


eleves.append("Laetitia")
notes.append(14.5)

# Fonctions utiles

# insert()
# pop()
# remove()

print(eleves)
print(notes)

# SLICING

jours = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]
print(jours)

print(jours[0:2]) # lun, mar
print(jours[4:5]) # ven
print(jours[:3]) # lun, mar, mer
print(jours[:]) # affiche tout le tableau

weekend = jours[-2:]
print(weekend) # sam, dim

# LISTES N-DIMENSIONS
jours_fr_en = [
    ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"],
    ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
]
