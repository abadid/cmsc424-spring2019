package com.match.web;
import com.match.model.Person;
import com.match.model.Organ;
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

public class AddRequest extends HttpServlet {
  private static final Logger logger = LogManager.getLogger("match");
  public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException, NumberFormatException {

    //Gets the string data of all of the fields in the form to register
    String id = request.getParameter("id");
    String organ = request.getParameter("organ");
    String by = request.getParameter("by");

    /*
    TODO: Call the addNeededOrgan and getDoctorUpdate methods given the parameters passed
    to the post request. Only call getDoctorUpdate if the first function is successful.
    Then, send the status and new doctor as URL parameters in the redirect.
    Ensure that the 'by' parameter (short for 'needs by') is a day greater than the current day.
    */

    // Replace 'true' below and check for input constraints
    if (true) {
      response.sendRedirect("invalidinput");
    }
    else {
        //Here we make the call to the method in Person that connects to the database and inserts the person with the given values

        // status should be the code returned from addNeededOrgan and doc should be the doctor's id returned from getDoctorUpate.
        // There is no need to update doc if addNeededOrgan fails.

        int status = -1;
        int doc = -1;
        //Sends the response to the add page so that another person can be added. ID is passed as a parameter to display the id
        //for the new user to refer to get and view matches
        response.sendRedirect("request?status=" + status + "&doc=" + doc);
    }


  }
}
