import psycopg2
import os
import sys
import subprocess

def executePrint(s):
	cur.execute(s)
	print cur.fetchall()

if len(sys.argv) != 2:
	print "Usage: trigger-test.py <your trigger SQL file>"
	sys.exit(1)

subprocess.call(["psql", "-f", "trigger-database.sql", "flighttrigger"])
subprocess.call(["psql", "-f", sys.argv[1], "flighttrigger"])

conn = psycopg2.connect("dbname=flighttrigger user=vagrant")
cur = conn.cursor()

print "Initial State"
executePrint("select * from customers")
executePrint("select * from newcustomers")
executePrint("select * from ffairlines")

print "Inserting a new customer into newcustomers"
cur.execute("insert into newcustomers values ('cust4', 'Anthony Gonzalez', to_date('1977-10-06', 'yyyy-mm-dd'))")
conn.commit()

print "After insertion"
executePrint("select * from customers")
executePrint("select * from newcustomers")
executePrint("select * from ffairlines")

print "Inserting flights for recently added customer and adding airline to ffairlines"
cur.execute("insert into flewon values ('SW132', 'cust4', to_date('2016-08-05', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('AA131', 'cust4', to_date('2016-08-08', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('SW116', 'cust4', to_date('2016-08-03', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('UA101', 'cust4', to_date('2016-08-01', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('SW116', 'cust4', to_date('2016-08-04', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('SW110', 'cust4', to_date('2016-08-02', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('SW106', 'cust4', to_date('2016-08-06', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('UA138', 'cust4', to_date('2016-08-09', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('SW107', 'cust4', to_date('2016-08-07', 'YYYY-MM-DD'))")
cur.execute("insert into ffairlines values ('cust4', 'AA')")
conn.commit()

print "After insertion"
executePrint("select * from customers")
executePrint("select * from newcustomers")
executePrint("select * from ffairlines")

print "Deleting a customer from customers table"
cur.execute("delete from flewon where customerid = 'cust15'")
cur.execute("delete from customers where customerid = 'cust15'")
conn.commit()

print "After deletion"
executePrint("select * from customers")
executePrint("select * from newcustomers")
executePrint("select * from ffairlines")
