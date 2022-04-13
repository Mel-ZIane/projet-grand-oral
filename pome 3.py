"""   2-obtenir le dernier mot de la ligne  """
poème = ["Le vin sait revêtir le plus sordide bouge",
"D'un luxe miraculeux",
"Et fait surgir plus d'un portique fabuleux",
"Dans l'or de sa vapeur rouge",
"Comme un soleil couchant dans un ciel nébuleux",
"L'opium agrandit ce qui n'a pas de bornes",
"Allonge l'illimité",
"Approfondit le temps, creuse la volupté",
"Et de plaisirs noirs et mornes",
"Remplit l'âme au delà de sa capacité",
"Tout cela ne vaut pas le poison qui découle",
"De tes yeux, de tes yeux verts",
"Lacs où mon âme tremble et se voit à l'envers",
"Mes songes viennent en foule",
"Pour se désaltérer à ces gouffres amers",
"Tout cela ne vaut pas le terrible prodige",
"De ta salive qui mord",
"Qui plonge dans l'oubli mon âme sans remords",
"Et charriant le vertige",
"La roule défaillante aux rives de la mort "]
listerime = []

dico = {
    "E": ["é", "er", "ez", "ey", "ai", "è", "és"],
    "U": ["ou", "oun", "ouls", "oo","ue"],
    "OUGE":  ["ouge"],
    "EU":  ["eux"],
    "NE":  ["nes"],
    "LE":  ["le"],
    "ERS":  ["ers","ert"],
    "IGE":  ["ige"],
    "OR":  ["ords","ort"]

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
            #print(value, resultat, "son=", son, ":")
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
#print(listerime)



def creer_rime(listerime):
    nombrerime = 0
    nombrerimecroise = 0
    nombrerimeambrase = 0
    for i in range(len(listerime)-3):
        if listerime[i] == listerime[i+1]:
            nombrerime += 1
        if listerime[i] == listerime[i+2] and listerime[i+1] == listerime[i+3]:
            nombrerimecroise +=1
        if listerime[i] == listerime[i+3] and listerime[i+1] == listerime[i+2]:
            nombrerimeambrase +=1
    return ('rimes:',nombrerime,"rimes croisés",nombrerimecroise,"rimes embrasé", nombrerimeambrase)
print(creer_rime(listerime))