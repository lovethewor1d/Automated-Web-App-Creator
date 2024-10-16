


       <!-- start -->
       <?php
       include "config.php";
       $con = mysqli_connect("localhost", "root", "", "database");
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