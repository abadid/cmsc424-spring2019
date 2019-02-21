## Project 2: Advanced SQL Assignment, CMSC424, Spring 2019

*The assignment is to be done by yourself.*

Please do a `git pull` to download the directory `project2`. The files are:

1. README.md: This file
1. small.sql: SQL script for populating `flights` database.
1. queries.py: The file where to enter your answers for Q1 and Q2; this file has to be submitted
1. answers.py: The answers to query Q1 and Q2.
1. answers.txt: Put your answer to Q3 here; this file has to be submitted.
1. SQLTesting.py: File to be used for testing your SQL submission -- see below 
1. trigger-database.sql: SQL script for setting up the `flighttrigger` database.
1. trigger-test.py: Python script for testing the trigger.
1. Vagrantfile: Vagrantfile that creates the required databases and populates some of them.

### Getting started
Start the VM with `vagrant up` in the `project2/` directory. The database `flights` should already be set up. The `flightstrigger` database is already created for you, but you need to populate it explicitly. 

### Testing and submitting using SQLTesting.py
- Your answers (i.e., SQL queries) should be added to the `queries.py` file similar to Project 1. You are also provided with a Python file `SQLTesting.py` for testing your answers.

- We recommend that you use `psql` to design your queries, and then paste the queries to the `queries.py` file, and confirm it works.

- SQLTesting takes quite a few options: use `python SQLTesting.py -h` to see the options.

- If you want to test your answer to Question 1, use: `python SQLTesting.py -dbname flights -q 1`. The program compares the result of running your query against the provided answer (in the `answers.py` file).

- The -v flag will print out more information, including the correct and submitted answers etc.

### Submission Instructions
- Submit your answers to Q1 in `queries.py`
- Submit your answers to Q2, Q3 in `answers.txt`
- Submit your answer to Q4 in `trigger.sql`

<br />


**Q1 (5pt)**. [Outer Join] Write a query that uses an outer join to list all the customers who did not take a flight on August 3, 2016. [Output Column: `customerid`]

**Q2 (5pt)**. [Outer Join]  Write a query to find the percentage participation of Southwest Airlines in each airport, relative to the other airlines.  One instance of participation in an airport is defined as a flight (EX. SW123) having a source or dest of that airport. If SW123 leaves LAX and arrives in JFK, that adds 1 to Southwest's count for each airport.  This means that if SW has 1 in LAX, AA has 2 in LAX, DL has 3 in LAX, and UA has 4 in LAX, the query returns:

| airport | participation |
| :---: | :---: |
|Los Angeles International  | .10 |

Output: (airport_name, participation).
Order: Participation in descending order
Note: 
1. The airport column must be the full name of the airport <br />
1. The participation percentage is rounded to 2 decimals, as shown above <br />
1. You do not need to confirm that the flights actually occur by referencing the flewon table. This query is only concerned with flights that exist in the flights table. 
1. This is the same query 6 from project 1. The only difference is that we now include airports with 0 participation 

**Q3 (8pt)**. [Outer Join] We will write a query using outer joins to find all the customers who satisfy all the following conditions  
  1. are born in or after 1996, and  
  1. have taken a flight at least once, and  
  1. have never taken a flight in or out of ‘ORD’.

Note that your query should **only use** the following views which are defined as:

```
create view customer_flight as
select distinct c.customerid as cid, flightid
from customers c, flewon f
where c.customerid = f.customerid and extract(year from birthdate) >= 1996
order by cid, flightid;
	
create view flight_ORD as
select flightid from flights
where source = 'ORD' or dest = 'ORD'
order by flightid;
```

The `customer_flight` view lists all the customers who are born in or after 1996 and the flightid of the flights that the customer has taken. The `flight_ORD` view lists all the flights that fly in or out of ORD.

```
with temp as (
select distinct cid, v2.flightid as afid
from customer_flight v1 left outer join flight_ORD v2
on v1.flightid = v2.flightid
order by cid
)
select cid
from temp
group by cid
having count(*)=1
order by cid;
```

Does the query work for all cases? Explain. If not, modify the above query to produce the correct output. If you modify the query, you can only change the having clause. Right now it says: `having count(*)= 1`. You can change it to say: `having count(*) = 1 AND exists (<write your expression here>)`. You cannot change any other part of the query.




**Q4 (22pt)**.[Trigger]

For this problem you are a database administrator who needs to deal with an issue with the current schema in the flights database.  Today's customers have multiple frequent flier airline memberships. However, the flights schema only allows one frequent flier airline per customer.  To fix the issue, we're going to evolve the database to a new schema.  We decide to delete the frequentflieron column from the `customers` table and instead store customer frequenet flier information in a new table: `ffairlines (customerid, airlineid)`. By storing this information in a seperate table, if a customer has more than one frequent flier airline, this information can be represented as multiple rows in this new ffairlines table.

