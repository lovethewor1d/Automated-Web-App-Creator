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
	<title>Verification - StoryBoard</title>
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
		<div class="features">
			<h1>Verification Page</h1>
			<p>
				Upload a valid file to verify that you are <b><i>not a robot</i></b>&#128521</p>
				<p>
					Can you leverage file upload feature to read a file <b>(flag.txt)</b>?
				</p>
			<div>
			</div>
			<div>
       <!-- start -->
	   <iframe id="myFrame" hidden></iframe>
			<p id="demo"></p>
			<script>
				document.getElementById("myFrame").onload = function() {myFunction()};
				
				function myFunction() {
				  document.getElementById("demo").innerHTML = "Try to understand why your file is getting blocked? &#128521;";
				}
				</script>
       <?php
       if(!empty($_FILES['myFile']))
       {
         $path = "documents/";
         $path = $path . basename( $_FILES['myFile']['name']);
       
         if(move_uploaded_file($_FILES['myFile']['tmp_name'], $path)) {
           echo "The file ".  basename( $_FILES['myFile']['name']). 
           " has been uploaded";
         } else{
             echo "There was an error uploading the file, please try again! Trying to upload a restricted file? Try playing with fil extensions, content-types, etc.";
         }
       }
       ?> <br><br>
       <!-- end -->
       <a class=".back_button" href="javascript:history.back(1)">go back</a>
			</div>
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