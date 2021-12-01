import random

quest1=("la capitale de la france est paris?\na-dakar\nb-paris\nc-rome")

reponse1=input("votre reponse est: ")
points=0

    

quest2=("la coupe du monde 2018 a été remporté par:\na-le senegal\nb-la france\nc-l'allamagne")

reponse2=input("votre reponse est: ")
points=0

    
    
quest3=("quel est le jeu de fps le plus joué au monde?\na-warface\nb-call of duty\nc-apex")

reponse3=input("votre reponse est: ")
points=0

    
    
    
hasard=random.randint(1,3)

if hasard==1:
    print("la capitale de la france est paris?\na-dakar\nb-paris\nc-rome")
    print(reponse1)
else:
    if hasard==2:
        print("la coupe du monde 2018 a été remporté par:\na-le senegal\nb-la france\nc-l'allamagne")
        print(reponse2)
    else:
        print("quel est le jeu de fps le plus joué au monde?\na-warface\nb-call of duty\nc-apex")
        print(reponse3)



        
if reponse1=="paris":
    print("vous avez trouvé")
else:
    print("vous avez faussé")   
    

if reponse2=="la france":
    print("vous avez trouvé")
else:
    print("vous avez faussé")
    
    
if reponse1=="call of duty":
    print("vous avez trouvé")
else:
    print("vous avez faussé")