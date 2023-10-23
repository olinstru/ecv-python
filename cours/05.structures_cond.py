# IF

int
float
str
bool # True / False (avec une majuscule !)

# Opérateurs booléens

# and
# or
# not

if (True):
    pass # L'identation est très importante ; c'est ce qui indique au code si on est dans un bloc d'instruction ou pas.
pass

# Une tablutation est symbolisée par 4 espaces en Python. VSCode ajoute automatiquement 4 espaces lorsqu'on appuie sur la touche Tab. 
# Attention aux copié-collé sur Internet : on ne peut pas mélanger des tabulation "normales" aux tabulations Python (on choisit soit l'un soit l'autre !)

if (False):
    pass
elif (False):
    pass
else:
    pass

""" 
La clause ELIF permet d'ajouter une autre condition à tester : 
Si la condition IF est fausse, alors Python teste la condition ELIF. 
Si la condition ELIF est fausse, Python applique les instructions contenues dans ELSE. """

#  == équal
# <= inférieur ou égal
# >= supérieur ou égal
# < inférieur à
# > supérieur à
# != n'est pas égal à

# Algo SNCF
age = int(input("Quel est votre âge ?"))

if (age > 0) and (age < 18):
    print("Statut enfant")
elif (age >= 18) and (age < 70):
    print("Statut adulte")
elif (age >= 70):
    print("Statut sénior")


# Algo Notes
note = -1
absence = False
triche = True

# not


if (absence == True) or (triche == True):
    note = 0
else:
    note = int(input("Saisir la note de l'élève: "))
    
if (note >= 0) and (note <= 20):
    print(f"Note finale: {note}")
else:
    print("Erreur système")