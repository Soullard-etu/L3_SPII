import random

def message_imc(iMC:float) -> str:
    
    if iMC < 16.5:
        chaineReponce = 'dénutrition ou famine'
    elif iMC <= 18.5:
        chaineReponce = 'maigreur'
    elif iMC <= 25:
        chaineReponce = 'corpulence normale'
    elif iMC < 30:
        chaineReponce = 'surpoids'
    elif iMC <= 35:
        chaineReponce = 'obésité modérée'
    elif iMC <= 40:
        chaineReponce = 'obésité sévère'
    else :
        chaineReponce = 'obésité morbide'

    return  chaineReponce

def test():
        indice = float(input("Entrer un IMC : "))
        print("Cet IMC corespond à une", message_imc(indice))


valeursTest = random.sample(range(50), 20)

for i in valeursTest :
    print(i, '=>', message_imc(i))
