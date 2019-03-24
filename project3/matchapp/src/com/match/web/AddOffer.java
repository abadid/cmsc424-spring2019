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
public class AddOffer extends HttpServlet {
  private static final Logger logger = LogManager.getLogger("match");
  public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException, NumberFormatException {

    //Gets the string data of all of the fields in the form
    String id = request.getParameter("id");
    String organ = request.getParameter("organ");

    /*
    TODO: Call the addAvailableOrgan and getDoctorUpdate methods given the parameters passed
    to the post request. Only call getDoctorUpdate if the first function is successful.
    Then, send the status and new doctor as URL parameters in the redirect
    */

    // status should be the code returned from addAvailableOrgan and doc should be the doctor's id returned from getDoctorUpate.\
    // There is no need to update doc if addAvailableOrgan fails.

    int status = -1;
    int doc = -1;

    response.sendRedirect("offer?status=" + status + "&doc=" + doc);
  }
}
