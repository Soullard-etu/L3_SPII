import random
#-------------------------------declaration--variale---------------------------------------------------------------
gameActive = True 
scoreJoueur1 = 0
scoreJoueur2 = 0
#-----------------------------------choix--nom--joueurs------------------------------------------------------------
while gameActive:
    isActive = True
    continuerPuit = True
    choixMachineOuNon = True
    tabChoixPossib = ['papier','pierre','ciseaux']

    while choixMachineOuNon:
        start = input("Voulez-vous jouer contre l'ordinateur (en 3 parties gagnante) O/N ? " )
        if start == 'O' or start == 'o':
            nomJoueur1 = input("Quel est votre nom ? ")
            print("Bienvenu ",nomJoueur1, " nous allons jouer ensemble \n")
            nomJoueur2 = 'Machine'
            machine = True
            choixMachineOuNon = False
        elif start == 'N' or start == 'n':
            nomJoueur1 = input("Quel est votre nom ? ")
            print("Bienvenu ",nomJoueur1, " nous allons jouer ensemble")
            nomJoueur2 = input("Quel est le nom du deuxième joueur ? ")
            print("Bienvenu ",nomJoueur2, " nous allons jouer ensemble \n")
            machine = False
            choixMachineOuNon = False
        else :
            print("Je n'ai pas compris desole...\n")
#--------------fin--choix--nom--joueurs--------------------------------------------------------------------------
#-----puit--autoriser--ou--non---------
    while continuerPuit:
        puit = input("Voulez vous jouer avec le puit O/N ? ")
        if puit == 'o' or puit == 'O':
            tabChoixPossib.append("puit")
            continuerPuit = False
        elif puit == 'n' or puit == 'N':
            continuerPuit = False
#--------------------------------------
#--------------------------------------la--patie--comence--(-ou--continue-)--------------------------------------
    while isActive:
        #---------------------------choix--joueurs---------------------------------------------------------------
        choixJoueur1 = input("Jouer {} faîtes votre choix parmi : {}" .format(nomJoueur1 ,tabChoixPossib), " ")
        if choixJoueur1 not in tabChoixPossib:
            joueur1_Ok = False
            print("Je n'ai pas compris votre réponse")
            while joueur1_Ok == False :
                choixJoueur1 = input("Jouer {} faîtes votre choix parmi : {}" .format(nomJoueur1 ,tabChoixPossib))
                joueur1_Ok = True
                if choixJoueur1 not in tabChoixPossib: 
                    joueur1_Ok = False

        if machine == True: 
            choixJoueur2 = random.choice(tabChoixPossib)

        elif machine == False:
            choixJoueur2 = input("Jouer {} faîtes votre choix parmi : {}" .format(nomJoueur2 ,tabChoixPossib), " ")
            if choixJoueur2 not in tabChoixPossib:
                joueur2_Ok = False
                print("Je n'ai pas compris votre réponse")
                while joueur2_Ok == False :
                    choixJoueur2 = input("Jouer {} faîtes votre choix parmi : {}" .format(nomJoueur2 ,tabChoixPossib), " ")
                    joueur2_Ok = True
                    if choixJoueur2 not in tabChoixPossib: 
                        joueur2_Ok = False
        #-------------fin--choix--joueurs-------------------------------------------------------------------------
        #----affiche--les--choix----------
        print("Si on récapitule :",nomJoueur1, choixJoueur1, "et", nomJoueur2, choixJoueur2,"\n")
        #--fin--affichage--choix----------------
        nomGagnant = 'aucun'
        #---teste--qui--gagne---------------------
        if choixJoueur1 == choixJoueur2:
            print("egaliter\n")
        elif (choixJoueur1 == 'puit' and (choixJoueur2 == 'pierre' or choixJoueur2 == 'ciseaux')) or (choixJoueur1 == 'pierre' and choixJoueur2 == 'ciseaux') or (choixJoueur1 == 'papier' and (choixJoueur2 == 'pierre' or choixJoueur2 == 'puit')) or (choixJoueur1 =='ciseaux' and choixJoueur2 == 'papier'):
            nomGagnant = nomJoueur1
            scoreJoueur1 += 1
        else:
            nomGagnant = nomJoueur2
            scoreJoueur2 += 1
        #---fin--du--test--------------------------
        #---affiche--le--resultat--de--la--manche--------------------------------
        if nomGagnant != 'aucun':
            print("le gagnant de la manche est",nomGagnant)
            print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")
        #--fin--affichage--------------------------------------------------------
        #----si--gagnant----------------------------------------------------------------------------------------
        if scoreJoueur1 == 3 or scoreJoueur2 == 3:
                isActive= False
                gameActive = False
                condition = True
                print("le grand gagnant est",nomGagnant)
                print("Les scores à l'issue de cette partie sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")
                scoreJoueur1 = 0
                scoreJoueur2 = 0
                while condition:
                    ouiNonAutrePartie = input("Voulez vous faire une autre partie O/N ? ")
                    if ouiNonAutrePartie == 'o' or ouiNonAutrePartie == 'O':
                        gameActive = True
                        while condition:
                            onChangeNom = input("Voulez vous changer les joueurs O/N ? ")
                            if onChangeNom == 'n' or onChangeNom == 'N':
                                isActive= True
                                condition = False
                            elif onChangeNom == 'o' or onChangeNom == 'O':
                                condition = False
                                choixMachineOuNon = True
                    elif ouiNonAutrePartie == 'n' or ouiNonAutrePartie == 'N':
                        break
print("Merci d'avoir joué ! A bientôt")