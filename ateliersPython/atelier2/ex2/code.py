def position(L:list,e:int) -> int:
    
    # for i in range(len(L)):
    #     if L[i] == e:
    #         return i

    # return -1
    defaut = -1
    compteur = 0
    while compteur > -1:
        if L[compteur] == e:
            defaut = compteur 
            compteur = -2
        compteur =+ 1

    return defaut
#-----------------------------------------------------------------------------------------------
def nb_occurrences(L:list,e:int) -> int:

    compteurE = 0
    for i in L:
        if e == i:
            compteurE +=1

    return compteurE
#-----------------------------------------------------------------------------------------------
def est_triee(L:list) -> bool:

    res = True
    for i in range(len(L)):
        if i != 0 and L[i-1] > L[i]:
            res = False

    # cdtion = True
    # i = 0
    # while cdtion:
    #     try:
    #         if L[i] < L[i+1]:
    #             cdtion = False
    #     except:
    #         cdtion = False
    #     i += 1

    # cdtion = True
    # i = 0
    # while cdtion:
    #     if i <= len(L)
    #         if L[i] < L[i+1]:
    #             cdtion = False
    #     else:
    #         cdtion = False
    #     i += 1

    return res
#-----------------------------------------------------------------------------------------------
# def position_tri(L:list,e:int):

#-----------------------------------------------------------------------------------------------
def a_repetitions(L:list) -> bool:
    res = False

    for i in L:
        for j in L:
            if i == j:
                res = True

    return res
#-----------------------------------------------------------------------------------------------




# # initialisation de la liste T à la liste vide 
# #Pour chaque élément de la liste L (boucle while):
# #  si l'élément n'est pas présent dans la liste T (NB: on peut utiliser l'opérateur in 
# (if x in T)):
# on ajoute l'élément dans la liste T 
# sinon
# on peut conclure qu'il y a une répétition

T = []*0
