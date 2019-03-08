# **Project 3: Matchapp (JDBC Manipulation)**

## **Introduction**

This project should help you gain the skills involved in creating a fully functional web application that interfaces with a database system using JDBC. We will be creating an application that functions as a Craigslist of organ donations. We will be using Java and Tomcat to make this happen in conjunction with a variation of HTML (JSP) to create webpages. You will be a "Full-stack developer" in this project since you will be dealing with all three tiers of a 3-tier architecture: the front-end (presentation tier), the back-end (logic tier), and the database system components of the application!

## **Relevant Project Files**

To begin this project you will have to pull the project 3 folder from our git repo. Below, we give an overview of the important files that you should know about; all of the other files that are included in the code that you pull are just there to make sure that the application works properly:

* **build.sh**: you should run "sudo ./build.sh" in order for your project files to build. This will compile all the necessary files for the application. Make sure you run build as the root user **(sudo)** to have it copy the war file to the tomcat directory properly. Run this AFTER starting tomcat to see our website instead of the default tomcat site.

Make sure to run this every time you change your code in order to recompile it. You should also run it while the server is running (more on that later).

You may encounter an issue with running sudo ./build.sh if you are using Windows to edit build.sh. This might cause issues with carriage return characters and when you try to run it no command runs properly (the first line will be along the lines of "1: cd: can't cd to ./src"). If this happens, you can resolve this by doing the following:

 - Download the program dos2unix on your vagrant machine with: sudo apt-get install dos2unix
 - Run dos2unix build.sh in your vagrant command line

