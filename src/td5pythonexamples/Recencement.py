#!/usr/bin/python3

# utiliser "python3 ./Recencement.py

import psycopg2

conn = psycopg2.connect("dbname='dbnf18p094' user='nf18p094' host='tuxa.sme.utc' password='hTpwa6SF'")
cur = conn.cursor()
sql = "SELECT * FROM dpt2 ORDER by num"
cur.execute(sql)
print("\t[N] Nom (Population)")

row = cur.fetchone()
while row:
    print("\t[%s] %s (%s)" % (row[0], row[1], row[2]))
    row = cur.fetchone()

sql = "SELECT MAX (population) FROM dpt2";
cur.execute(sql)
row = cur.fetchone();
print("\n\tDépartement le plus peuplé: ", row[0]);

sql = "SELECT MIN (population) FROM dpt2";
cur.execute(sql);
row = cur.fetchone();
print("\tDépartement le moins peuplé: ", row[0]);
print()
conn.close();