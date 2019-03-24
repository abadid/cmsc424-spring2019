import psycopg2
import os
import sys
import subprocess
import pprint
import datetime


pp = pprint.PrettyPrinter(indent=3)


def compareAns(correctans, ans):
	correct_cust, correct_newcust, correct_ff = correctans
	cust, newcust, ff = ans
	correct = True
	if len(cust) == len(correct_cust) and len(newcust) == len(correct_newcust) and len(ff) == len(correct_ff):
		for x in correct_cust:
			if x not in cust:
				correct = False

		for x in correct_newcust:
			if x not in newcust:
				correct = False

		for x in correct_ff:
			if x not in ff:
				correct = False
	else:
		correct = False

	return correct


def executePrint(s):
	cur.execute(s)
	pp.pprint(cur.fetchall())

def getAns():
	cur.execute("select * from customers")
	customers =  cur.fetchall()
	cur.execute("select * from newcustomers")
	newcustomers =  cur.fetchall()
	cur.execute("select * from ffairlines")
	ffairlines =  cur.fetchall()
	ans = (customers, newcustomers, ffairlines)
	return ans

def printAll(s):
	print(s)
	print("~~~~~~~~~~CUSTOMERS~~~~~~~~~~")
	executePrint("select * from customers")
	print("~~~~~~~~~~NEWCUSTOMERS~~~~~~~~~~")
	executePrint("select * from newcustomers")
	print("~~~~~~~~~~FFAIRLINES~~~~~~~~~~")
	executePrint("select * from ffairlines")


def resetdb(c, coms):
	c.close()
	subprocess.call(["dropdb", "flighttrigger"])
	subprocess.call(["createdb", "flighttrigger"])
	subprocess.call(["psql", "-f", "trigger-database.sql", "flighttrigger"])
	conn = psycopg2.connect("dbname=flighttrigger user=vagrant")
	cur = conn.cursor()
	for x in coms:
		cur.execute(x)
	conn.commit()
	subprocess.call(["psql", "-f", sys.argv[1], "flighttrigger"])
	return (cur, conn)

def resetdb2(c, coms):
	c.close()
	subprocess.call(["dropdb", "flighttrigger"])
	subprocess.call(["createdb", "flighttrigger"])
	subprocess.call(["psql", "-f", "trigger-database2.sql", "flighttrigger"])
	subprocess.call(["psql", "-f", sys.argv[1], "flighttrigger"])
	conn = psycopg2.connect("dbname=flighttrigger user=vagrant")
	cur = conn.cursor()
	for x in coms:
		cur.execute(x)
	conn.commit()
	return (cur, conn)

if len(sys.argv) != 2:
	print "Usage: trigger-test.py <your trigger SQL file>"
	sys.exit(1)

subprocess.call(["dropdb", "flighttrigger"])
subprocess.call(["createdb", "flighttrigger"])
subprocess.call(["psql", "-f", "trigger-database.sql", "flighttrigger"])
subprocess.call(["psql", "-f", sys.argv[1], "flighttrigger"])
conn = psycopg2.connect("dbname=flighttrigger user=vagrant")
cur = conn.cursor()

totalScore = 0
failedTests = []

print("------------------- OPERATIONS ON CUSTOMERS -------------------")

printAll("Initial state")
try:
	print("TEST 1-1: Insert of customer into customers table")
	cur.execute("INSERT into customers values ('cust4', 'Anthony Gonzalez', to_date('1977-10-06', 'yyyy-mm-dd'), 'AA')")
	conn.commit()
	correctans = ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6), None)], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22)), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA'), ('cust4     ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 1-1: Insert of customer into customers table")
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 1-1: Insert of customer into customers table")
printAll("After inserting cust4. customer should be present in all tables")
cur, conn = resetdb(conn, [])

