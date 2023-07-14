
def main():
       
    from conn import cursor,connection
    def liste_doc():
        request = "SELECT * FROM livre"
        cursor.execute(request)
        donnee = cursor.fetchall()
        for i in donnee:
            print(i)
            
    def insert_doc():
        libelle = input("Entrez le nom du libelle :")
        description = input("Entrez la description :")
        auteur = input("Entrez le nom de l'auteur :")
        date_parution = input("Entrez la date de parution :")
        ref_livre = int(input("Entrez la ref du livre 5 chiffre svp :"))
        maison_edition = input("Entrez le nom de la maison d'edition :")
        request = """insert into livre
            (libelle,description,auteur,date_parution,ref_livre,maison_edition)
            values (%s, %s, %s, %s, %s, %s)"""
        params = (libelle,description,auteur,date_parution,ref_livre,maison_edition)
        cursor.execute(request,params)
        connection.commit()

    def update_doc():
        premier = input("Que vous voulez mettre a jour (description,auteur,date_parution,maison_edition) :")
        deux =  input("entrez la valeur :")
        trois = input("Entrez le libelle du livre :")
        request =  f"update livre set {premier.strip('')}= %s where libelle= %s"
        params = (deux,trois)
        cursor.execute(request,params)
        connection.commit()
        print("Nombre de lignes mises à jour :", cursor.rowcount)
        
        
    def delete_doc():
        sup = str(input("Entrez le libelle du livre a supprimer :"))
        request =  "delete from livre WHERE libelle = %s"
        params = (sup)
        cursor.execute(request,(params,))
        connection.commit()
            
    
    
    
    print("""  
            ---------------------------
            Menu - Gestion des documents:
            ----------------------------
        """)
    print("""
        \n 1-Afficher la liste des documents" 
        \n 2-Ajouter un document
        \n 3-Mettre à jour un document
        \n 4-Supprimer un document
        \n 5-Retour au menu principal
        \n 0-Quitter
        """)
    choix = int(input("Votre choix : "))
    while choix != 0:
        if choix == 1:
            liste_doc()
        elif choix == 2:
            insert_doc()
            print("Enregistrement effectuer...")
        elif choix == 3:
            update_doc()
            print('Mise a jour effectuer...')
            pass
        elif choix == 4:
            delete_doc()
            print('Suppression effectuer...')
        elif choix == 5:
            exec(open("maine.py").read())
        else:
            print("Choix invalide. Veuillez réessayer.")
            choix = int(input("Votre choix : "))
        choix = int(input("Veillez entrez votre nouveau choix : "))
    print('Merci ("_")')

if __name__ == "__main__":
    main()
