<html>
   <title>search</title>
   <head>
      <title>Search Page</title>
	  	 	      <!-- CSSstart -->
	  	  <link rel="stylesheet" href="styles1.css">
		  <!-- CSSend -->
   </head>
<body>
	  	   <div class="header">
  <div class="logo"></div>
  <!--- for logo:  <div class="logo"><img src="logo.jpg" width="130" height="40"></div> -->
   <div class="header-right">
    <a href="home.html">Home</a>
  
    <a href="upload.html">File Upload</a>
	 <a class="active" href="search.html">Search</a>
	 <a href="feedback.html">Feedback</a>
      <a href="logout.php">Logout</a>
</div></div>
	  
	  <div class="footer"><p>Lorem Ipsum</p></div
</body>
</html>




       <!-- start -->
       <?php
       require_once "auth_check.php";
       require_once "config.php";
       header("X-XSS-Protection: 0");
       /*
       $id = $_GET['id'];
       include($id);
       $blacklist = array(" ","&","&&","|","||","@","%",",","/","~","^");
       $input = str_replace($blacklist,"", $id);
       $blacklist = array("ls","dir","cat","type","whoami","pwd","echo","ipconfig","ifconfig","nc","netcat");
       $input = str_replace($blacklist,"", $id);
       $input = htmlspecialchars($input);
       echo "<font color='black'>".$id."</font>";
       $output = shell_exec("nslookup " . $input);
       echo "<b>".htmlspecialchars($output,ENT_QUOTES,'UTF-8');
       */
       //code for Local File Inclusion ----- this can be used to read flag: php://filter/convert.base64-encode/resource=flag      [flag/flag.php will have the flag]
       require_once "auth_check.php";
       require_once "config.php";
       $id = $_GET[ 'id' ].".php";
       include($id);
       if( $id != "include.php" && $id != "file1.php" && $id != "file2.php" && $id != "file3.php" ) {
           // This isn't the page we want!
           echo "ERROR: File not found!";
           exit;
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