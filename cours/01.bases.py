#geoffroy@gl-conseil.dev

print("Hello world!")

# Ceci est un commentaire 

mon_entier = 42
pi = 3.14
un_texte = "This is a text"
un_texte2 = 'This is a text'

x = 42
x = x + 1
x = x - 3
x = x / 10
x = x * 10
x = (x + 1) * 10

""" MANIPULATIONS DE TEXTE """

chaine = "Python "
chaine = chaine + "3.10 "
chaine = chaine * 3

print(chaine)
# Python 3.10 Python 3.10 Python 3.10 

chaine = "Python "
# chaine = chaine + 3.10
# TypeError: can only concatenate str (not "float") to str

# TYPES
int
str 
float
bool
list

chaine = chaine + str(3.10)
print(chaine)

nb_error = "3.10"
nb = float(nb_error)

print(nb)
print(type(nb))
print(type(nb) == float)