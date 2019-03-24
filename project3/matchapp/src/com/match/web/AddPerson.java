package com.match.web;
import com.match.model.Person;
import java.util.Date;
import java.text.DateFormat;
import java.text.SimpleDateFormat;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import javax.servlet.jsp.tagext.SimpleTagSupport;
import java.io.*;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class AddPerson extends HttpServlet {
  private static final Logger logger = LogManager.getLogger("match");
  public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException, NumberFormatException {

    //Gets the string data of all of the fields in the form
    String first = request.getParameter("first");
    String last = request.getParameter("last");
    String birthdate = request.getParameter("birthdate");
    String blood_type = request.getParameter("type");

    /*
    TODO: Call the addPerson and getDoctorFirst methods, given the parameters passed
    to the post request. Only call getDoctorFirst if the first function is successful.
    Redirect to the invalid input page if any constraint defined in
    the Schema + User section of the readme is violated:

    You must check that first name is less or equal to 12 chars, last name less
    than or equal to 18 chars, and that their age is greater than or equal to 18.
    You should calculate age with the birthdate parameter - feel free to use the java
    standard library to help you with this.

    Then, send the person and doctor_id's in the url parameters.
    */

    // Replace 'true' below and check for input constraints
    if (true) {
        response.sendRedirect("invalidinput");
    } else {

        //Here we make the call to the addPerson method in Person.java that connects to the database and inserts the person with the given values
        // If that's successful, update their doctor with getDoctorFirst, which is also in person.java.
        // id should be the id returned from addPerson, and doc should be the doctor's id returned from getDoctorFirst.

        int id = -1;
        int doc = -1;
        //Sends the response to the add page so that another person can be added. ID is passed as a parameter to display the id
        //for the new user to refer to get and view matches
        response.sendRedirect("add?id=" + id + "&doc=" + doc);
    }


  }
}
