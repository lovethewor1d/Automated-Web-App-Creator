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
        <title>Home Page - StoryBoard</title>
        <link rel="stylesheet" href="css/style.css" type="text/css">
    </head>
    <body>
        <div id="header">
            <div><a href="home.php">StoryBoard</a>
            <script type='text/javascript' src='javascript/jquery-3.3.1.js' crossorigin="anonymous"></script>
                <script> 
					$(function(){
					  $("#header").load("headers.html"); 
					  //$("#footer").load("footer.html"); 
					});
					</script>                 
            </div>
        </div>
    </div>
    <div id="contents">
        <p>
				Welcome to the Storyboard, a gateway through which you can verify your identity, check your virtual name, view &amp; search products, leave your feedback </p>
        <div class="features">
</div>
    </div>
    <div id="footer">
        <div class="clearfix">
            <div id="connect"><a href="http://freewebsitetemplates.com/go/facebook/" target="_blank" class="facebook"></a>
                <a href="http://freewebsitetemplates.com/go/googleplus/" target="_blank" class="googleplus"></a>
                <a href="http://freewebsitetemplates.com/go/twitter/" target="_blank" class="twitter"></a>
                <a href="http://www.freewebsitetemplates.com/misc/contact/" target="_blank" class="tumbler"></a>
            </div>
            <p>
				© 2023 Love. </p>
            <p> Designed by freewebsitetemplates.com</p>
        </div>
    </div>
</body>
