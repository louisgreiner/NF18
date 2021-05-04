#!/usr/bin/python3

import psycopg2
import display

conn = psycopg2.connect("dbname='dbnf18p094' user='nf18p094' host='tuxa.sme.utc' password='hTpwa6SF'")

cur = conn.cursor()
sql = "SELECT * FROM etudiant ORDER by nom"
cur.execute(sql)
print("\t--- (login) Nom Prénom ---")

row = cur.fetchone()
while row:
    print("\t(%s) %s %s" % (row[0], row[1], row[2]))
    row = cur.fetchone()


login = '1'

while login != '0':
    login = input("Entrez le login de l'étudiant recherché (entrez 0 pour sortir): ")
    display.display(conn,login)

conn.close();