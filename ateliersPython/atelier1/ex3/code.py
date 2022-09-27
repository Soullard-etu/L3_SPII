from math import sqrt
##########################################################################
def discriminant(a : int or float,b : int or float,c : int or float) -> float:
    """ calcule le discriminant

    Args:
        a (int or float): _description_
        b (int or float): _description_
        c (int or float): _description_

    Returns:
        float: discriminant
    """
    return b*b - 4*a*c
##########################################################################
def racine_unique(a,b):
    """calcule racine unique

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    x = (-b)/(2*a)
    return x
##########################################################################
def racine_double(a,b,delta,num):
    if num == 1:
        return (-b+sqrt(delta))/(2*a)
        
    elif num == 2:
        return (-b-sqrt(delta))/(2*a)
##########################################################################
def str_equation(a,b,c) -> str:
    chaine = str(a) + 'x^2 '

    if a == -1 or a == 1: 
        chaine = chaine.replace('1', '')

    if b == -1 : 
        chaine += '-x '
    elif b < 0 : 
        chaine += str(b) + 'x '
    elif b == 1 : 
        chaine += '+ x '
    elif b != 0 : 
        chaine += '+ ' + str(b) + 'x '

    if c < 0 : 
        chaine += str(c)
    elif c != 0 : 
        chaine += '+ ' + str(c)

    return chaine
##########################################################################
def  solution_equation(a,b,c) -> str:
        delta = discriminant(a,b,c)
        chaineRetour = 'La solution de léquoition : ' + str_equation(a,b,c) + '\n'

        if delta == 0:
            x = racine_unique(a,b)
            chaineRetour += 'Racine unique : x = ' + str(x)

        elif delta > 0:
            num = 1
            x1 = racine_double(a,b,delta,num)
            num = 2
            x2 = racine_double(a,b,delta,num)
            chaineRetour += 'Deux racines :\nx1 = ' + str(x1) + '\nx2 = ' + str(x2)

        else:
            chaineRetour += 'Pas de solution réelle'

        return chaineRetour
##########################################################################
def equation(a,b,c):
    print(solution_equation(a,b,c))
##########################################################################
def test():
    a = float(input("saisir a (!=0): "))
    b = float(input("saisir b : "))
    c = float(input("saisir c : "))
    if a != 0 :
        equation(a,b,c)
##########################################################################
while True :
    test()