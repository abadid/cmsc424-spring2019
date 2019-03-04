<%@ taglib prefix="tagfiles" tagdir="/WEB-INF/tags" %>

<html>

  <head>
    <meta charset="utf-8"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <link href="css/bootstrap.css" rel="stylesheet" />
    <link href="css/match.css" rel="stylesheet" />

    <title>Register to find your match!</title>
  </head>

  <body>
    <tagfiles:header />

    <div class="container heading">
      <h2>Offer an Organ!</h2>
      <form action="offer.do" method="post">
        <div class = "row">
            User ID: <br />
            <input type="number" size="18" name="id" required  />
            <br />
            Organ: <br />
            <select name="organ">
              <option value="Heart">Heart</option>
              <option value="Liver">Liver</option>
              <option value="Kidney">Kidney</option>
              <option value="Lung">Lung</option>
              <option value="Pancreas">Pancreas</option>
            </select>
            <br />
            <!-- ADD YOUR INPUT FIELD FOR THE FIELD YOU ADDED TO THE PERSON DATABASE RIGHT HERE-->

        </div>

        <div>
          <input type="submit" value="Submit" />
        </div>

      </form>
    </div>

    <div>
      <%
        String status =  request.getParameter("status");
        String doc = request.getParameter("doc");
        String message = null;
        if(status == null) {
          message = "";
        }
        else if(status.compareTo("-1") == 0){
          message = "Request failed";
        }
        else if(status.compareTo("1") == 0){
            message = "Request Successful";
        }
        else{
            message = "Request status unknown";
        }

        if(doc == null || doc.compareTo("-1") == 0){
            doc = "";
        }
        else{
            doc = "Your new doctor's id is " + doc;
        }
      %>
      <p><%= message %> <br> <%= doc %></p>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
