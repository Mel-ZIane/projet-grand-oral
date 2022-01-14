from collections import ChainMap

with open("Lyrics.txt","r") as file:
    print(file.read())




i = {"i","î","y","outil","ean","ee"}
y = {"hu", "u", "ût"}
u = {"ou", "oun", "ouls", "oo"}
e = {"é","er","ez","ey","ai","è"}
ø = {"eu", "eux", "heu","oeu"}
o = {"au", "ô", "eau", "o"}
a = {"à", "a", }
ɛ = { "oint "," in","aint","ein","im","ien" }
œ̃un = {"un", "um"}
ɔ = {"on", "om", "ont"}
ɑ̃an = {"en", "am", "ang","em"}
dico_rime = ChainMap(i,y,u,e,ø,o,a,ɛ,œ̃un,ɔ,ɑ̃an)
print(dico_rime)

def analyse_rime ()