Unfortuantely there are several apps that are using this schema, and some of them need some time before they can update their code to move to the new schema. In the meantime, they want to use the old schema. On the other hand, other apps need to use the new schema right away. We can't use views to solve this problem since both the apps that want to use the old schema and the apps that want to use the new schema want to insert new records into their respective schemas (see the discussion in the textbook about inserting data into views). 


We can solve this using triggers!  We'll keep the old customers table around. And we'll give the new customers table a different name `newcustomers`. Originally it is populated with data from the original customers table (without the frequentflieron column which instead will be populated in the new ffairline table). 

You need to write triggers that do the following:
1. Whenever an app inserts/updates/deletes data into the `customers` table, a trigger is fired that does the same corresponding action for the copy of the data in the `newcustomers` and `ffairline` tables.  On inserts into the `customers` table the value for frequentflieron should result on an insertion into `ffairlines` of (customer, frequentflieron).  If frequentflieron is NULL you should NOT add (customerid, NULL) to the `ffairlines` table.  If frequentflieron is updated to NULL then delete all entries in `ffairlines` for that customer
1. Whenever an app inserts/updates/deletes data into the `newcustomers` table, a trigger is fired that does the same corresponding action for the copy of the data in the `customers` table. The value of the `frequentflieron` column in the `customers` table is the most frequently travelled airline for that customer (based on the record in the `flewon` table) that is one of the frequent flier airlines for that customer as listed in the new `ffairline` table (or null if there are no frequent flier airlines for that customer). In the case of a tie, the one that is smallest lexicographically is chosen. 
1. We also need a trigger on the new `ffairline` table to update the value of the ffairline column of the old customers table if the value should change as a result of the update to the ffairline table.
1. Since the flewon table can affect the choice of which airline should be listed as the `frequentflieron` value in the old customers table, we also need a trigger on the flewon table if as as result of the insert/update/delete to the table, the `frequentflieron` value needs to be changed in the old customers table. 

Here's an example (`flewon` table not shown):

Initially our database looks like this

`customers`

| customerid | name | birthdate | frequentflieron |
| :---: | :---: | :---: | :---: |
| cust0 | Anthony Allen | 1985-05-14 | AA |
| cust12 | Betty Brown | 1975-08-14 | UA |
| cust24 | Carol Clark | 1984-08-24 | DL |
| cust36 | Daniel Baker | 1998-05-27 | SW |
| cust82 | Edward Edwards | 1984-07-15 | DL |

`newcustomers`

| customerid | name | birthdate |
| :---: | :---: | :---: | 
| cust0 | Anthony Allen | 1985-05-14 | 
| cust12 | Betty Brown | 1975-08-14 | 
| cust24 | Carol Clark | 1984-08-24 | 
| cust36 | Daniel Baker | 1998-05-27 | 
| cust82 | Edward Edwards | 1984-07-15 |

`ffairlines`

| customerid | airlineid |
|:---:|:---:| 
| cust0 | AA |
| cust12 | UA |
| cust24 | DL |
| cust36 | SW |
| cust82 | DL |


First, let's delete `(cust82, Edward Edwards, 1984-07-15, DL )` from `customers`, we then have:

`customers`

| customerid | name | birthdate | frequentflieron |
| :---: | :---: | :---: | :---: |
| cust0 | Anthony Allen | 1985-05-14 | AA |
| cust12 | Betty Brown | 1975-08-14 | UA |
| cust24 | Carol Clark | 1984-08-24 | DL |
| cust36 | Daniel Baker | 1998-05-27 | SW |

`newcustomers`

| customerid | name | birthdate |
| :---: | :---: | :---: | 
| cust0 | Anthony Allen | 1985-05-14 | 
| cust12 | Betty Brown | 1975-08-14 | 
| cust24 | Carol Clark | 1984-08-24 | 
| cust36 | Daniel Baker | 1998-05-27 | 

`ffairlines`

| customerid | airlineid |
|:---:|:---:| 
| cust0 | AA |
| cust12 | UA |
| cust24 | DL |
| cust36 | SW |


Next let's insert `(cust102, George Gonzalez, 1996-01-30)` into `newcustomers`, we then have:

`customers`

