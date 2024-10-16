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
echo "User Registration Successful <a href='index.php'>Login Now!</a>";
}else{
echo "User Registration Failed!";
}}
?>
<!-- end -->
<!DOCTYPE HTML>
<html>
	<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>Storyboard</title>
	<!-- <link href="https://fonts.googleapis.com/css?family=Work+Sans:300,400,500,700,800" rel="stylesheet">	 -->
	<link href="https://fonts.googleapis.com/css?family=Inconsolata:400,700" rel="stylesheet">
	
	<!-- Animate.css -->
	<link rel="stylesheet" href="css/animate.css">
	<!-- Icomoon Icon Fonts-->
	<link rel="stylesheet" href="css/icomoon.css">
	<!-- Bootstrap  -->
	<link rel="stylesheet" href="css/bootstrap.css">
	<!-- Flexslider  -->
	<link rel="stylesheet" href="css/flexslider.css">

	<!-- Theme style  -->
	<link rel="stylesheet" href="css/style.css">

	<!-- Modernizr JS -->
	<script src="js/modernizr-2.6.2.min.js"></script>

	</head>
	<body>
		
	<div class="fh5co-loader"></div>
	
	<div id="page">
	<nav class="fh5co-nav" role="navigation">
		<div class="top-menu">
			<div class="container">
				<div class="row">
					<div class="col-xs-2">
						<div id="fh5co-logo"><a href="index.html">Storyboard<span>.</span></a></div>
					</div>
					<div class="col-xs-10 text-right menu-1">
						<ul>
							<li><a href="index.php">Login</a></li>
							<li class="active">><a href="signup.php">Signup</a></li>
						</ul>
					</div>
				</div>
				
			</div>
		</div>
	</nav>

	<header id="fh5co-header" class="fh5co-cover js-fullheight" role="banner">
		<div class="overlay"></div>
		<div class="container">
			<div class="row">
				<div class="col-md-8 col-md-offset-2 text-center">
					<div class="display-t js-fullheight">
						<div class="display-tc js-fullheight animate-box" data-animate-effect="fadeIn">
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
			</div>
		</div>
	</header>
			<div class="row copyright">
				<div class="col-md-12 text-center">
					<p>
						<small class="block">&copy; 2023 Love. All Rights Reserved.</small> 
						<small class="block">Designed by <a href="http://freehtml5.co/" target="_blank">FreeHTML5.co</a> Demo Images: <a href="http://unsplash.co/" target="_blank">Unsplash</a></small>
					</p>
				</div>
			</div>

		</div>
	</footer>
	</div>

	<div class="gototop js-top">
		<a href="#" class="js-gotop"><i class="icon-arrow-up22"></i></a>
	</div>
	
	<!-- jQuery -->
	<script src="js/jquery.min.js"></script>
	<!-- jQuery Easing -->
	<script src="js/jquery.easing.1.3.js"></script>
	<!-- Bootstrap -->
	<script src="js/bootstrap.min.js"></script>
	<!-- Waypoints -->
	<script src="js/jquery.waypoints.min.js"></script>
	<!-- Flexslider -->
	<script src="js/jquery.flexslider-min.js"></script>
	<!-- Main -->
	<script src="js/main.js"></script>

	</body>
</html>

