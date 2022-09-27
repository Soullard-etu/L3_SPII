DIC_PRIX_SELON_POID_SELON_TYPE_DE_LETTRE = {
    'verte': {
        '20': 1.16,
        '100': 2.32,
        '250': 4.00,
        '500': 6.00,
        '1000': 7.50,
        '3000': 10.50,
        'om1' : 0.05,
        'om2' : 0.11
    },

    'prioritere': {
        '20': 1.43,
        '100': 2.86,
        '250': 5.26,
        '500': 7.89,
        '3000': 11.44,
        'om1' : 0.05,
        'om2' : 0.11
    },

    'ecopil': {
        '20': 1.14,
        '100': 2.28,
        '250': 3.92,
        'om1' : 0.02,
        'om2' : 0.05
    },

    'colissimo': {
        '500': 8.35,
        '1000': 11.20,
        '2000': 14.10,
        '5000': 23.65,
        '10000': 37.50,
        '15000': 75.85,
        '30000': 87.40
    }
}
#-------------------------------------------------------------------------------------------------------
# #declaration constante des pays part zones
DIC_ZONES = {
    'om1' : ['guyane', 'guadeloupe', 'martinique', 'lareunion', 'stpierreetmiquelon', 'stbarthelemy', 'stmartinetmayotte'],
    'om2' : ['nouvellecaledonie', 'polynesiefrançaise', 'wallisetfutuna', 'taaf']
}
#-------------------------------------------------------------------------------------------------------
def replacementCarac(paraChaine:str) -> str:
    """fonction de remplacement de caractere et mise en minuscule

    Args:
        paraChaine (str): chaine de caractere a modiffier

    Returns:
        str: chaine modifier
    """
    #tableau des caractere a echanger
    TAB_DE_REMPLACEMENT = [['.', '-', ' ', 'é', 'è', 'à'], ['', '', '', 'e', 'e', 'a']]

    #renplace les caractere
    for j in range(len(TAB_DE_REMPLACEMENT[0])) :
        paraChaine = paraChaine.replace( TAB_DE_REMPLACEMENT[0][j], TAB_DE_REMPLACEMENT[1][j])

    #met le pays en minuscule
    minusculeChaine = ''
    for i in paraChaine :
        minusculeChaine += i.lower() 
    
    return minusculeChaine
#-------------------------------------------------------------------------------------------------------   
def testZone(paraPays:str) -> str:
    """fonction test de zone par raport au pays

    Args:
        paraPays (str): pays de reception à teste pour connaitre sa zone

    Returns:
        str: si il fait partie d'une zone si oui la quelle
    """

    #enleve espace, tiret, poing, accent et met en minuscule
    testPays = replacementCarac(paraPays)

    for key in DIC_ZONES :
        for i in DIC_ZONES[key] :
            if i == testPays :
                return key

    # #test si le pays saisie fait partie de om1
    # for k in TAB_OM1 :  #parcour le tableau reference 
    #     if k == testPays :  #teste si egaliter
    #         return 'om1'       #renvoie la zone
  
    # #test si le pays saisie fait partie de om2
    # for y in TAB_OM2 :
    #     if y == testPays : 
    #         return 'om2'  

    return 'aucune' #aucune zone par defaut
#-------------------------------------------------------------------------------------------------------
def testPoid(paraPoid:str, argTypeLettre:str) -> str:
    """test le poid referance tarif selon le type de lettre

    Args:
        paraPoid (str): poid de l'envoie
        argTypeLetre (str): le type de lettre utiliser

    Returns:
        str: le poid de referance pour le tarif ou si trop lourd pour ce type d'envoie
    """
    #part defaut 
    reponse = 'trop lourd' 

    #parcour les poid selon le type de lettre, renvoie la premiere 
    for keyPoid in DIC_PRIX_SELON_POID_SELON_TYPE_DE_LETTRE[argTypeLettre] : 
        try:
            if int(paraPoid) <= int(keyPoid) : 
                reponse = keyPoid
                return reponse 
                
        except: #certain dictionnaire comporte une zone et la convertion ex: om1 en int est une erreur mais veut aussi dire que le poid d'envoi est trop lourd
            return reponse

    return reponse

def calculeTarif(argPoid:str, argPoidMax:str, argTypeLettre:str, argZone:str) -> float:
    """calcule le cout de l'envoie

    Args:
        argPoidMax (str): _description_
        argPoid (str): _description_
        argTypeLettre (str): _description_
        argZone (str): zone d'envoie

    Returns:
        float: le prix final
    """
    tarifSelonPoid = DIC_PRIX_SELON_POID_SELON_TYPE_DE_LETTRE[argTypeLettre][argPoidMax]
    tarifZone = 0
    if argZone != 'aucune':
        for keyChercheZone in DIC_PRIX_SELON_POID_SELON_TYPE_DE_LETTRE[argTypeLettre] :
            if keyChercheZone == argZone :
                tarifZone = DIC_PRIX_SELON_POID_SELON_TYPE_DE_LETTRE[argTypeLettre][keyChercheZone]

    if float(argPoid)%10 != 0 :
        poidDisaine = float(argPoid)//10 +1
    else :
        poidDisaine = float(argPoid)/10

    return tarifSelonPoid + poidDisaine * tarifZone

#saisir pays de reception et teste s'il existe
okPays = False
while okPays == False :
    inputPays = input('saisir pays de reception : ')
    pays = replacementCarac(inputPays)
    if pays == 'france':
        break
    for i in range(len(DIC_ZONES)):
        for key in DIC_ZONES[i]:
            if key == pays :
                okPays = True
                break

#saisie de poid et test si c'est un chffre
poid = 0
okPoid = False
while okPoid == False :
    try : 
        poid = input("saisir le poid du coli (en g) : ")
        int(poid)
        okPoid = True
    except:
        okPoid == False

#saisie type de lettre et teste si elle fait partie de la liste 
typeLettre = ''
okLettre = True
while okLettre :
    inputTypeLettre = input('saisir type de lettre (verte, prioritere, ecopil, colissimo) : ')
    typeLettre = replacementCarac(inputTypeLettre)
    for key in DIC_PRIX_SELON_POID_SELON_TYPE_DE_LETTRE :
        if typeLettre == key : 
            okLettre = False
            break

#teste si le poid est trop lourd et la zone
poidMax = testPoid(poid, typeLettre)
zone = testZone(pays)

#######################################################################################################################
if typeLettre == 'colissimo' and zone != 'om1' :  #car l'envoie en colissimo est seulement disponible pour les envoie en zone om1
    print("L'envoi en colissimo n'est pas possible hors de la zone om1")

elif poidMax == 'trop lourd':
    print("envoie imposible car poid trop lourd pour ce type d'envoie")

else :
    prix = calculeTarif(poid, poidMax, typeLettre, zone)
    print("\nPour un envoie de type:", typeLettre,"vers le pays:", pays,"zone:", zone, "de", poid,"g\nLe prix d'envoie est de", prix)




