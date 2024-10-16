<?php
require_once "config.php";
if(isset($_POST['submit'])){
$username = $_POST['username']; 
$password = $_POST['password'];
$con = mysqli_connect("db", "php_docker", "password", "php_docker");
$query = "insert into users (username, password) values('$username', '$password')";
$result = mysqli_query($con, $query);
$con->close();
if($result == true){
echo "User Registration Successful <a href='index.php'>Login Now!</a>";
}else{
echo "User Registration Failed!";
}}
?>
<html>
   <title>Penetration Testing</title>
   <head>
      <title>Signup Page</title>
	  		      <!-- CSSstart -->
	  	  <link rel="stylesheet" href="styles1.css">
		  <!-- CSSend -->
   </head>
   <body>
   <div class="header">
  <div class="logo"></div>
   <div class="header-right">
   
</div></div>
  <div class="logo"></div>
   </div>

         <div align = "center">
	           <div style = "width:500px;height:200px; border: solid 5px #FDFEFE; position: absolute; top: 50%; left: 40%; margin-top: -100px; margin-left: -150px; " align = "left">
            <div style = "background-color:#FDFEFE; color:#120f0f; padding:3px;font-family:Arial; font-size:15"><b>Welcome to Penetration Testing</b></div>

            <div style = "margin:20px">
                <form action="signup.php" method="post">
                <label>username: </label><input type="text" name="username" value="" required class = "box"/></br>
                <label>password: </label><input type="password" name="password" value="" class = "box"/></br>
                <input type="submit" name="submit" value="submit" required /><br />
				<a href="index.php">Already have an account? Login here.</a>
               </form>	
            </div>
         </div>
      </div>
	  <div class="footer"><p>Lorem Ipsum</p></div>
   </body>
</html>