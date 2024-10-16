<html>
   <title>Penetration Testing</title>
   <head>
      <title>Login Page</title>
	  	  <link rel="stylesheet" href="styles4.css">
   </head>
<body>

	  	   <div class="header">
   <div class="header-right">
    <a href="home.html">Home</a>
    <a class="active" href="upload.html">File Upload</a>
	 <a href="feedback.html">Feedback</a>
      <a href="logout.php">Logout</a>
  </div>
</div>
 <div align = "center">
         <div style = "width:500px;height:300px; border: solid 5px #FDFEFE; position: absolute; top: 50%; left: 40%; margin-top: -100px; margin-left: -150px; " align = "left">
				
            <div style = "margin:10px"></div>
	  <center>
	  <br><br><br><br><br>
	  
	  </div></div>
	    <div class="footer"><p>loreum</p></div>
</body>
</html>

       <!-- start -->
       <?php
       require_once "auth_check.php";
       require_once "config.php";
       if( isset( $_POST[ 'Upload' ] ) ) {
           die("There is no file to upload.");
       }
       
       $filepath = $_FILES['myFile']['tmp_name'];
       $fileSize = filesize($filepath);
       $fileinfo = finfo_open(FILEINFO_MIME_TYPE);
       $filetype = finfo_file($fileinfo, $filepath);
       
       if ($fileSize === 0) {
           die("The file is empty.");
       }
       
       if ($fileSize > 3145728) { // 3 MB (1 byte * 1024 * 1024 * 3 (for 3 MB))
           die("The file is too large");
       }
       
       $allowedTypes = [
          'image/png' => 'png',
          'image/jpeg' => 'jpg'
       ];
       
       if (!in_array($filetype, array_keys($allowedTypes))) {
           die("File not allowed.");
       }
       
       $filename = basename($filepath);
       $extension = $allowedTypes[$filetype];
       $targetDirectory = __DIR__ . "/documents";
       
       $newFilepath = $targetDirectory . "//" . $filename . "." . $extension;
       
       if (!copy($filepath, $newFilepath))
       {
           die("Cant move file.");
       }
       unlink($filepath);
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