try:
	print("TEST 1-2: Insert of customer into customers table with NULL frequentflieron")
	cur.execute("INSERT into customers values ('cust4', 'Anthony Gonzalez', to_date('1977-10-06', 'yyyy-mm-dd'), NULL)")
	conn.commit()
	correctans = ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6), None)], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22)), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 1-2: Insert of customer into customers table with NULL frequentflieron")
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 1-2: Insert of customer into customers table with NULL frequentflieron")
printAll("After inserting cust4. Should be present in customers and newcustomers but not ffairlines")
cur, conn = resetdb(conn, [])
try:
	print("TEST 1-3: Deleting a customer from customers table")
	cur.execute("DELETE from customers where customerid = 'cust0'")
	conn.commit()
	correctans = ([('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA')], [('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22))], [('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 1-3: Deleting a customer from customers table")
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 1-3: Deleting a customer from customers table")
printAll("After deletion. cust0 should not be in any table")
cur, conn = resetdb(conn, [])
try:
	print("TEST 1-4: Update of name of customer in customers table")
	cur.execute("UPDATE customers set name = 'Tony Allen' where customerid='cust0'")
	conn.commit()
	correctans = ([('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust0     ', 'Tony Allen                    ', datetime.date(1985, 5, 14), 'AA')], [('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22)), ('cust0     ', 'Tony Allen                    ', datetime.date(1985, 5, 14))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 1-4: Update of name of customer in customers table")
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 1-4: Update of name of customer in customers table")
printAll("After updating name.  Update should be seen in both customer tables")
cur, conn = resetdb(conn, ["INSERT into customers values ('cust4', 'Anthony Gonzalez', to_date('1977-10-06', 'yyyy-mm-dd'), NULL)", "INSERT into newcustomers values ('cust4', 'Anthony Gonzalez', to_date('1977-10-06', 'yyyy-mm-dd'))"])
try:
	print("TEST 1-5: Update of frequentflieron of customer in customers table; no flights")
	cur.execute("UPDATE customers set frequentflieron = 'DL' where customerid='cust4'")
	conn.commit()
	correctans = ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6), None)], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22)), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA'), ('cust4     ', 'DL')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 1-5: Update of frequentflieron of customer in customers table; no flights")
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 1-5: Update of frequentflieron of customer in customers table; no flights")
printAll("After update of frequentflieron to DL for cust4. Still no flights for cust4 so customers frequentflieron cloumn should be null still")
cur, conn = resetdb(conn, [])
try:
	print("TEST 1-6: Update of frequentflieron of customer in customers table; with change in frequentflieron")
	cur.execute("UPDATE customers set frequentflieron = 'UA' where customerid='cust33'")
	conn.commit()
	correctans =  ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'UA')], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA'), ('cust33    ', 'UA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 1-6: Update of frequentflieron of customer in customers table; with change in frequentflieron")
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 1-6: Update of frequentflieron of customer in customers table; with change in frequentflieron")
printAll("After update of frequentflieron to DL for cust4. Still no flights for cust4 so customers frequentflieron cloumn should be null still")
cur, conn = resetdb(conn, [])
try:
	print("TEST 1-7: Update of frequentflieron of customer in customers table; with no change in frequentflieron")
	cur.execute("UPDATE customers set frequentflieron = 'AA' where customerid='cust15'")
	conn.commit()
	correctans = ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW')], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA'), ('cust15    ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 1-7: Update of frequentflieron of customer in customers table; with no change in frequentflieron")
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 1-7: Update of frequentflieron of customer in customers table; with no change in frequentflieron")
printAll("After update of frequentflieron to DL for cust4. Still no flights for cust4 so customers frequentflieron cloumn should be null still")
cur, conn = resetdb(conn, [])
try:
	print("TEST 1-8: Update of frequentflieron of customer to NULL in customers table")
	cur.execute("UPDATE customers set frequentflieron = NULL where customerid='cust0'")
	conn.commit()
	correctans = ([('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), None)], [('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22)), ('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14))], [('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 2
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 1-8 (2pts): Update of frequentflieron of customer to NULL in customers table")
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 1-8 (2pts): Update of frequentflieron of customer to NULL in customers table")
printAll("After updating frequentflieron to null. This should delete all entries for cust4 in ffairlines")
cur, conn = resetdb(conn, [])


print("------------------- CONTINUING WITH OPERATIONS ON NEWCUSTOMERS -------------------")
try:
	print("TEST 2-1: Delete from newcustomers table")
	cur.execute("DELETE from newcustomers where customerid = 'cust15'")
	conn.commit()
	correctans =  ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA')], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22))], [('cust0     ', 'AA'), ('cust33    ', 'DL'), ('cust109   ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 2-1: Delete from newcustomers table")
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 2-1: Delete from newcustomers table")
printAll("After deletion, cust15 should not appear in any table")
cur, conn = resetdb(conn, [])
try:
	print("TEST 2-2: Insert into newcustomers table")
	cur.execute("INSERT into newcustomers values ('cust4', 'Anthony Gonzalez', to_date('1977-10-06', 'yyyy-mm-dd'))")
	conn.commit()
	correctans =  ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6), None)], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22)), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 2-2: Insert into newcustomers table")
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 2-2: Insert into newcustomers table")
printAll("After inserting cust4, should be in both customer tables but not ffairlines")
cur, conn = resetdb(conn, [])
try:
	print("TEST 2-3: Update of name of customer in newcustomers table")
	cur.execute("UPDATE newcustomers set name = 'Tony Allen' where customerid='cust0'")
	conn.commit()
	correctans = ([('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust0     ', 'Tony Allen                    ', datetime.date(1985, 5, 14), 'AA')], [('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22)), ('cust0     ', 'Tony Allen                    ', datetime.date(1985, 5, 14))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 2-3: Update of name of customer in newcustomers table")
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 2-3: Update of name of customer in newcustomers table")
printAll("After updating name, Update should appear in both customer tables")
cur, conn = resetdb2(conn, [])



print("------------------- CONTINUING WITH OPERATIONS ON FFAIRLINES -------------------")
coms = []
try:
	print("TEST 3-1: Adding first entry for a customer into ffairlines table")
	cur.execute("INSERT into ffairlines values ('cust4', 'AA')")
	conn.commit()
	correctans = ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6), 'AA')], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA'), ('cust4     ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 3-1: Adding first entry for a customer into ffairlines table")
	coms.append("INSERT into ffairlines values ('cust4', 'AA')")
	cur, conn = resetdb2(conn, coms)
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 3-1: Adding first entry for a customer into ffairlines table")
printAll('After setting cust4 ff airline as AA. frequentflieron in customer should also be AA')
try: 
	print('TEST 3-2: Updating single entry in ffairlines table')
	cur.execute("UPDATE ffairlines set airlineid = 'SW' where customerid = 'cust4' and airlineid = 'AA'")
	correctans = ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6), 'SW')], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA'), ('cust4     ', 'SW')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 3-2: Updating single entry in ffairlines table")
	coms.append("UPDATE ffairlines set airlineid = 'SW' where customerid = 'cust4' and airlineid = 'AA'")
	cur, conn = resetdb2(conn, coms)
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 3-2: Updating single entry in ffairlines table")
printAll('after updating AA to SW as ff airline.  SW should now be the frequentflieron for cust4')
try:
	print("TEST 3-3: Adding a second entry for customer in ffairlines table")
	cur.execute("INSERT into ffairlines values ('cust4', 'AA')")
	conn.commit()
	correctans = ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6), 'SW')], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA'), ('cust4     ', 'SW'), ('cust4     ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 3-3: Adding a second entry for customer in ffairlines table")
	coms.append("INSERT into ffairlines values ('cust4', 'AA')")
	cur, conn = resetdb2(conn, coms)
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 3-3: Adding a second entry for customer in ffairlines table")
printAll("With AA and SW as ffairlines for cust4,  It should still be SW for frequentflieron because cust4 took more SW flights")
try:
	print('TEST 3-4: Delete a single entry in ffairlines for a customer')
	cur.execute("DELETE from ffairlines where customerid = 'cust4' and airlineid = 'SW'")
	correctans = ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6), 'AA')], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA'), ('cust4     ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 3-4: Delete a single entry in ffairlines for a customer")
	coms.append("DELETE from ffairlines where customerid = 'cust4' and airlineid = 'SW'")
	cur, conn = resetdb2(conn, coms)
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 3-4: Delete a single entry in ffairlines for a customer")
printAll('after Removing SW as ff airline it should be AA again for frequentflieron')
try:
	print('TEST 3-5: Delete all entries for a customer in ffairlines table')
	cur.execute("DELETE from ffairlines where customerid = 'cust4' and airlineid = 'AA'")
	correctans = ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6), None)], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 3-5: Delete all entries for a customer in ffairlines table")
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 3-5: Delete all entries for a customer in ffairlines table")
printAll('after Removing AA as ffairline.  Now it should be null because cust4 has no entries in fffairlines')

