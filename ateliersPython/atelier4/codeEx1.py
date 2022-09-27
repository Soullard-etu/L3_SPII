import random
#---------------------------------fin des import
def gen_list_random_int(int_nbr=10, int_binf=0, int_bsup=10) -> list:
    """genere une liste d'entier selont 3 parametre

    Args:
        int_nbr (int, optional): longueur de la liste. Defaults to 10.
        int_binf (int, optional): entier minimum. Defaults to 0.
        int_bsup (int, optional): entier maximum. Defaults to 10.

    Returns:
        list: la liste construite
    """
    # listeRetour = []
    # for i in range(int_nbr):
    #     listeRetour.insert(i, random.randrange(int_binf, int_bsup))
    
    # return listeRetour

    return [random.randrange(int_binf, int_bsup) for i in range(int_nbr)]

#print de test
print(gen_list_random_int())