* **src/**

    * **.jsp**: These are the Java Server Pages. JSP allows Java code to be interleaved with static web markup content (HTML in our case), with the resulting page being compiled and executed on the server to deliver a complete HTML page. Basically Java is being used to dynamically create HTML pages. A good overview/tutorial on JSP can be found at: [https://www.tutorialspoint.com/jsp/jsp_overview.htm](https://www.tutorialspoint.com/jsp/jsp_overview.htm) (however, you can skip the parts of the tutorial on how to set up the enviornment, since we’ve already done that for you). It is a good idea to check out the other jsp files we are providing you, so that you can get a sense of how each page of the app is generated. **(Front-end Component)**

    * **com/match/**

        * **model/**

            * **Person.java:** This Java file interfaces with the person table in the matchapp database. We provide basic constructors for a person object but there are several functions missing that you must complete. **(Back-end + DB Component)**

        * **web/**

            * **.java:** These are servlet files that deal with porting over information computed by the **model** files. They help bridge the gap between the back-end and the frontend. **(Back-end + Front-end Components)**

## **Getting Started**

Start the VM with **"vagrant up"**. You will use the database “matchapp” which we created for you. You can quickly start your web application through the following commands:

```bash
$ vagrant up
$ vagrant ssh
vagrant@vagrant-ubuntu-trusty-64:~$ sudo systemctl start tomcat
vagrant@vagrant-ubuntu-trusty-64:~$ sudo systemctl status tomcat
vagrant@vagrant-ubuntu-trusty-64:~$ cd /vagrant/matchapp
# sudo ./build.sh or sudo /bin/bash build.sh
vagrant@vagrant-ubuntu-trusty-64:/vagrant/matchapp$ sudo /bin/bash build.sh
# Navigate to the page localhost:8080 in your browser
```

More technical details are given in the section below. We will be using tomcat to run our server locally. Here are some useful commands to run (run as super user, i.e. “sudo” or “sudo su”):

* `sudo systemctl start tomcat`: Starts your server

* `sudo systemctl status tomcat`: Checks status of your server

* `sudo systemctl stop tomcat`: Stops your server

* `sudo ./build.sh`:  Builds all necessary files and copies your **ROOT.war** file to the right directory

* `sudo tail /opt/tomcat/logs/catalina.out`: Checks log file of tomcat server

* `sudo tail /opt/tomcat/logs/localhost.(current-date)`: Checks log file of localhost

You won't be able to debug this web application with print statements like you would for other programs. With Tomcat, you can print values and errors to the log and view the output they produce in the log file. We have set up the log and have included some uses of the logger in the getConnection method but you may want to add your own statements that log information in the methods you write to debug what your program is doing. [Here](https://logging.apache.org/log4j/2.x/manual/messages.html) is a useful link to using the log with examples.

Basically, you can add `logger.info()` and `logger.trace()` statements to print values when your code runs that you can then view the output of in the catalina.out file. If your application isn't behaving as expected or is crashing, add logging statements to your code and view the log to figure out the issue.

**Run the tomcat start command found above. Then run `sudo ./build.sh`. If your machine gives the error 'command not found', then run `sudo /bin/bash build.sh` instead.**

Navigate to the page `localhost:8080` in your browser (you can use whatever browser you usually use on your computer) to see the website. Take some time to view the different pages and examine the format of the website. You may see some error messages until you get the database set up. Here is which files correspond to which links on the website:

- **404.jsp** - going to any url that is not set up to be a page on the website  
- **default.jsp** - The home page
- **add.jsp** - The Register link
- **request.jsp** - The Request Organ link
- **offer.jsp** - The Offer Organ link
- **people.jsp** - The People link  
- **generate.jsp** - The Find Matches page  
- **invalid_input.jsp** - Page shown if the user enters invalid input in the Register page  
- **matches.jsp** - The View Matches link  

## **Schema + User**

We already created a database called `matchapp` for you. You should run `\i organs.sql` from the psql interface to insert tuples. Make sure you are in the top level of the `/vagrant` directory when you enter the database (`psql matchapp`).

```bash
$ cd /vagrant
$ psql matchapp
matchapp=# \i organs.sql
matchapp=# \q
```

The schema is as follows:

* **person**: [organs.sql#L31-L41](https://github.com/abadid/cmsc424-spring2019/blob/fe1e6cc74182409f8a6b96aa727b2a09b954174c/project3/organs.sql#L31-L41)

    * **id:** This is the primary key of the table, to represent a unique person. This will be of type "serial" which we have not seen yet this semester; this data type auto generates a next unique id to assign to a new person in the table.

    * **first_name:** A string less than or equal to 12 characters long.

    * **last_name:** A string less than or equal to 18 characters long.

    * **birthdate:** A date representing birthdate.

    * **blood_type:** A string representing blood type. See the blood_type table for a list of all possible blood types.

    * **doctor_id:** This is an integer type that references the doctor table's id field.

* **doctors**: [organs.sql#L21-L28](https://github.com/abadid/cmsc424-spring2019/blob/fe1e6cc74182409f8a6b96aa727b2a09b954174c/project3/organs.sql#L21-L28)

    * **id:** **(Primary Key)**  An integer that represents the id of the doctor. This is also of type serial, although you won't be creating any doctors for this project.

    * **name:** String representing the doctor's name.

    * **specialty:** String representing what organ the doctor specializes in.

    * **experience:** int representing how long the doctor has worked for.

* **needs**: [organs.sql#L43-L50](https://github.com/abadid/cmsc424-spring2019/blob/fe1e6cc74182409f8a6b96aa727b2a09b954174c/project3/organs.sql#L43-L50)

    * **id:** **(Primary Key)**  An integer that represents the id of the person with the need. This references the person table.

    * **organ:** **(Primary Key)** String representing what organ the person needs.

    * **by:** date representing when the person needs the organ by.

* **available**: [organs.sql#L52-L58](https://github.com/abadid/cmsc424-spring2019/blob/fe1e6cc74182409f8a6b96aa727b2a09b954174c/project3/organs.sql#L52-L58)

    * **id:** **(Primary Key)**  An integer that represents the id of the person with the organ offer. This references the person table.

    * **organ:** **(Primary Key)** String representing what organ the person needs. References the organs table

* **organs**: [organs.sql#L2-L8](https://github.com/abadid/cmsc424-spring2019/blob/fe1e6cc74182409f8a6b96aa727b2a09b954174c/project3/organs.sql#L2-L8)

    * **organ:** **(Primary Key)**  A string that names an organ.

* **blood_type**: [organs.sql#L10-L19](https://github.com/abadid/cmsc424-spring2019/blob/fe1e6cc74182409f8a6b96aa727b2a09b954174c/project3/organs.sql#L10-L19)

    * **type:** **(Primary Key)**  A string that names a blood type.

You will also have to create a user with name **"matchmaker"** and password **“kingofthenorth”** and you must grant all permissions to that user to access your database and tables as it will be the one doing the database manipulation. Below are the commands to do this (which you can run in psql or add to a .sql file):

```bash
$ psql matchapp
matchapp=# create user matchmaker with password 'kingofthenorth';
matchapp=# grant all privileges on database matchapp to matchmaker;
matchapp=# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO matchmaker;
matchapp=# GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO matchmaker;
matchapp=# \q
```

# Your Tasks

## **Part 1: ER diagram (5 points)**

Please draw an ER diagram that could have been used to generate this schema specified above such that it contains at least one weak entity set. Please do not have organs and blood_type as their own entity sets in your diagram; rather just have them as string fields of other entity sets (for instance, blood_type should be an attribute in the person entity). You should also make the 'available' table into it's own entity set (or weak entity set), rather than a multi-valued attribute of the person's table. Please answer the following questions about your ER diagram via a quiz on ELMS.

- How many entity sets were included in your ER diagram for this application? (You should count weak entity sets as entity sets for the purpose of this question.) 

- Does the needs table correspond to an entity set, a weak entity set, or a relationship set? 

- How many attributes were included in the person set?

- True or False: There are no many-to-many mapping cardinalities in your ER diagram. 

- True or False: There are no total participation constraints in your ER diagram.


We will also ask you to submit your ER diagram as a `.png`, `.jpg`, or `.pdf` file to the quiz on ELMS. Feel free to draw it by hand, take a picture of what you drew, and submit it that way. It will not be graded separately, but only used to justify your answers above.

## **Part 2: Person.java: Back-end + DB (24 points)**

You will need to complete the following methods in the `Person.java` model file that interfaces with the `person table` in the matchapp database. We have already completed a few of these methods, including the constructors as well as functions that interface with your database remotely and locally. You have to complete:

* **getPeople():** Get a list of all the people in the database. (2pts)

* **getPerson(int pid):** Get a specific person given a value for the id attribute. (2pts)

* **getPersonSearch(String substring):** Return people in the Person table that have an attribute that have a substring match with the query.  (3pts)

* **addPerson(String first, String last, String birthdate, String blood_type):** Add a person with the specified values in the person table. Should leave doctor_id null.  (3pts)

* **getOrganMatches(id):** Get everyone who can donate an organ to this person. Should use your `computeOrganMatch()` to check the compatibility of each potential match. (3pts)

* **addNeededOrgan(Organ o, int pid, String byDate):** Add a needed organ to the database for the given person and organ. (2pts)

* **addAvailableOrgan(Organ o, int pid):** Add an available organ to the database for given person and organ. (2pts)

* **computeOrganMatch(int id1,int id2):** Check if the two people given are compatible for a donation. (3pts)

* **getDoctorFirst(pid):** Assign a doctor to a newly registered person. See the method comments for more details on how to do that. (2pts)

* **getDoctorUpdate(Organ o,int pid):** Assign a new doctor to someone who registers an organ. See the method comments for more details on how to do that. (2pts)

The `Person.java` file has comments above each method with more details about what each method should do. We will be testing each of these methods individually to ensure that they produce the output as specified by the comments above each method on a database with different people and doctors that we make. The data we test it on will be exactly the same as the form we have given to you in `organs.sql` --- only the actual values will be different.  

You can add main function in `Person.java` to test each function you modified. For example:

```java
public static void main(String [] args) {
  Person[] persons1 = Person.getPeople();
    for (Person p : persons1) {
      System.out.println(p.getFirstName() + " " + p.getLastName());
    }
}
```

To run `Person.java`:

```bash
cd /vagrant/matchapp/src/WEB-INF
cd ../../ && sudo bash build.sh
cd /vagrant/matchapp/src/WEB-INF
java -classpath "lib/*:classes/.:." com.match.model.Person
```

**The following resources may help you in writing this code:**

[Creating Statements](https://docs.oracle.com/javase/tutorial/jdbc/basics/processingsqlstatements.html#creating_statements)

[Prepared Statements](https://docs.oracle.com/javase/tutorial/jdbc/basics/prepared.html)

## **Part 3: Connecting Back-end + Front-end (6 points)**

Now that you have successfully finished the majority of the back-end (logic tier) components, you will now have to hook up the back-end with the front-end components. This process will be done via the Java files in the **matchapp/src/com/match/web** directory. You will complete the TODO stubs found in the `doPost()` methods of **AddPerson.java**, **AddOffer.java**, and **AddRequest.java**.

## **Part 4: Adding a Page (10 points)**

Finally, we want you to put all of these steps together and add a new page to `OrganTrail`. This page will allow people to find the name of their doctor by entering their person id. Follow these steps to create and add the page to your website:

**Note:** We are giving you some free range here so we will not be grading you strictly on exactly how your html page looks. We will only be testing to see that your page is added and visible on the website and that it meets the functional requirements discussed below. The purpose of this part is to give you experience adding a new feature to the website from start to finish.

1. First, go to the given file `doctor.jsp`. This file will contain the html that we want to display for the page. It is mostly blank right now. You will need to add a form element to display an input box corresponding to the person’s id who you are finding the doctor for. View the comments in the file for more guidance.

2. Now we need to set up an HttpServlet file to display and handle the form data for the jsp file. You want to create a new java file that will extend HttpServlet and contain the void doPost(HttpServletRequest request, HttpServletResponse response) method. This java file should be placed in the `com.match.web` directory. Look at the `AddPerson.java` file for a template on how to create this. Within this file, you need to get the parameters you pass from the request (which will be each field in the form submitted by the user in `doctor.jsp`), make a call to a method in `Person.java` that you create to return the name of the doctor with the given patient, and send the response back to the `doctor.jsp` page where the name will be displayed. If you are really confused on how to do this, try to understand how the other servlet files operate.

3. Now we need to add the `getDoctorName` method in `Person.java` to retrieve the doctor name from the database. This will be the page's only interaction with the database.

4. The last steps we have to do is connect all of the files we just made and expose them on the website. We need to register our `doctor.jsp` file as a web page and our HttpServlet file from step 2 as a servlet. To do this, open the `web.xml` file. Here is a template for what you need to insert:

  ```xml
    <servlet>
      <servlet-name>INSERT NAME</servlet-name> --choose a name for your servlet
      <jsp-file>/doctor.jsp</jsp-file> --the jsp file we made
    </servlet>
    <servlet-mapping>
      <servlet-name>SAME NAME AS ABOVE</servlet-name>
      <url-pattern>/URL</url-pattern> --whatever you want the url to be to direct you to this page (for example, if it is /doctor, going to localhost:8080/doctor takes you to the page
    </servlet-mapping>


    <servlet>
      <servlet-name>INSERT NAME</servlet-name>
      <servlet-class>com.match.web.(NAME OF YOUR JAVA HTTPSERVLET FILE)</servlet-class>
    </servlet>
    <servlet-mapping>
      <servlet-name>SAME NAME AS ABOVE</servlet-name>
      <url-pattern>/(NAME OF THE ACTION IN YOUR FORM)</url-pattern>
    </servlet-mapping>
  ```

  The first servlet exposes the `doctor.jsp` file and creates a url to access the page.
  For the second servlet, make sure the url-pattern is the same as the action field in the form you created in `doctor.jsp`. This tells the `doctor.jsp` form to direct to the java file you made in step 2 which then adds the info to the database.

5. Last, we need to add our new files to the build and re-build the web application. In the `build.sh` file, add this line to build your Java HttpServlet file from step 2. Note that you need to insert the name of your java file.

  ```bash
    javac -classpath WEB-INF/lib/*:WEB-INF/classes -d WEB-INF/classes com/match/web/INSERT_SERVLET NAME.java
  ```
You also need to add a navbar for your doctor page. In the `header.tag` file, add the following line to create it:

  ```html
    <li><a href="doctor">Find Doctor</a></li>
  ```

As described earlier, you may encounter an issue with running `sudo ./build.sh` you are using Windows to edit `build.sh`. This might cause issues with carriage return characters and when you try to run it no command runs properly (the first line will be along the lines of "1: cd: can't cd to ./src"). If this happens, you can resolve this by doing the following:

- Download the program dos2unix on your vagrant machine with: `sudo apt-get install dos2unix`
- Run `dos2unix build.sh` in your vagrant command line

In addition to editing `./build.sh`, we want to add a link to the new page in the header bar of the site. In header.tag under WEB-INF/tags, add ```<li><a href="your url for the jsp page">Whatever you want the link to say</a></li> ``` so that you can navigate to the page from the header.

# Testing

**We do not provide you with a testing file like the first two projects, but if you follow the steps below, it should give you a good idea of whether or not your project is working correctly.**

1. To start, ensure that your database is properly created and set up by following the steps in the *Schema + User* section. You should also be running the server and have built the project. Steps for this can be found in the *Getting Started* section. In your vagrant command line, run `psql matchapp`. We will use the psql interface to verify that your queries are working correctly.
2. In a browser, go to `localhost:8080`. The OrganTrail home page should be visible. If not, try refreshing the page a couple times or rebuilding the project. Also make sure the server is running.
3. Click on the `register` tab. Enter any first name, last name, and birthdate (>18 years old). Then select AB+ for the blood type. Click submit. You should see the id and doctor id of your created person. If this is the first person you have registered, it should be id 101 and doctor 2.
4. Now create another person, but this time make the person younger than 18. You should be redirected to an invalid input page.
5. Navigate to the `People` tab. You should see a list of 10 people. Now, enter your registered person's first name into the search bar and press submit. You should see your created person come up. Do the same with last name, and blood type (AB+). For blood type, you may not see your person since there are more than 10 people with AB+. You can verify that all of the people returned have AB+ using the psql command line.
6. Go to the `Find Matches` page. Enter your person's id. It should display nothing (not 'No Matches').
7. Now go to the `Request Organ` tab. Enter your person's id, Liver, and some date that is a couple years into the future. Your doctor's id should be changed. Check that it was also changed in the database. You should also check that this doctor's specialty is liver. If this is the first person you created, you should get doctor 62.
8. Click on the `Find Matches` tab. Enter your person's id and click generate match. You should see at least 7 names, including Viv Bridgwood and Calypso Van Der Hoog. Verify in the database that everyone you see is present in the available table with liver being offered.
9. Now, go to the offer organ tab, and offer your person's heart. Your person's doctor should be changed again. Go back to the find matches tab, and enter id 6. You should see your person's name somewhere in the list.
10. Finally, we will check your view `doctor page`. Recall your most recent doctor's id number, and check his name in the database. Then enter your person's id on the view doctor page. The name should match what you found in the database.

**This testing is meant to give you a feel of how your project should work. It is not all-encompassing and we encourage you to more vigorously test your site.**



# **Submission**

To submit the project, zip the matchapp folder into a zip file named **matchapp.zip**. Please submit your zip file, `part1.txt` file and `ER diagram` as separate files on ELMS.


## **Part 5 (Optional): Deploying to AWS**

More likely than not, you will have to work with a database in the cloud at some point in the future. Here we give you the opportunity to deploy your MatchMaker application to the cloud, turn it into a publicly accessible Website, and get to work with cloud databases a little bit. Note that you can sign up for a free tier trial to use AWS with a new account; however Amazon may charge money to deploy this app. However, you can apply for free Amazon credit as a student (https://www.awseducate.com/Registration) that should cover the costs of the initial deployment. Please note that this application process may take several days for them to get back to you.

 Follow these steps to do this:

1. Open the [Elastic Beanstalk Management Console](https://console.aws.amazon.com/elasticbeanstalk/home)

2. Choose *Create New Application*

3. For *Application Name*, type tomcat-snakes. Choose *Next*.

4. Choose *Web Server Environment*

5. Set the platform to *Tomcat* and choose *Next*.

    * Use the tomcat8/java8 platform (which it should set to by default)

6. Choose *Upload your own* and *Choose File*.

7. Upload *ROOT.war* from your project directory and choose *Next*.

8. Type a unique *Environment URL* and choose *Next*.

9. Check *Create an RDS DB Instance with this environment* and choose *Next*.

10. Set *Instance type* to *t2.nano* and choose *Next*. Choose *Next* again to skip tag configuration.

11. Apply the following RDS settings and choose *Next* (leave the other settings default):

    * DB engine: *postgres*

    * Engine version: *9.6.2 (or whatever the most recent version is)*

    * Instance class: *db.t2.micro*

    * Master username: any username (make sure you know it)

    * Master password: any password (make sure you know it)

12. Choose Next to create and use the default role and instance profile.

13. Choose Launch.

This may take awhile (10 to 15 minutes). After it finishes, your application is in the cloud, but your database it created to go with it is actually empty :(. You need to create the person and match table in the database instance just like you did in your local postgres environment. You can do this by connecting to the database from your a postgresql client. Here are directions for using the psql linux client (which you already have on your virtual machine)

1. Navigate to the configuration tab on your Elastic Beanstalk management console in your environment that you deployed the match application

2. Scroll down to the Data Tier section and click on the link in the RDS card called "endpoint"

3. It should take you to the Amazon RDS portion of the console. From here click on the link for your database. If you have used AWS and have other instances already there you should click on the link for the instance you just made, if not you should only have one link to click on anyways

4. Scroll down to the Connect tab on the page

5. Here you should see information we’re going to need to connect to the database: Take note of the endpoint name and port number. Make sure under publicly accessible it says "yes" (AWS should do this for you when you deployed with Beanstalk)

6. We need to add a security rule to allow you to connect to your database from your own psql client. Go ahead and click on the link to the security group which is just below the endpoint information. This will take you to a new page in the console.

7. At the bottom of the page, click on the inbound tab and click the edit button

8. Click Add Rule and add a new rule with the following fields:

    1. Type: All Traffic

    2. Protocol: All

    3. Port Range: 0 - 65535

    4. Source: Custom

        1. In the box enter "0.0.0.0/0"

9. Leave the description blank and hit the save button

10.  Now that our rule is set, we should be able to use psql to connect to the database

11. From the command line on your machine type the following to connect:

Psql --host=yourendpointname --port=yourport(should be 5432) --username=username you set previously in deploying --password --dbname=ebdb

Notes:

Your endpoint name should look something like: randomcharacters.morerandomcharacters.us-east-2.rds.amazonaws.com

The dbname should be ebdb by default, if it is not, find the database name on the page for your db instance information

You should get the prompt from ebdb, once there, create your tables.

Don't forget to delete your account (or at least undeploy the Website) after you complete the exercise --- otherwise Amazon will continue to charge you after your free credits are used up. Alternateively, you can get a real domain name, get users to pay for the app (which means you will probably have to add more features), and cover your costs that way ;)
