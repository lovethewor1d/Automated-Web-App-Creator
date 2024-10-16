<!-- start -->
<?php
require_once "config.php";
require_once 'protect.php';
if(isset($_GET["id"]))
{    
    $id=$_GET['id'];
    $query=mysqli_query($db,"SELECT * FROM types WHERE id= $id");

if(mysqli_num_rows($query) > 0){
        while($row = mysqli_fetch_array($query)){
            printf ("%s %s\n",$row["name"],$row["description"]);
        }
        // Free result set
        mysqli_free_result($query);
    } else{
        echo "No records found.";
    }
}
?>
<!-- end -->
<html>
   <title>StoryBoard</title>
   <head>
      <title>Types Page</title>
	      <!-- CSSstart -->
	  	  <link rel="stylesheet" href="styles1.css">
		  <!-- CSSend -->   </head>
   <body>
   </body>
</html>