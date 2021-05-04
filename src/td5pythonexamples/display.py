#!/usr/bin/python3

# utiliser "python3 ./Menu.py

def display(conn,login):
    cur = conn.cursor()
    sql = "SELECT nom, prenom FROM etudiant WHERE login='%s'" % login
    cur.execute(sql)
    row = cur.fetchone()
    nom = row[0]
    prenom = row[1]
    
    print("Notes de l'étudiant %s %s (%s)" % (prenom, nom, login))
    
    sql = "SELECT * FROM devoir INNER JOIN note ON devoir.num = note.devoir WHERE note.etudiant = '%s' ORDER BY devoir.daterendu" % login
    cur.execute(sql)
    row = cur.fetchone()

    while row: 
        print("\t- %s [%s]: %s" % (row[5], row[4], row[2]))
        row = cur.fetchone()