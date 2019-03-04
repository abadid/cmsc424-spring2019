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
      <h2>Enter Your Information</h2>
      <form action="add.do" method="post">
        <div class = "row">
            <h3>Personal Information</h3>
            First Name: <br />
            <input type="text" size="18" name="first" required  />
            <br />
            Last Name: <br />
            <input type="text" size="18" name="last" required/>
            <br />
            Birthdate: <br />
            <input type="date" size="18" name="birthdate" />
            <br/>

            Blood type: <br />
            <select name="type">
              <option value="O+">O+</option>
              <option value="O-">O-</option>
              <option value="A+">A+</option>
              <option value="A-">A-</option>
              <option value="B+">B+</option>
              <option value="B-">B-</option>
              <option value="AB+">AB+</option>
              <option value="AB-">AB-</option>
            </select>
            <br/>

        </div>

        <div>
          <input type="submit" value="Submit" />
        </div>

      </form>
    </div>
    <div>
      <%
        String id =  request.getParameter("id");
        String doc = request.getParameter("doc");
        if(id == null) {
          id = "";
        }
        else {
          id = "Your ID is " + id + " - Remember it!";
        }
        if(doc == null){
            doc = "";
        }
        else{
            doc = "Your doctor's id is " + doc;
        }
      %>
      <p><%= id %> <br> <%= doc %></p>


    </div>

    <div class="sample">
      <p>You will be assigned a certified Organ Trail doctor following your organ request/offer. </p>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
