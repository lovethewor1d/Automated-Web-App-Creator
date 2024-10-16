<?php
session_start();
if (!isset($_session['logged_in'])) {
    header("Location: index.php");
}
?>