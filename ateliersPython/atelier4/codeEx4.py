import random
#---------------------fin des import
def extract_elements_list(list_in_which_to_choose:list, int_of_element_to_extract:int) -> list:
    """renvoie un ou plusieur d'elements d'une liste 

    Args:
        list_in_which_to_choose (list): la liste ou choisir
        int_of_element_to_extract (int): nombre d'element(s) a choisir dans la liste

    Returns:
        list: liste avec element(s) choisie
    """
    
    # res = []
    # for i in range(int_of_element_to_extract):
    #     res.insert(i, random.choice(list_in_which_to_choose))
    # return res

    return [random.choice(list_in_which_to_choose) for i in range(int_of_element_to_extract)]

#print de teste
print(extract_elements_list(['test', 'tt', 'ee'], 2))