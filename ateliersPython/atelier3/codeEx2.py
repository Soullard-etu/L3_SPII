from encodings import utf_8


def mots_Nlettres(lst_mot:list, n:int) -> int:
    compteurDeN = 0

    for i in lst_mot:
        if len(i) == n:
            compteurDeN += 1

    return compteurDeN
#-----------------------------------------------------------------------------------------------
def commence_part(mot:str, prefix:str) -> bool:
    teste = ''

    for i in range(len(prefix)):
        teste = teste + mot[i]

    if teste == prefix:
        res = True
    else:
        res = False
    
    return res
#-----------------------------------------------------------------------------------------------
def fini_par(mot:str, suffixe:str) -> bool:
    teste = ''

    for i in range(len(suffixe)):
            teste = teste + mot[-(i+1)]

    if teste == suffixe:
        res = True
    else:
        res = False

    return res
#-----------------------------------------------------------------------------------------------
def finissent_par(lst_mot:list, suffixe:str) -> list:
    res = []*0

    for i in lst_mot:
        if fini_par(i, suffixe):
            res += i
    
    return res
#-----------------------------------------------------------------------------------------------
def commencent_part(lst_mot:list, prefixe:str) -> list:
    res = []*0

    for i in lst_mot:
        if commence_part(i, prefixe):
            res += i
    
    return res
#-----------------------------------------------------------------------------------------------
def liste_mots(lst_mot:list, prefixe:str, suffixe:str, n: int) -> list:

    res = commencent_part(lst_mot, prefixe)
    res = finissent_par(res, suffixe)
    res = mots_Nlettres(res, n)

    return res
#-----------------------------------------------------------------------------------------------
def dictionnaire(fichier:str) -> list:
    FICHIER = open(fichier, "r", encoding="utf_8")
    return FICHIER.readlines()
#-----------------------------------------------------------------------------------------------


print(dictionnaire("ateliersPython/atelier3/littre.txt"))





