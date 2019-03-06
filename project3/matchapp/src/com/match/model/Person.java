package com.match.model;

import com.match.model.Organ;
import java.sql.*;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Arrays;
import java.util.Map;
import java.lang.NullPointerException;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import com.fasterxml.jackson.core.*;
import com.fasterxml.jackson.databind.*;
import java.io.File;
import java.io.IOException;

public class Person {

	static Connection con = null;
	/*Fields for a person entry in the person table
	remember to add one of your own choice of fields
	*/
	private String firstName, lastName, bloodtype, birthdate;
	private int doctor;

	private String[] needs;
	private String[] donations;

	//used for logging output, see catalina.out for log files
	private static final Logger logger = LogManager.getLogger("match");
	static JsonFactory factory = new JsonFactory();

	public Person() {

	}

	//constructor for person if only need to display the name
	public Person(String firstName, String lastName) {
		this.firstName = firstName;
		this.lastName = lastName;
	}

	//constructor for person with all inital fields
	public Person(String firstName, String lastName, String birthdate, String bloodtype) {
		this.firstName = firstName;
		this.lastName = lastName;
		this.birthdate = birthdate;
		this.bloodtype = bloodtype;
	}

	//constructor for person with needs or donations
	public Person(String firstName, String lastName, String birthdate, String bloodtype, int doctor, String[] needOrDon, boolean needed) {
		this.firstName = firstName;
		this.lastName = lastName;
		this.birthdate = birthdate;
		this.bloodtype = bloodtype;
		this.doctor = doctor;
		if (needed) {
			this.needs = needOrDon;
		} else {
			this.donations = needOrDon;
		}
	}

	public String getFirstName() {
		return firstName;
	}

	public String getLastName() {
		return lastName;
	}

/*
	Return an array of all the people in the person table
	You will need to make a SQL call via JDBC to the database to get all of the people
	Since the webpage only needs to display the person's first and last name, only those fields
	of the Person object need to be instantiated (i.e., you can use the second of the three Person constructors above)
	Order does not matter.
*/
	public static Person[] getPeople() {

		con = getConnection();

		if (con == null) {
			logger.warn("Connection Failed!");
			Person failed = new Person("Connection", "Failed");
			return new Person[] { failed };
		}

		return new Person[]{};

	}

	/* For every person record in the database, search each of its character fields to see if input query is a substring of any of them
	Return everything that matches with every char/varchar column. This should be case senstive in finding substring matches

	For example if we have 2 people with:
	First: Alex, Last: Westave, bloodtype: O-
	First: Dave, Last: Howland, bloodtype: AB

	If we query with the string: "ave", the Person array that is returned contains both people
	If we query with the string: "West", the Person array that is returned contains just Alex
	If we query with the string: "COUNT", the Person array is empty

	The order of the people returned does not matter.

	Once again you only have to return first and last name.

	If no rows in the database are found with a substring match, you should return an empty array of Person.

	You must use a prepared statement.
	*/
	public static Person[] getPersonSearch(String query) {

		con = getConnection();

		if (con == null) {
			logger.warn("Connection Failed!");
			Person failed = new Person("Connection", "Failed");
			return new Person[] { failed };
		}

		return new Person[]{};
	}

	/*This should return a Person object with all of its fields instantiated
	for the person with the given id in the person table. Note that since id is unique, there
	will only be one person ever returned by this method

	Return a person with the first name "No" and the last name "Matches" if
	the person with the id does not exist.

	You do not need to use a prepared statement (but you still can!).
	*/
	public static Person getPerson(String pid) {

		con = getConnection();

		if (con == null) {
			logger.warn("Connection Failed!");
			Person failed = new Person("Connection", "Failed");
			return failed;
		}

		return new Person("No", "Matches");
	}

	/*Add a person to the database with all of the fields specified.

	Do not update the user's doctor_id in this method, simply leave it null in this method. That will be taken care of in AddPerson.java.

	If the connection fails or the person was not inserted, return -1, otherwise return the id of the person that you inserted.

	You must use a prepared statement to insert the person.
	*/
	public static int addPerson(String first, String last, String birthdate, String bloodtype) {

		con = getConnection();

		if (con == null) {
			logger.warn("Connection Failed!");
			return -1;
		}

		return -1;
	}

