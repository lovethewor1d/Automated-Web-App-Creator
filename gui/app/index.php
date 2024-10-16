<!-- start -->
<?php
        //require_once "protect.php";
    require_once "config.php";
  if(isset($_GET["id_submit"]))
  {
   $con = mysqli_connect("db", "php_docker", "password", "php_docker");
     $username = $_GET['username'];
     $password = $_GET['password'];
     $stmt = $con->prepare("SELECT * FROM users WHERE username = ? && password = ?");
  $stmt->bind_param("ss", $username, $password);
     if($stmt->execute()){
       $result = $stmt->get_result();
       $num_rows = $result->num_rows;
     }
     if($num_rows > 0){
      session_start();
      $_session["name"] = $customer["name"];
      $_session["id"] = $customer["id"];
      $_session["logged_in"] = true;
        echo("<script>location.href = 'home.html';</script>");
          }else{
            echo '<span style="color:white;text-align:center;">Invalid username and password</span>';
          }}
?>
<!-- end -->
<html>
   <title>StoryBoard</title>
   <head>
      <title>Login Page</title>
	  	 	      <!-- CSSstart -->
	  	  <link rel="stylesheet" href="styles1.css">
		  <!-- CSSend -->
   </head>
   <body>
   <div class="header">
  <div class="logo"></div>
   <div class="header-right">
</div></div>
   </div>
         <div align = "center">
	           <div style = "width:500px;height:200px; border: solid 5px #FDFEFE; position: absolute; top: 50%; left: 40%; margin-top: -100px; margin-left: -150px; " align = "left">
            <div style = "background-color:#FDFEFE; color:#120f0f; padding:3px;font-family:Arial; font-size:15"><b>Welcome to StoryBoard</b></div>
            <div style = "margin:20px">
               <form action="" method = "GET">
				  <label>UserName: </label><input type = "text" name = "username" required class = "box"/><br /><br />
                  <label>Password: </label><input type = "password" name = "password" class = "box" /><br/><br />
                  <input type = "submit" value = "Submit " name="id_submit" required /><br /></br/>
				  <a href="signup.php">Create an account</a>
               </form>	
            </div>
         </div>
      </div>
	  <div class="footer"><p>Lorem Ipsum</p></div>
   </body>
</html>