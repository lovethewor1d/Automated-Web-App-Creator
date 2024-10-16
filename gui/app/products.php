
             <?php
             $cookie_name = "{flagz}";
             $x = random_int(100, 999);
             $y = md5($x);
             $cookie_value = $y;
             setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
             ?>
             <!-- Cookieend -->
            
       <!-- start -->
       <?php
       require_once "auth_check.php";
       require_once "config.php";
       //require_once "protect.php";
		if(isset($_GET["id"]))
		    {
       $id=$_GET['id'];
       $pass = addslashes($_GET['id']);
       $con = mysqli_connect("db", "php_docker", "password", "php_docker");
       $stmt = $con->prepare("SELECT * FROM products WHERE id=? LIMIT 1");
       $stmt->bind_param("s", $pass);
       $stmt->execute();
       $result = $stmt->get_result();
       $stmt->close();
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
       <!-- end -->
 <html>
   <title>StoryBoard</title>
   <head>
      <title>Products</title>
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
	  <a href="feedback.html">Feedback</a>
	 <a class="active" href="products.html">products</a>
	 <a href="logout.php">Logout</a>
</div></div>