	/*Return a list of all donors with organ matches in the database for the person with the given id based on the
	blood type compatibility and type of organ needed. If the person needs more than
	one organ, return all matches for all organs needed.

	A person is not allowed to be matched with herself or himself.

	If the person with id does not exist, return a Person array with one person with the first name "No" and last name "Matches"
	If the person has no matches, return an empty Person array.
	If the person doesn't need an organ, return an empty Person array.

	You must use a prepared statement.
	*/

	public static Person[] getOrganMatches(String id) {

		con = getConnection();
		// If that fails, send dummy entries
		if (con == null) {
			logger.warn("Connection Failed!");
			Person failed = new Person("Connection", "Failed");
			return new Person[] { failed };
		}

		return new Person[] {};
	}

	/*
	Use this method to add a needed organ 'o' into the database. The person who needs
	the organ is given by their id. A person should not be able to submit a request for 2
	of the same organ.

	Do not update the person's doctor_id in this method. That will be taken care of in AddRequest.java.

	You must use a prepared statement.

	Return 1 on success or -1 otherwise.
	*/
	public static int addNeededOrgan(Organ o, int pid, String byDate) {

		con = getConnection();

		if (con == null) {
			logger.warn("Connection Failed!");
			return -1;
		}

		return -1;
	}

	/*
	Use this method to add an available organ o into the database. The person who can give
	the organ is given by their id. A person should not be able to offer more than one
	of each organ.

	Do not update the person's doctor_id in this method. That will be taken care of in AddOffer.java.

	Return 1 on success or -1 otherwise.

	You must use a prepared statement.
	*/
	public static int addAvailableOrgan(Organ o, int pid) {

		con = getConnection();

		if (con == null) {
			logger.warn("Connection Failed!");
			return -1;
		}

		return -1;
	}

	/*
	Fill in this method to check if person donorID can satisfy person needID's needs for
	an organ. This means the organ must match and person alt's bloodtype must be
	compatible with person p's (use checkBloodType() function).

	You do not need to use prepared statements.
	*/
	public static boolean computeOrganMatch (int needID, int donorID){

		con = getConnection();

		if (con == null) {
			logger.warn("Connection Failed!");
			return false;
		}

		return false;
	}

	/* This method will assign a doctor to a person as they sign up for the first time.

	You will assign a doctor to a person by updating the person's doctor_id field with
	the doctor with the fewest patients. The number of patients is defined as the number of
	people assigned to that doctor through their doctor_id field. To break ties, choose
	the doctor with the smallest id.

	pid = person id

	You must use prepared statements.
	*/
	public static int getDoctorFirst (int pid) {

	    con = getConnection();

	    if (con == null) {
	        logger.warn("Connection Failed!");
	        return -1;
	    }

	   return -1;
	}


	/*
	Fill in this method to assign a doctor to the given person following an organ
	request or offer. This function will run each time a person requests or offers an organ.
	The way to assign a proper doctor is to find the doctor with the
	fewest patients, who also has the same specialty as their requested/offered organ.
	You should use more experience as a tiebreaker. If two doctors are still tied,
	choose the doctor with the smallest id.

	note: the patient will already be assigned a doctor from either signup or a previous
	request/offer. DO NOT include the patient you are updating in the count of their doctor's patients.

	Make sure you update the correct person entry in the database with the assigned
	doctor id.

	Example: A person request a Heart

	Name: Abrams, Specialty: Hearts, Experience: 10, # of patients: 3
	Name: Scott, Specialty: Hearts, Experience: 5, # of patients: 3
	Name, Delagdo, Specialty: Hearts, Experience: 10, # of patients: 3

	This should return the id of Abrams, since they have the fewest patients, most
	experience, and their name comes before Delgado's aphabetically.

	You must use prepared statements.
	*/
	public static int getDoctorUpdate (Organ o, int pid) {
		con = getConnection();

	    if (con == null) {
	        logger.warn("Connection Failed!");
	        return -1;
	    }

		return -1;
	}

	/*
	Get the name of a patient's doctor, given the patient's id.

	You must use a prepared statement.
	*/
	public static String getDoctorName(int pid){
		con = getConnection();

		if (con == null) {
			logger.warn("Connection Failed!");
			return "No connection";
		}

		return "NOT IMPLEMENTED";
	}

