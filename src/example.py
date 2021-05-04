# PROGRAMME PYTHON TYPE CREER ASSOCIATION (à dériver sous toutes ses formes pour faire les autres fonctions)
import psycopg2

arguments = "dbname='dbnf18p083' user='nf18p083' host='tuxa.sme.utc' password='SGcA8loh'" #args du compte nf18 de louis

def run(sql,args):
    conn = psycopg2.connect(arguments)
    cur = conn.cursor()
    cur.execute(sql,args)

    if cur.description:
        results = cur.fetchall()
    else:
        results = False

    conn.commit()
    cur.close()
    conn.close()
    return results

def addAssociation(): # à modifier, pas assez de d'attributs pris en compte, c'est juste un exemple ici
    nom = input("Nom de l\'association : ")
    dateCreation = input("Date de création de l\'association : ")
    
    sql = "SELECT * FROM association WHERE nom=%s"

    foundAsso = run(sql,(nom,))
    if foundAsso:
        print("Nom d\'association déjà pris.")
    else: 
        sql="INSERT INTO association VALUES (%s,%s)"
        run(sql,(nom,dateCreation,))

        # vérification d'insertion
        sql = "SELECT * FROM association WHERE nom=%s"
        
        verif = run(sql,(nom,))
        print(f"L\'association {verif[0][0]} a bien été ajoutée.") # pour retourner juste le nom
    #    print(f"L\'association {verif[0]} a bien été ajoutée.") # pour retourner juste le tuple

    return 

addAssociation()