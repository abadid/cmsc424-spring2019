import psycopg2
import os
import sys
import subprocess
import pprint


pp = pprint.PrettyPrinter(indent=3)

def executePrint(s):
	cur.execute(s)
	pp.pprint(cur.fetchall())

def printAll(s):
    print(s)
    print("~~~~~~~~~~CUSTOMERS~~~~~~~~~~")
    executePrint("select * from customers")
    print("~~~~~~~~~~NEWCUSTOMERS~~~~~~~~~~")
    executePrint("select * from newcustomers")
    print("~~~~~~~~~~FFAIRLINES~~~~~~~~~~")
    executePrint("select * from ffairlines")

if len(sys.argv) != 2:
	print "Usage: trigger-test.py <your trigger SQL file>"
	sys.exit(1)

subprocess.call(["dropdb", "flighttrigger"])
subprocess.call(["createdb", "flighttrigger"])
subprocess.call(["psql", "-f", "trigger-database.sql", "flighttrigger"])
subprocess.call(["psql", "-f", sys.argv[1], "flighttrigger"])

conn = psycopg2.connect("dbname=flighttrigger user=vagrant")
cur = conn.cursor()



print("------------------- OPERATIONS ON CUSTOMERS -------------------")

printAll("Initial state")

print("Inserting ('cust4', 'Anthony Gonzalez', to_date('1977-10-06', 'yyyy-mm-dd'), 'AA') into customers table")
cur.execute("INSERT into customers values ('cust4', 'Anthony Gonzalez', to_date('1977-10-06', 'yyyy-mm-dd'), 'AA')")
conn.commit()

printAll("After inserting cust4")

print("Now deleting cust4")
cur.execute("DELETE from customers where customerid = 'cust4'")
conn.commit()

printAll("After deletion")

print("Inserting ('cust4', 'Anthony Gonzalez', to_date('1977-10-06', 'yyyy-mm-dd'), NULL) into customers table")
cur.execute("INSERT into customers values ('cust4', 'Anthony Gonzalez', to_date('1977-10-06', 'yyyy-mm-dd'), NULL)")
conn.commit()

printAll("After inserting cust4")

print("Updating cust4's name to 'Tony Gonzalez' in customers table")
cur.execute("UPDATE customers set name = 'Tony Gonzalez' where customerid='cust4'")
conn.commit()

printAll("After updating name")

print("Updating cust4's frequentflieron to DL in customers table")
cur.execute("UPDATE customers set frequentflieron = 'DL' where customerid='cust4'")
conn.commit()

printAll("After update of frequentflieron")

print("Updating cust4's frequentflieron to NULL in customers table")
cur.execute("UPDATE customers set frequentflieron = NULL where customerid='cust4'")
conn.commit()

printAll("After updating frequentflieron")

print("Now deleting cust4")
cur.execute("DELETE from customers where customerid = 'cust4'")
conn.commit()

printAll("After deletion")




print("------------------- CONTINUING WITH OPERATIONS ON NEWCUSTOMERS -------------------")


print("Now deleting cust15")
cur.execute("DELETE from customers where customerid = 'cust15'")
conn.commit()

printAll("After deletion")

print("Inserting ('cust4', 'Anthony Gonzalez', to_date('1977-10-06', 'yyyy-mm-dd')) into newcustomers table")
cur.execute("INSERT into newcustomers values ('cust4', 'Anthony Gonzalez', to_date('1977-10-06', 'yyyy-mm-dd'))")
conn.commit()

printAll("After inserting cust4")

print("Updating cust4's name to 'Tony Gonzalez' in newcustomers table")
cur.execute("UPDATE newcustomers set name = 'Tony Gonzalez' where customerid='cust4'")
conn.commit()

printAll("After updating name")



print("------------------- CONTINUING WITH OPERATIONS ON FFAIRLINES -------------------")

print("Adding cust4's flights to flewon table and after that adding ffairline as AA")
cur.execute("insert into flewon values ('SW132', 'cust4', to_date('2016-08-05', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('AA131', 'cust4', to_date('2016-08-08', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('SW116', 'cust4', to_date('2016-08-03', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('UA101', 'cust4', to_date('2016-08-01', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('SW116', 'cust4', to_date('2016-08-04', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('SW110', 'cust4', to_date('2016-08-02', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('SW106', 'cust4', to_date('2016-08-06', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('UA138', 'cust4', to_date('2016-08-09', 'YYYY-MM-DD'))")
cur.execute("insert into flewon values ('SW107', 'cust4', to_date('2016-08-07', 'YYYY-MM-DD'))")
cur.execute("INSERT into ffairlines values ('cust4', 'AA')")
conn.commit()

printAll('After setting cust4 ff airline as AA')

print('Updating AA to be SW instead for cust4 in ffairlines')
cur.execute("UPDATE ffairlines set airlineid = 'SW' where customerid = 'cust4' and airlineid = 'AA'")

printAll('after adding SW as ff airline')

print("Inserting ('cust4', 'AA') into ffairline for cust4")
cur.execute("INSERT into ffairlines values ('cust4', 'AA')")
conn.commit()

printAll("With AA and SW as ffairlines for cust4")

print('Removing SW as cust4 ff airline')
cur.execute("DELETE from ffairlines where customerid = 'cust4' and airlineid = 'SW'")

printAll('after Removing SW as ff airline')

print('Removing AA as cust4 ff airline')
cur.execute("DELETE from ffairlines where customerid = 'cust4' and airlineid = 'AA'")

printAll('after Removing AA as ff airline')

print("------------------- CONTINUING WITH OPERATIONS ON FLEWON -------------------")


print("Adding both UA and SW as ff airlines for cust4")
cur.execute("INSERT into ffairlines values ('cust4', 'UA')")
cur.execute("INSERT into ffairlines values ('cust4', 'AA')")
conn.commit()

printAll("Initial state")

print("Now removing a single UA flight in flewon for cust 4")
cur.execute("DELETE from flewon where customerid = 'cust4' and flightid = 'UA101'")

printAll("Deleted single UA flight and now there are the same number of flights for UA and AA for cust 4")

print("updating an AA flight to be SW instead")
cur.execute("UPDATE flewon set flightid = 'SW132' where customerid = 'cust4' and flightid = 'AA131'")

printAll("After update")

print("Inserting ('UA101', 'cust4', to_date('2016-08-01', 'YYYY-MM-DD') into flewon")
cur.execute("INSERT into flewon values ('UA101', 'cust4', to_date('2016-08-01', 'YYYY-MM-DD'))")

printAll("After insert")
