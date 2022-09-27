import random
#----------------------fin des import
def choose_element_list(list_in_which_to_choose:list):
    """choisie un element d'une liste au hazard

    Args:
        list_in_which_to_choose (list): liste ou il faut choisir

    Returns:
        _type_: renvoie l'element choisie
    """
    i = random.randrange(0, len(list_in_which_to_choose))
    return list_in_which_to_choose[i]


#print de teste
print(choose_element_list([1,2,3,4,5,6]))