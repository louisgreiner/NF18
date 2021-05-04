#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect("dbname='dbnf18p094' user='nf18p094' host='tuxa.sme.utc' password='hTpwa6SF'")
cur = conn.cursor()

print()
dpt = input("Entrez le nom de département: ")

sql = "DELETE FROM dpt2 WHERE nom='%s'" % (dpt)
cur.execute(sql)
conn.commit()

conn.close();