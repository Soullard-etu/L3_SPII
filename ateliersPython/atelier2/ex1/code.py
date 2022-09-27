def somme(L:list)->float:
    """fait la somme des entier de la liste 'L'

    Args:
        L (list): liste d'entier

    Returns:
        float: moyenne de la liste entrer en parametre
    """
    laSomme = 0
    # for i in range(len(L)):
    #     laSomme += L[i]

    for e in L:
        laSomme += e
    
    # while Element in L:
    #     laSomme += Element

    return laSomme
#-----------------------------------------------------------------------------------------------
def test_exercice1 ():
    """fonction de test de l'ennonce de l'exo
    """
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide : ", somme([]))
    #test somme 11111
    S=[1,10,100, 1000,10000]
    print("Test somme 1111 : ", somme(S))
#-----------------------------------------------------------------------------------------------
def moyenne(L:list) -> int:
    """fait la moyenne de la liste d'entier en parametre

    Args:
        L (list): liste d'entier

    Returns:
        int: entier le plus grand de la liste
    """
    if len(L) == 0:
        return 0
    return somme(L)/len(L)
#-----------------------------------------------------------------------------------------------
def nb_sup (L:list,e:int) -> int:  
    """cherche le nombre de valeur superieur a 'e' dans une liste d'entier

    Args:
        L (list): liste d'entier
        e (int): entier

    Returns:
        int: le nombre d'entier superieur a 'e' dans 'L'
    """
    valMax = 0
    for i in L:
        if i > e :
            valMax +=1

    return valMax
#-----------------------------------------------------------------------------------------------
def moy_sup(L:list,e:int) -> float:
    """fait la moyene des entier strictement superieur au parametre 'e'

    Args:
        L (list): liste d'entier
        e (int): entier 

    Returns:
        float: moyenne des entier superieur a 'e'
    """
    moyenneSup = 0
    for i in L:
        if i > e:
            moyenneSup += i

    return moyenneSup/nb_sup(L,e)
#-----------------------------------------------------------------------------------------------
def val_max(L:list) -> int:
    """cherche la valeur max dans une liste d'entier et la retourne

    Args:
        L (list): liste d'entier

    Returns:
        int: entier le plus grand trouver dans la liste
    """
    valMax = 0
    for i in L:
        if i > valMax:
            valMax = i

    return valMax
#-----------------------------------------------------------------------------------------------
def ind_max(L:list) -> int:
    """retourne l'index de la valeur max de la liste entrer en parametre

    Args:
        L (list): liste d'entier suposer sans repetition

    Returns:
        int: index de l'entier le plus grand
    """
    index = 0
    valMax = 0
    for i in range(len(L)):
        if L[i] > valMax:
            valMax = L[i]
            index = i

    return index
#-----------------------------------------------------------------------------------------------