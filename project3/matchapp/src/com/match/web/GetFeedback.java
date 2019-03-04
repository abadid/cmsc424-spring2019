package com.match.web;
import com.match.model.Person;
import com.match.model.Match;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import javax.servlet.jsp.tagext.SimpleTagSupport;
import java.io.*;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class GetFeedback extends HttpServlet {
  private static final Logger logger = LogManager.getLogger("match");
  public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException, NumberFormatException {
    
    String id1 = request.getParameter("id1");
    String id2 = request.getParameter("id2");
    String feedback = request.getParameter("fback");

    int feed_int = Integer.parseInt(feedback);

    boolean res = Match.insertFeedback(id1,id2,feed_int);

    response.sendRedirect("feedback");
  }
}
