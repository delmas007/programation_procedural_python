

def main():
    print(""" 
    Bienvenu(e) au Menu:
    \n 1-Gestion des documents 
    \n 2-Gestion des prets
    \n 00-Quitter
    """)
    choix = int(input("Votre choix :"))

    while choix != 0:
        if choix == 1 :
            exec(open("document.py").read())
            choix=9
        elif choix == 2 :
            exec(open("pret.py").read())
            choix=9
        else:
            print("Choix invalide. Veuillez réessayer.")
            print(""" 
            Bienvenu(e) au Menu:
            \n 1-Gestion des documents 
            \n 2-Gestion des prets
            \n 0-Quitter
            """)
        choix = int(input("Votre choix :"))
    print('Merci ("_")')
            
    
if __name__ == "__main__":
    main()
        