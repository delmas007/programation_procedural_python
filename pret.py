

def main():
    from conn import cursor,connection
    from datetime import date
    def insert_pret():
        date_pret = date.today()
        date_formate_pret = date_pret.strftime('%Y-%m-%d')
        
        print("Veillez inserer la date retour")
        annee = 2023
        mois = int(input("Entrez le mois :"))
        jour = int(input("Entrez le jour :"))
        date_a_inserer = date(annee, mois, jour)
        date_formatee = date_a_inserer.strftime('%Y-%m-%d')
        
        rendu = False
        id_Livre = int(input("Entrez id du livre :"))
        id_per_Personne = int(input("Entrez id de la personne :"))
        
        request = """insert into pret
            (date_pret,date_retour,rendu,id_Livre,id_per_Personne)
            values (%s, %s, %s, %s, %s)"""
        params = (date_formate_pret,date_formatee,rendu,id_Livre,id_per_Personne)
        cursor.execute(request,params)
        connection.commit()

    def list_pret():
        request = """
        
            SELECT livre.libelle, personne.nom, personne.prenom
            FROM livre
            JOIN pret ON livre.id = pret.id_Livre
            JOIN personne ON personne.id_per = pret.id_per_Personne
            WHERE rendu=0 AND date_retour < CURDATE();
        """
        cursor.execute(request)
        donnee = cursor.fetchall()
        for i in donnee:
            print(i)

    def retour_document():
        valeur = True
        idp = input("Id du pret :")
        request =  "update pret set rendu = %s where id_pret= %s"
        params = (valeur,idp)
        cursor.execute(request,params)
        connection.commit()

    print("""    
        -----------------------------
        Menu - Gestion des prets:
        ------------------------------
        """)
    print("""
        \n 1-Inserer un pret de document
        \n 2-Retour document
        \n 3-List pret en retard
        \n 4-Retour au menu principal
        \n 0-Quitter
        """)
    
    choix = int(input("Votre choix : "))
    while choix != 0:
        if choix == 1:
            insert_pret()
            print("Enregistrement effectuer...")
        elif choix == 2:
            retour_document()
            print('Mise a jour effectuer...')
        elif choix == 3:
            list_pret()
        elif choix == 4:
            exec(open("maine.py").read())
        else:
            print("Choix invalide. Veuillez réessayer.")
            choix = int(input("Votre choix : "))
        choix = int(input("Veillez entrez votre nouveau choix :"))
    print('Merci ("_")')

if __name__ == "__main__":
    main()

