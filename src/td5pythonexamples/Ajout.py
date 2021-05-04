#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect("dbname='nf18' user='root' host='localhost' password='root' port='5432'")
cur = conn.cursor()

print()
# num = input("Entrez le numéro de département: ")


# sql = "INSERT INTO dpt2 VALUES ('%s', '%s', %s)" % (num, dpt, pop)
sql = "INSERT INTO association VALUES ('AssoTest','test de la BdD', 'info', 'test@test', '10-10-2020', 'test.com')"
cur.execute(sql)
conn.commit()

conn.close();