cur, conn = resetdb2(conn, [])

print("------------------- CONTINUING WITH OPERATIONS ON FLEWON -------------------")

cur.execute("INSERT into ffairlines values ('cust4', 'UA')")
cur.execute("INSERT into ffairlines values ('cust4', 'AA')")
conn.commit()
coms = []
coms.append("INSERT into ffairlines values ('cust4', 'UA')")
coms.append("INSERT into ffairlines values ('cust4', 'AA')")

try:
	print("TEST 4-1: Delete a flight from flewon table")
	cur.execute("DELETE from flewon where customerid = 'cust4' and flightid = 'UA101'")
	correctans = ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6), 'AA')], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA'), ('cust4     ', 'UA'), ('cust4     ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 4-1: Delete a flight from flewon table")
	coms.append("DELETE from flewon where customerid = 'cust4' and flightid = 'UA101'")
	cur, conn = resetdb2(conn, coms) 
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 4-1: Delete a flight from flewon table")
printAll("Deleted single UA flight and now there are the same number of flights for UA and AA for cust 4")
try:
	print("TEST 4-2: Update of flightid in flewon table to change to a different airline")
	cur.execute("UPDATE flewon set flightid = 'SW132' where customerid = 'cust4' and flightid = 'AA131'")
	correctans =  ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6), 'UA')], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA'), ('cust4     ', 'UA'), ('cust4     ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 4-2: Update of flightid in flewon table to change to a different airline")
	coms.append("UPDATE flewon set flightid = 'SW132' where customerid = 'cust4' and flightid = 'AA131'")
	cur, conn = resetdb2(conn, coms) 
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 4-2: Update of flightid in flewon table to change to a different airline")
printAll("After update there are more UA flights than AA flights for cust4")
try:
	print("TEST 4-3: Insert of new flight into flewon table that doesn't change frequentflieron")
	cur.execute("INSERT into flewon values ('UA101', 'cust4', to_date('2016-08-01', 'YYYY-MM-DD'))")
	correctans = ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6), 'UA')], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA'), ('cust4     ', 'UA'), ('cust4     ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 4-3: Insert of new flight into flewon table that doesn't change frequentflieron")
	coms.append("INSERT into flewon values ('UA101', 'cust4', to_date('2016-08-01', 'YYYY-MM-DD'))")
	cur, conn = resetdb2(conn, coms) 
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 4-3: Insert of new flight into flewon table that doesn't change frequentflieron")
printAll("After insert UA is still the greatest")
try:
	print("TEST 4-4: Insert of new flights into flewon table that does change frequentflieron")
	cur.execute("INSERT into flewon values ('AA131', 'cust4', to_date('2016-08-09', 'YYYY-MM-DD'))")
	cur.execute("INSERT into flewon values ('AA131', 'cust4', to_date('2016-08-10', 'YYYY-MM-DD'))")
	cur.execute("INSERT into flewon values ('AA131', 'cust4', to_date('2016-08-11', 'YYYY-MM-DD'))")
	correctans = ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6), 'AA')], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA'), ('cust4     ', 'UA'), ('cust4     ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 4-4: Insert of new flights into flewon table that does change frequentflieron")
	coms.append("INSERT into flewon values ('AA131', 'cust4', to_date('2016-08-09', 'YYYY-MM-DD'))")
	coms.append("INSERT into flewon values ('AA131', 'cust4', to_date('2016-08-10', 'YYYY-MM-DD'))")
	coms.append("INSERT into flewon values ('AA131', 'cust4', to_date('2016-08-11', 'YYYY-MM-DD'))")
	cur, conn = resetdb2(conn, coms) 
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 4-4: Insert of new flights into flewon table that does change frequentflieron")
printAll("After insert AA is the greatest")