	private static Connection getConnection() {
		// Return existing connection after first call
		if (con != null) {
			return con;
		}
		logger.trace("Getting database connection...");
		// Get RDS connection from environment properties provided by Elastic Beanstalk
		con = getRemoteConnection();
		// If that fails, attempt to connect to a local postgres server
		if (con == null) {
			con = getLocalConnection();
		}
		// If that fails, give up
		if (con == null) {
			return null;
		}
		// Attempt to initialize the database on first connection
		//initDatabase();
		return con;
	}

	//Used for AWS connection to DB, not used locally!
	private static Connection getRemoteConnection() {
		/* Read database info from /tmp/database.json (advanced, more secure option)
		* - Requires database.config to be moved into .ebextensions folder and updated to
		* point to a JSON file in an S3 bucket that the instance profile has permission to read.
		*/
		try {
			/* Load the file and create a parser. If the project is not configured to store
			* database credentials in S3, fail out and try the next method.
			*/
			File databaseConfig = new File("/tmp/database.json");
			JsonParser parser = factory.createParser(databaseConfig);
			// Load the Postgresql driver class
			Class.forName("org.postgresql.Driver");
			/* Read the first value in the JSON document with Jackson. This must be a full JDBC
			*  connection string a la jdbc:postgresql://hostname:port/dbName?user=userName&password=password
			*/
			JsonToken jsonToken = null;
			while ( jsonToken != JsonToken.VALUE_STRING )
			jsonToken = parser.nextToken();
			String jdbcUrl = parser.getValueAsString();
			// Connect to the database
			logger.trace("Getting remote connection with url from database config file.");
			Connection con = DriverManager.getConnection(jdbcUrl);
			logger.info("Remote connection successful.");
			return con;
		}
		catch (IOException e) { logger.warn("Database configuration file not found. Checking environment variables.");}
		catch (ClassNotFoundException e) { logger.warn(e.toString());}
		catch (SQLException e) { logger.warn(e.toString());}

		// Read database info from environment variables (standard configration)
		if (System.getProperty("RDS_HOSTNAME") != null) {
			try {
				Class.forName("org.postgresql.Driver");
				String dbName = System.getProperty("RDS_DB_NAME");
				String userName = System.getProperty("RDS_USERNAME");
				String password = System.getProperty("RDS_PASSWORD");
				String hostname = System.getProperty("RDS_HOSTNAME");
				String port = System.getProperty("RDS_PORT");
				String jdbcUrl = "jdbc:postgresql://" + hostname + ":" + port + "/" + dbName + "?user=" + userName + "&password=" + password;
				logger.trace("Getting remote connection with connection string from environment variables.");
				Connection con = DriverManager.getConnection(jdbcUrl);
				logger.info("Remote connection successful.");
				return con;
			}
			catch (ClassNotFoundException e) { logger.warn(e.toString());}
			catch (SQLException e) { logger.warn(e.toString());}
		}
		return null;
	}

	/* Connect to the local database for development purposes
	Your database must be named "matchapp" and you must make a user "matchmaker" with the password "kingofthenorth"
	*/
	private static Connection getLocalConnection() {
		try {
			Class.forName("org.postgresql.Driver");
			logger.info("Getting local connection");
			Connection con = DriverManager.getConnection(
			"jdbc:postgresql://localhost/matchapp",
			"matchmaker",
			"kingofthenorth");
			logger.info("Local connection successful.");
			return con;
		}
		catch (ClassNotFoundException e) { logger.warn(e.toString());}
		catch (SQLException e) { logger.warn(e.toString());}
		return null;
	}

	/*
		This given function returns true if donType can be given to recType successfully
		and false otherwise.
	 */
	public static boolean checkBloodType(String recType, String donType) {

		//start with two catch-alls
		if (donType.equals("O-") || recType.equals("AB+")) {
			return true;
		}

		//all types can donate to themselves
		if (donType.equals(recType)) {
			return true;
		}

		//A-, O+, AB+, O-, B- are satisfied by catch-alls

		//check A+
		if (recType.equals("A+")) {
			if (donType.equals("A-") || donType.equals("O+")) {
				return true;
			} else {
				return false;
			}
		}


		//check B+
		if (recType.equals("B+")) {
			if (donType.equals("B-") || donType.equals("O+")) {
				return true;
			} else {
				return false;
			}
		}

		//check AB-
		if (recType.equals("AB-")) {
			if (donType.equals("A-") || donType.equals("B-")) {
				return true;
			} else {
				return false;
			}
		}

		return false;
	}


}
