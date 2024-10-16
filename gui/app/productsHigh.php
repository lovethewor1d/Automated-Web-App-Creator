<?php
        include "config.php";
		if(isset($_GET["id"]))
		{    
        $id=$_GET['id'];
        $con = mysqli_connect("db", "php_docker", "password", "php_docker");
        $query="SELECT * FROM products WHERE id=$id LIMIT 1";
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
<html>
   <title>Penetration Testing</title>
   <head>
      <title>Login Page</title>
	  	  <link rel="stylesheet" href="styles6.css">
   </head>
<body>

	  	   <div class="header">
  <div class="logo"></div>
   <div class="header-right">
    <a href="home.html">Home</a>
    <a href="about.html">About</a>
    <a href="upload.html">File Upload</a>
	 <a href="search.html">Search</a>
	  <a href="feedback.html">Feedback</a>
	 <a href="types.html">Types</a>
	 <a class="active" href="products.html">products</a>
	 <a href="index.php">Logout</a>
</div></div>
 <div align = "center">

         <div style = "width:500px;height:300px; border: solid 5px #006625; position: absolute; top: 50%; left: 40%; margin-top: -150px; margin-left: -150px;">
            <div style = "background-color:#006625; color:white; padding:3px;"><b>Types of Products</b></div>
				
            <div style = "margin:10px"></div>
	  <center>
	  <br><br><br><br><br>
	  <!---start1-->
	  <h3><a href="productsHigh.php?id=1" name="id" value="cars">Cars</a></h3>
	  <!---end1-->
	  
	  <!---start2-->
	  <h3><a href="productsHigh.php?id=2" name="id" value="bikes">Bikes</a></h3>
	  <!---end2-->
	  
	  <!---start3-->
	  <h3><a href="productsHigh.php?id=3" name="id" value="planes">Planes</a></h3></h3>
	  <!---end3-->
	  
	  <!---start4-->
	  <h3><a href="productsHigh.php?id=4" name="id" value="laptops">Laptops</a></h3></h3>
	  <!---end4-->
	  
	  <!---start5-->
	  <h3><a href="productsHigh.php?id=5" name="id" value="headphones">Headphones</a></h3></h3>
	  <!---end5-->
	  
	  </div></div>
	  
	  <div class="footer"><p>Lorem Ipsum</p></div>
	  
</body>
</html>
