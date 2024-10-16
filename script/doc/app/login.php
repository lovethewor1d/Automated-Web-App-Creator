<?php
	  session_start();
      require_once 'config.php';
	  
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
		
		$_SESSION["username"] = $username;
        echo("<script>window.location.href = 'home.php';</script>");
      }else{
        echo '<span style="color:white;text-align:center;">Invalid username and password</span>';
      }}
    ?>
       <!-- end -->
<!DOCTYPE HTML> 
<!-- Website template by freewebsitetemplates.com --> 
<html> 
    <head> 
        <meta charset="UTF-8"> 
        <title>Login - StoryBoard</title>         
        <link rel="stylesheet" href="css/style.css" type="text/css"> 
    </head>     
    <body> 
        <div id="header"> 
            <div> 
                <div class="logo"> <a href="home.php">StoryBoard</a> 
                </div>                 
                <script type='text/javascript' src='javascript/jquery-3.3.1.js' crossorigin="anonymous"></script>                       
        </div>         
    </div>     
    <div id="contents"> 
        <div id="about"> 
            <h3>Login</h3> 
            <form action="" method="GET"> 
                <label>UserName : </label>
                <input type="text" name="username" required class="box"/>
                <br/>
                <br/> 
                <label>Password : </label>
                <input type="password" name="password" class="box"/>
                <br/>
                <br/> 
                <input type="submit" value="Submit " name="id_submit" required/>
                <br/></br> <a href="signup.php">Create an account</a> 
            </form>             
        </div>         
    </div>     
    <div id="footer"> 
        <div class="clearfix"> 
            <div id="connect"> <a href="http://freewebsitetemplates.com/go/facebook/" target="_blank" class="facebook"></a>
                <a href="http://freewebsitetemplates.com/go/googleplus/" target="_blank" class="googleplus"></a>
                <a href="http://freewebsitetemplates.com/go/twitter/" target="_blank" class="twitter"></a>
                <a href="http://www.freewebsitetemplates.com/misc/contact/" target="_blank" class="tumbler"></a> 
            </div>             
            <p> 
				© 2023 Love.
 </p> 
            <p> Designed by freewebsitetemplates.com</p> 
        </div>         
    </div>     
</body> 
