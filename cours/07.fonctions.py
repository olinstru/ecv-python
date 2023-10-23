def enum_classe(classe = []):
    for eleve in classe:
        print(f"Mr/Mlle {eleve}")

def addition(a, b):
    return a + b

classe_B1 = ["Jérôme", "Philippe", "Mathilde"]
classe_B2 = ["Géraldine", "Marie", "Luc"]
classe_B3 = ["Vincent", "Laëtitia", "Laurent"]

enum_classe(classe_B1)
enum_classe(classe_B2)
enum_classe(classe_B3)
enum_classe()

# max()
# min()
# sorted()
# round()
# len()