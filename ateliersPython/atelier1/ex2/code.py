#fonction pour savoir si l'annee est bissextile
def est_bissextile(annee:int) -> bool:
    """
    Args:
        annee (int): exemple 2022

    Returns:
        bool: True si l'annee est bissextile et False si elle ne l'est pas
    """
    return (annee%4 == 0 and annee%100 != 0) or annee%400 ==0


#fonction test
def test():
    for i in range(2000,2040,1) :
        if est_bissextile(i):
            print("L'année ", i," est bissextile !")

        else:
            print("L'année ", i," n'est pas bissextile...")

#test
test()