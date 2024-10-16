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
	<title>Products - StoryBoard</title>
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
			<h1>Products</h1>
       <!-- start -->
       <?php
	  session_start();
      require_once 'config.php';
		if(isset($_GET["id"]))
		    {
       $id=$_GET['id'];
       $con = mysqli_connect("db", "php_docker", "password", "php_docker");
       $query="SELECT * FROM products WHERE id= $id LIMIT 1";
       $result = mysqli_query($con, $query);
	   echo "<table border='1' align='center'>
       <H2 align='center'> Products Table </h2>
       <tr>
       <th>Product Type</th>
       <th>Product Name</th>
       <th>Product Price</th>
       </tr>";
       while ($fetch = mysqli_fetch_array($result))
       {
           echo "<tr>";
           echo "<td>" . $fetch['type'] . "</td>";
           echo "<td>" . $fetch['name'] . "</td>";
           echo "<td>" . $fetch['price'] . "</td>";
           echo "</tr>";
       }
       echo "</table>";
       }
       ?>
       <!-- end -->		</div>
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