<!-- start -->
<?php
include "config.php";
if(isset($_POST['submit'])){
$username = $_POST['username']; 
$password = $_POST['password'];
$con = mysqli_connect("db", "php_docker", "password", "php_docker");
$query = "insert into users (username, password) values('$username', '$password')";
$result = mysqli_query($con, $query);
$con->close();
if($result == true){
echo "User Registration Successful <a href='login.php'>Login Now!</a>";
}else{
echo "User Registration Failed!";
}}
?>
<!-- end -->		
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

		</div>
	</div>
	<div id="contents">
		<div id="about">
	<h3>Signup</h3>
                            <form action="signup.php" method="post">
                            <label>username: </label><input type="text" name="username" value="" required class = "box"/></br>
							<br>
                            <label>password: </label><input type="password" name="password" value="" class = "box"/></br>
							<br>
                            <input type="submit" name="submit" value="submit" required /><br />
				            <a href="index.php">Already have an account? Login here.</a>
                            </form>
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
