"""   2-obtenir le dernier mot de la ligne  """
poème = ["La Cigale ayant chanté Tout l'Été","Se trouva fort dépourvé"]
listerime = []

dico = {
    "E": ["é", "er", "ez", "ey", "ai", "è", "és"],
    "U": ["ou", "oun", "ouls", "oo","ue"]
}
""""""
def has_son(e, son):
    if (son in e):
        return True
    else:
        return False


""" parcourir à l'envers pour extraire le minimum de lettre qui fait un son"""

def get_son (poème,dico):
    for key, value in dico.items():
        son = ""
        for i in range(len(poème) - 1, 0, -1):
            son = poème[i] + son
            resultat = has_son(value, son)
            print(value, resultat, "son=", son, ":")
            if resultat == True:
                pass
                break
        if resultat == True:
            break
    return key
for phrase in poème:
    print(get_son(phrase, dico))
    key = get_son (phrase, dico)
    listerime.append(key)
print(listerime)


nombrerime = 0

def creer_rime(listerime,nombrerime):
    for i in listerime:
        if listerime[i] == listerime[i+1]:
            nombrerime += 1
            print("Il y a",nombrerime,"rime(s)" )

creer_rime(listerime,nombrerime)