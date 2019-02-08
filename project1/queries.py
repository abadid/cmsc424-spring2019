queries = ["" for i in range(0, 11)]
### EXAMPLE
### 0. List all airport codes and their cities. Order by the city name in the increasing order.
### Output column order: airportid, city

queries[0] = """
select airportid, city
from airports
order by city;
"""

### 1. Write a query to find the names of customers who have flights on a wednesday and first name that has a second letter of 'h',
###    and do not include the youngest customer who fits those criteria in the results.
### Hint:  - See postgresql date operators and string functions that are linked to from the README
###        - You can avoid including the youngest customer by joining the customers table with itself (can you figure out the join predicate?).
###        - Try attacking this problem in parts. First, write a query that includes all customers, then modify that query to exclude the youngest.
### Order: by name
### Output columns: name
queries[1] = """

"""


### 2. Write a query to find unqiue customers who are frequent fliers on United Airlines (UA) that have a birthday in March or April.
### Hint: See postgresql date functions and distinct operator. Note that April has 30 days.
### Order: by name
### Output columns: customer id, name, birthdate, frequentflieron
queries[2] = """

"""

### 3. Write a query to find the names of the 10 customers who have the most flights with airlines other than their frequentflieron airline,
### along with the number of times they fly with other airlines. If there are any ties that make the top 10 ranking exceed 10 results
### (ex. the number of most flights is shared by 20 people), just limit the numbers of rows returned to 10.
### Output: (name, count)
### Order: first by count in descending order, then name in ascending order
queries[3] = """

"""

### 4. Write a query to find the names of customers with the most common frequent flier airline. For example, if 10 customers have Delta as their frequent flier airline, and no other airlines have more than 9 frequent flier customers, then the query should return all customers that have Delta as their frequent flier airline. In the case of a tie, return all customers from all tied airlines.
### Hint: use `with clause` and nested queries
### Output: only the names of the customer.
### Order: order by name.
queries[4] = """

"""


### 5. Write a query to find the name(s) of the person/people who flew on flights with Betty Gonzalez the most times. In case of a tie return all people tied. (Same flight id and flight date)
### Output: name
### Order: by name
queries[5] = """

"""

### 6. Write a query to find the percentage participation of Southwest Airlines in each airport, relative to the other airlines.
### One instance of participation in an airport is defined as a flight (EX. SW123) having a source or dest of that airport.
### If SW123 leaves LAX and arrives in JFK, that adds 1 to Southwest's count for each airport
### This means that if SW has 1 in LAX, AA has 2 in LAX, DL has 3 in LAX, and UA has 4 in LAX, the query returns:
###     airport 		    | participation
###     Los Angeles International  | .10
### Output: (airport_name, participation).
### Order: Participation in descending order
### Note: - The airport column must be the full name of the airport
###       - The participation percentage is rounded to 2 decimals, as shown above
###       - You do not need to confirm that the flights actually occur by referencing the flewon table. This query is only concerned with
###         flights that exist in the flights table.
###       - You must leave out airports that have no SW flights (participation of 0)
### Hint: You may find it useful to use the set operation 'union all'

queries[6] = """

"""

### 7. Write a query to find the customers' names that have never flown on their frequent flier airline, but have flown at least 5 other flights.
### Output: Customer name
### Order: name
queries[7] = """

"""

### 8. Write a query to find customers that took flights over three consecutive days, but did not fly any other day. Return the name, start and end date of the customers flights.
### Output: customer_name, start_date, end_date
### Order: by customer_name
queries[8] = """


"""

### 9. Write a query to find all flights that had a layover in IAD between 1 and 3 hours in length (inclusive)
### Output columns: 1st flight id, 2nd flight id, source city, destination city, layover duration
### Order by: layover duration
queries[9] = """

"""

### 10. Provide a top-20 ranking of the most loyal frequent fliers.
### We rank these fliers by the ratio of flights that they take that are with their frequentflieron airline. The customer with the highest ratio of (flights with frequentflieron) / total flights is rank 1, and so on.
### A customer needs at least 5 flights to be considered for the ranking
### Output: (customer_name, rank)
### Order: by the ascending rank, then name
### Note: a) If two customers tie, then they should both get the same rank, and the next rank should be skipped. For example, if the top two customers have the same ratio, then there should be no rank 2, e.g., 1, 1, 3 ...
###       b) This means there may be more than 20 customers in this ranking, so long as their ranks are under 20. This may occur if there are 10 at rank 15, etc.
queries[10] = """


"""