| customerid | name | birthdate | frequentflieron |
| :---: | :---: | :---: | :---: |
| cust0 | Anthony Allen | 1985-05-14 | AA |
| cust12 | Betty Brown | 1975-08-14 | UA |
| cust24 | Carol Clark | 1984-08-24 | DL |
| cust36 | Daniel Baker | 1998-05-27 | SW |
| cust102 | George Gonzalez | 1996-01-30 |  |

`newcustomers`

| customerid | name | birthdate |
| :---: | :---: | :---: | 
| cust0 | Anthony Allen | 1985-05-14 | 
| cust12 | Betty Brown | 1975-08-14 | 
| cust24 | Carol Clark | 1984-08-24 | 
| cust36 | Daniel Baker | 1998-05-27 | 
| cust102 | George Gonzalez | 1996-01-30 |

`ffairlines`

| customerid | airlineid |
|:---:|:---:| 
| cust0 | AA |
| cust12 | UA |
| cust24 | DL |
| cust36 | SW |


Note: George's frequentflieron column is null in `customers` because we inserted his info into the `newcustomers` table but didn't add any entries in `ffairlines`.

Next let's assume that George takes a lot of flights on Delta so he decides to become a `DL` frequent flier. So we add (cust102, DL) to `ffairlines`. Our table looks like:

`customers`

| customerid | name | birthdate | frequentflieron |
| :---: | :---: | :---: | :---: |
| cust0 | Anthony Allen | 1985-05-14 | AA |
| cust12 | Betty Brown | 1975-08-14 | UA |
| cust24 | Carol Clark | 1984-08-24 | DL |
| cust36 | Daniel Baker | 1998-05-27 | SW |
| cust102 | George Gonzalez | 1996-01-30 | DL |

`newcustomers`

| customerid | name | birthdate |
| :---: | :---: | :---: | 
| cust0 | Anthony Allen | 1985-05-14 | 
| cust12 | Betty Brown | 1975-08-14 | 
| cust24 | Carol Clark | 1984-08-24 | 
| cust36 | Daniel Baker | 1998-05-27 | 
| cust102 | George Gonzalez | 1996-01-30 |

`ffairlines`

| customerid | airlineid |
|:---:|:---:| 
| cust0 | AA |
| cust12 | UA |
| cust24 | DL |
| cust36 | SW |
| cust102 | DL |


Note: We added DL as George's frequent flier airline because it is his most flown airline in the flewon table.

Lastly let's say Betty becomes a South West frequent flier in addition to her United Airlines frequent flier membership.  So we insert (cust12, SW) into `ffairlines`. Our tables look like:

`customers`

| customerid | name | birthdate | frequentflieron |
| :---: | :---: | :---: | :---: |
| cust0 | Anthony Allen | 1985-05-14 | AA |
| cust12 | Betty Brown | 1975-08-14 | SW |
| cust24 | Carol Clark | 1984-08-24 | DL |
| cust36 | Daniel Baker | 1998-05-27 | SW |
| cust102 | George Gonzalez | 1996-01-30 | DL |

`newcustomers`

| customerid | name | birthdate |
| :---: | :---: | :---: | 
| cust0 | Anthony Allen | 1985-05-14 | 
| cust12 | Betty Brown | 1975-08-14 | 
| cust24 | Carol Clark | 1984-08-24 | 
| cust36 | Daniel Baker | 1998-05-27 | 
| cust102 | George Gonzalez | 1996-01-30 |

`ffairlines`

| customerid | airlineid |
|:---:|:---:| 
| cust0 | AA |
| cust12 | UA |
| cust24 | DL |
| cust36 | SW |
| cust102 | DL |
| cust12 | SW |


Note: We updated Betty's frequentflieron airline.  This may not always happen.  By looking at the `flewon` table (not shown here) we saw that Betty flew on more SW flights than UA flights so we updated her frequentflieron.  If we had found that she had flown on more UA flights than SW flights then there would be no changes in the `customers` table.  

Switch to the `flighttrigger` database (i.e. exit out of the flights database and run `psql flighttrigger`). Execute `\i trigger-database.sql` The trigger code should be submitted in `trigger.sql` file. Running `psql -f trigger.sql flighttrigger` should generate the trigger without errors.

You may also use `trigger-test.py`, in which case you do not need to execute `psql -f trigger.sql flighttrigger` (it is included in the script). You can run the test script as `python trigger-test.py trigger.sql`. A few transactions to the `newcustomers` and `ffairlines` table are also provided. You are free to add more transactions for purposes of testing your trigger code. If you are going to run it multiple times.

In the following link, you’ll find some useful trigger examples. https://www.postgresql.org/docs/9.2/static/plpgsql-trigger.html 
https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-INFO-SESSION-TABLE
