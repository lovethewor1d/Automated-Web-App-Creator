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
	<title>Feedback - StoryBoard</title>
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
		<div class="section">
<!-- start -->
<?php
       //include "config.php";
       $con = mysqli_connect("db", "php_docker", "password", "php_docker");
       $sql = "SELECT * FROM commentsnew";
       $result = mysqli_query($con, $sql);
       while ($row = $result->fetch_assoc()) {
       	$row['name'] = htmlspecialchars($row['name'],ENT_QUOTES,'UTF-8');
       	$row['comment'] = htmlspecialchars($row['comment'],ENT_QUOTES,'UTF-8');
       	echo "name:"; echo $row['name']."<br>";
           echo "comment:"; echo $row['comment']."<br><br>";
       }
       ?>
       <!-- end -->
	   <a class=".back_button" href="javascript:history.back(1)">go back</a>
		</div>
		<div class="section contact">
			<p>
				Don't forget to steal your cookies <span>&#127850;</span>
			</p>
		</div>
	</div>
	<div id="footer">
		<div class="clearfix">
			<div id="connect">
				<a href="http://freewebsitetemplates.com/go/facebook/" target="_blank" class="facebook"></a><a href="http://freewebsitetemplates.com/go/googleplus/" target="_blank" class="googleplus"></a><a href="http://freewebsitetemplates.com/go/twitter/" target="_blank" class="twitter"></a><a href="http://www.freewebsitetemplates.com/misc/contact/" target="_blank" class="tumbler"></a>
			</div>
			<p>
				© 2023 Zerotype. All Rights Reserved.
			</p>
		</div>
	</div>
</body>
</html>