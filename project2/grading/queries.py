queries = ["" for i in range(0, 3)]

### 1.
queries[1] = """
SELECT customerid
FROM customers NATURAL LEFT OUTER JOIN (
    SELECT customerid, flightdate 
    FROM flewon 
    WHERE flightdate = date '2016-08-03'
) as flewondate
WHERE flightdate is NULL;
"""


### 2.
queries[2] = """
WITH allflights (airport, airlineid) AS (
    SELECT source, airlineid FROM flights
    UNION ALL
    SELECT dest, airlineid FROM flights
), totalflights (airportid, total) AS (
    SELECT airport, COUNT(*)
    FROM allflights
    GROUP BY airport
), swflights (airportid, sw) AS (
    SELECT airport, COUNT(*)
    FROM allflights
    WHERE airlineid = 'SW'
    GROUP BY airport
)
SELECT name, round(  COALESCE(sw, 0.00) / total    ,2) AS participation
FROM swflights NATURAL RIGHT OUTER JOIN totalflights NATURAL JOIN airports
ORDER BY participation DESC;
"""