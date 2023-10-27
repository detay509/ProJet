
import random
jwe_tj=""
while not jwe_tj=="k":
    inter=random.randint(1,48)
    essaie=5
       

    while essaie>0:
            try:
                nombre=int(input("Entrer un nombre il vous reste " +str(essaie) +" essaie"))
                if nombre>=1 and nombre<=48:
                    if nombre>inter:
                        print(" Vous avez perdu ce nombre est plus grand que le nombre genere")
                    elif nombre<inter:
                        print("Vous avez perdu ce nombre est plus petit que le nombre genere")
                    else:
                        print("Vous avez gagne")
                        break
                    essaie -=1
                else:
                    print("Ce nombre doit etre dans l'intervalle 1 a 48")
            except valueError:
                print("Entrer un nombre")
    if essaie==0:
        print("vous n'avez plus d'essaie, le nombre etait " +str(inter))
    jwe_tj=input("Voulez-vous continuer? Si oui presser n'importe quelle touche, sinon k")
    if jwe_tj.lower=="k":
        print('Merci d avoir jouer')
    
        


