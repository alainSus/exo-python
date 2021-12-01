import random

#les variables questions
quest1="Quelle est la capitale de la france?"
quest2="Qui a remporté la coupe du monde 2018?"
quest3="combien font 8+9?"
quest4="ya t il des hommes sur mars?"

#les variables reponses
rep1="c'est paris"
rep2="c'est la france"
rep3="ca fait 17"
rep4="non"

print("\nBienvenue au jeu de la connaissance veuillez repondre conrectement aux questions afin de gagner des points au cas contraire votre compteur de points sera a 0, lorsque vous aurez raté 3 questions la partie est fini pour vous et lorsque vous en trouvé 10 vousgagnez et fin du jeu\n")

# alea est la variable choisi pour contenir la questions choisi aleatoirement
#la fonctions random pour choisir les questions aleatoirement
alea1= random.randint(1,4)
alea2= random.randint(1,4)

print("votre question est:\n")

if alea1==1:
    print(quest1)
    if alea1==1:
        print(rep1,"votre reponse est juste vous gaagner 1 points")
    else:
        print("votre reponse est fausse vous compteur retourne a 0")
        
else: 
    if alea1==2:
        print(quest2)
        if alea1==2:
            print(rep2,"votre reponse est juste vous gagner 1 points")
        else:
            print("votre reonse est fausse votre compteur retourne a 0") 
    else:
        if alea1==3:
            print(quest3)
            if alea1==3:
                print(rep3,"votre reponse est juste vous gagner 1 points")
            else:
                print("votre reponse est fausse votre est compteur retourne a 0")
        else:
            print(quest4)
            if alea1==4:
                print(rep4,"votre reponse est juste vous gagnez 1 points")
            else:
                print("votre reponse est fausse votre compteur retourne a 0")
    




