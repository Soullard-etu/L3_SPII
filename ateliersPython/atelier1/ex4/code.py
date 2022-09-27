import datetime

def est_bissextile(annee:int) -> bool:
    """
    Args:
        annee (int): exemple 2022

    Returns:
        bool: True si l'annee est bissextile et False si elle ne l'est pas
    """
    return (annee%4 == 0 and annee%100 != 0) or annee%400 ==0


def date_est_valide(jour:int,mois:int,annee:int) -> bool:
    dateValide = False

    if jour > 0 and mois < 13:
        if mois == 2:
            if jour < 29 and est_bissextile(annee):
                dateValide = True
            elif jour < 28:
                dateValide = True

        elif mois%2 != 0:
            if jour < 31:
                dateValide = True
            elif jour < 30:
                dateValide = True

    return dateValide

def saisie_date_naissance() -> datetime:
    while 1:
        jour = int(input('Entrer votre date de naissance\nsaisir le jour: '))
        mois = int(input('saisir le mois: '))
        annee = int(input('saisir annee: '))

        if date_est_valide(jour,mois,annee) :
            date = datetime.datetime(annee, mois, jour)
            return date

        print('date incorect...')

def age(date_naissance:datetime) -> int:
    date = datetime.datetime.now()
    a = date.year - date_naissance.year
    return a


def est_majeur(date_naissance:datetime) -> bool:
    if age(date_naissance) < 18:
        return False
    return True

def test_acces():
    dateNaissance = saisie_date_naissance()
    ageTest = age(dateNaissance)

    if est_majeur(dateNaissance):
        print('Bonjour, vous avez ', ageTest,' ans, Accès autorisé')
    else :
        print('Désolé, vous avez ', ageTest,' ans, Accès interdit')

test_acces()