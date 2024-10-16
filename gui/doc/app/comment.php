<!-- start -->
<?php
require_once "config.php";
//require_once 'protect.php';
$name = $_POST['name'];
$comment = $_POST['comment'];
$strname = str_ireplace( 'alert', '', $_POST['name'] ); 
$strcomment = str_ireplace( 'alert', '', $_POST['comment'] );
$con = mysqli_connect("db", "php_docker", "password", "php_docker");
$query = "INSERT INTO commentsNew (name, comment) VALUES ('$strname', '$strcomment')";
$result = mysqli_query($con, $query);
echo("<script>window.location.href = 'feedback.html';</script>");
?>
<!-- end -->