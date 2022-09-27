def full_name(str_arg:str) -> str:
    """prend en paramètre une chaine de caractère 
        de type 'nom prenom' et qui renvoie la même chaîne avec le nom en majuscule et le prénom 
        avec la première lettre seulement en majuscule.

    Args:
        str_arg (str): chaine a modifier

    Returns:
        str: chaine modifier
    """
    chaineList = str_arg.split()    #separe le nom et prenom
    chaineList[0] = chaineList[0].upper()   #met le nom en majuscule
    chaineList[1] = chaineList[1][0].upper() + chaineList[1][1:].lower()    #met le prenom en misuscule sauf la premiere lettre qui elle passe en majuscule
    
    return chaineList[0] + ' ' + chaineList[1]  #retourne le resultat
#-----------------------------------------------------------------------------------------------
def is_mail(str_arg:str) -> tuple:
    """test si mail valide

    Args:
        str_arg (str): mail a tester

    Returns:
        tuple: renvoi un code erreur
                (1, x) x n’est pas important, le mail est valide 
                (0, 1) le mail n’est pas valide, le corp n’est pas valide (bisgambiglia)
                (0, 2) le mail n’est pas valide, il manque l’@ 
                (0, 3) le mail n’est pas valide, le domaine n’est pas valide (univ-corse)
                (0, 4) le mail n’est pas valide, il manque le 
    """
    res = (1, 0)    #message d'erreur part defaut 

    #liste constante pour les caractere autoriser pour le corp ou le domaine du mail (alphanumerique autosiser de base)
    LIST_CARACTERE_AUTORISEE_CORP = ['-', '_', '.']
    LIST_CARACTERE_AUTORISEE_DOMAINE = ['.', '-']


    if str_arg.count('@') != 1:     #si oui veut dire que '@' non present
        res = (0,2)
    else:
        #separation du corp et du domaine pour faciliter les test
        t = str_arg.split('@')
        corp = t[0]
        domaine = t[1]

        #declaration d'une variable pour tester les caractere non autoriser pour le corp
        testCorp = corp
        testDomaine = domaine
        for i,j in LIST_CARACTERE_AUTORISEE_CORP,LIST_CARACTERE_AUTORISEE_DOMAINE:
            testCorp = testCorp.replace(i,'')
            testDomaine = testDomaine.replace(j,'')
            

        if (not testCorp.isalnum()) or corp[0] == '.' or corp[-1] == '.' or ('..' in corp):  #test si '..' present, si '.' en debut ou fin de chaine et si il y a la presence d'un caractere non autoriser 
            res = (0,1)
        elif (not testDomaine.isalnum()) or ('..' in domaine):  #test si un caractere non autoriser est present ou si '..'present
            res = (0,3)
        elif (not '.' in domaine):  #test si il mange le '.'
            res = (0,4)
        
    return res  #retourne le code erreur 




print( is_mail('charle@test.com'))



