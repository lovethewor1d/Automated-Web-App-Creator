
       <!-- start -->
       <?php
       require_once "auth_check.php";
       require_once "config.php";
       $name = $_POST['name'];
       $comment = $_POST['comment'];
       $strname = str_ireplace( 'alert', '', $_POST['name'] ); 
       $strcomment = str_ireplace( 'alert', '', $_POST['comment'] );
       $con = mysqli_connect("db", "php_docker", "password", "php_docker");
       $stmt = $con->prepare("INSERT INTO commentsnew (name, comment) VALUES (?, ?)");
       $stmt->bind_param("ss", $strname, $strcomment);
       $stmt->execute();
       $result = $stmt->get_result();
       $stmt->close;
       echo("<script>location.href = 'feedback.html';</script>");
       ?>
       <!-- end -->

             <!-- Cookiestart -->
             <?php
             include"config.php";
             $cookie_name = "{flag}";
             $x = random_int(100, 999);
             $y = md5($x);
             $cookie_value = $y;
             setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
             ?>
             <!-- Cookieend -->
            
<html>
   <title>StoryBoard</title>
   <head>
      <title>Comments Page</title>
	      <!-- CSSstart -->
	  	  <link rel="stylesheet" href="styles1.css">
		  <!-- CSSend -->   
        </head>
<body>

	  	   <div class="header">
  <div class="logo"></div>
   <div class="header-right">
    <a href="home.html">Home</a>
  
    <a href="upload.html">File Upload</a>
	 <a href="search.html">Search</a>
	  <a class="active" href="feedback.html">Feedback</a>
	 <a href="products.html">products</a>
	 <a href="logout.php">Logout</a>
</div></div>
   </body>
</html>