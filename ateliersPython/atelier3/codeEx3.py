import random
#-----------------------------------------------------------------------------------------------
def places_lettre(ch:str, mot:str) ->list:
    indexList = []

    for i in range(len(mot)):
        if mot[i] == ch:
            indexList.insert(0, i) 

    return indexList
#-----------------------------------------------------------------------------------------------
def outputStr(mot:str, lpos:list) -> str:
    retour = ['_']*len(mot)
    res = ''

    if len(lpos) != 0:
        if len(lpos) == len(mot):
            retour = mot

        else:
            for i in lpos:
                retour[i] = mot[i]
            for j in retour:
                res = res + j
            retour = res
    else:
        for i in range(len(mot)):
            res += '_'
        retour = res
        
    return retour
#-----------------------------------------------------------------------------------------------
def runGame():
    LIST_MOTS = ['chomage', 'avenir', 'travail', 'bebe']
    motRandom = random.choice(LIST_MOTS)
    lposTotal = []
    
    gagner = 5
    while gagner > 0:
        lettreTest = input("donne une lettre: ")
        lpos = places_lettre(lettreTest, motRandom)

        if lpos != 0:
            if lpos != lposTotal:
                for i in lpos:
                    if not i in lposTotal:
                        lposTotal.insert(0, i)
        else:
            gagner -= 1

        print(outputStr(motRandom, lposTotal))
        if outputStr(motRandom, lposTotal) == motRandom:
            print("gagner")
            gagner = 0
        elif gagner == 0:
            print("perdu")


runGame()


