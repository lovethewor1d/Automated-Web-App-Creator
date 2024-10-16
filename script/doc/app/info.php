<?php
session_start();
if (!isset($_SESSION["username"])){
    header("location: index.php");
	exit;
}
?>
<!-- start -->

<!-- end -->
<a class=".back_button" href="javascript:history.back(1)">go back</a>
