<?php
   define('DB_SERVER', 'db');
   define('DB_USERNAME', 'php_docker');
   define('DB_PASSWORD', 'password');
   define('DB_DATABASE', 'php_docker');
   $db = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);
?>