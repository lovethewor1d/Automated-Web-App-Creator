<?php 
include"config.php";

$file_get = $_FILES['files']['name'];
$temp = $_FILES['files']['tmp_name'];

$file_to_saved = "documents/".$file_get; //Documents folder, should exist in your host in there you're going to save the file just uploaded
move_uploaded_file($temp, $file_to_saved);

/*echo $file_to_saved;*/

$insert_img = mysqli_query($db,"INSERT INTO image values ('".$file_to_saved."')");
if ($insert_img) {
# code...
echo "file uploaded successfully";
}
else{
 echo "There is something wrong.";
}
?>
