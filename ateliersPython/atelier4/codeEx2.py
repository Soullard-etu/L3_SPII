import random
#-----------------------fin des importartations
def mix_list(list_to_mix:list) -> list:
    """mix la liste entrer en parametre

    Args:
        list_to_mix (list): chaine a mixer

    Returns:
        list: liste mixer
    """
    return random.sample(list_to_mix, len(list_to_mix)) 

#print de teste
l=[1,2,3,4,5,6]
print(mix_list(l))
print(l)


