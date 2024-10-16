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
						<div id="fh5co-logo"><a href="home.html">Storyboard<span>.</span></a></div>
					</div>
					<div class="col-xs-10 text-right menu-1">
						<ul>
							<li><a href="home.html">Home</a></li>
							<li><a href="upload.html">Verification</a></li>
							<li><a href="products.html">View Products</a></li>
							<li class="active"><a href="search.html">Search</a></li>
							<li><a href="include.php">V &mdash; Name Check</a></li>
							<li><a href="feedback.html">Feedback</a></li>
							<li class="btn-cta"><a href="index.php"><span>Logout?</span></a></li> <! -- logout? -->
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

<!-- Cookiestart -->
<?php
$cookie_name = "flag";
$x = random_int(100, 999);
$y = md5($x);
$cookie_value = $y;
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
?>
<!-- Cookieend -->
						</div>
					</div>
				</div>
			</div>
		</div>
	</header>
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