try:
	print("TEST 4-5: DELETE all flights for a customer")
	cur.execute("DELETE from flewon where customerid = 'cust4'")
	correctans = ([('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14), 'AA'), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28), 'SW'), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13), 'DL'), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22), 'AA'), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6), None)], [('cust0     ', 'Anthony Allen                 ', datetime.date(1985, 5, 14)), ('cust4     ', 'Anthony Gonzalez              ', datetime.date(1977, 10, 6)), ('cust15    ', 'Betty Gonzalez                ', datetime.date(1993, 12, 28)), ('cust33    ', 'Christopher Davis             ', datetime.date(1984, 5, 13)), ('cust109   ', 'James Adams                   ', datetime.date(1994, 5, 22))], [('cust0     ', 'AA'), ('cust15    ', 'SW'), ('cust33    ', 'DL'), ('cust109   ', 'AA'), ('cust4     ', 'UA'), ('cust4     ', 'AA')])
	if compareAns(correctans, getAns()):
		totalScore += 1
	else:
		print(getAns())
		print("-----")
		print(correctans)
		failedTests.append("FAILED: TEST 4-5: DELETE all flights for a customer")
	printAll("frequentflieron should be null now")
except Exception as e:
	print(e)
	conn.commit()
	failedTests.append("ERROR: TEST 4-5: DELETE all flights for a customer")






print("-------------------RESULTS-------------------")

for s in failedTests:
	print(s)

print(totalScore)