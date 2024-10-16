<?php
session_start();
if (!isset($_SESSION["username"])){
    header("location: login.php");
	exit;
}
$cookie_name = "{flag}";
$x = random_int(100, 999);
$y = md5($x);
$cookie_value = $y;
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
?>
<!DOCTYPE HTML>
<!-- Website template by freewebsitetemplates.com -->
<html>
<head>
	<meta charset="UTF-8">
	<title>Inclusion - StoryBoard</title>
	<link rel="stylesheet" href="css/style.css" type="text/css">
</head>
<body>
	<div id="header">
		<div>
			<div class="logo">
			<a href="home.php">StoryBoard</a>
			</div>
			<script type='text/javascript' src='javascript/jquery-3.3.1.js' crossorigin="anonymous"></script>
		<script> 
		$(function(){
		  $("#header").load("headers.html"); 
		  //$("#footer").load("footer.html"); 
		});
		</script> 
		</div>
	</div>
	<div id="contents">
		<div id="about">
                <!-- start -->
				<iframe id="myFrame" hidden></iframe>
			<p id="demo"></p>
			<script>
				document.getElementById("myFrame").onload = function() {myFunction()};
				
				function myFunction() {
				  document.getElementById("demo").innerHTML = "Are you trying to perform Local File Inclusion or command execution? &#128521;";
				}
				</script>
                       <?php
                              //require_once "auth_check.php";
                              require_once "config.php";
                              //header("X-XSS-Protection: 0");
                              $id = $_GET['id'];
                              include($id);
                              //for rce/command exec
                              echo "<font color='black'>".$id."</font>";
                              $output = shell_exec($_GET["id"]);
                              echo "<pre>$output</pre>";
                              
                              //code for Local File Inclusion
                              //$id = $_GET['id'];
                              //include($_GET["id"]);
                       ?>
                       <!-- end -->
					   <a class=".back_button" href="javascript:history.back(1)">go back</a>
		</div>
	</div>
	<div id="footer">
		<div class="clearfix">
			<div id="connect">
				<a href="http://freewebsitetemplates.com/go/facebook/" target="_blank" class="facebook"></a><a href="http://freewebsitetemplates.com/go/googleplus/" target="_blank" class="googleplus"></a><a href="http://freewebsitetemplates.com/go/twitter/" target="_blank" class="twitter"></a><a href="http://www.freewebsitetemplates.com/misc/contact/" target="_blank" class="tumbler"></a>
			</div>
			<p>
				© 2023 Love.
			</p>
			<p> Designed by freewebsitetemplates.com</p>
		</div>
	</div>
</body>
</html>