import re
import os
import string
import secrets
import random
import shutil
import module.globals
import sys
app = module.globals.DirCheck() 

def replacing():
    def replace(filePath, subs, flags=0):
        with open(file_path, "r+") as file:
            x = file_contents = file.read()
            y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
            result = '\n'.join(y)
            text_pattern = re.compile(re.escape(result), flags)
            file_contents = text_pattern.sub(subs, file_contents)
            file.seek(0)
            file.truncate()
            file.write(file_contents)
            file.close()
            #shutil.copy(file_path, app) 
            #print("Code Replacement Process Successful \n")
            print("Please check the apps folder for your newly modified file")
    #file_path=input("Please enter the filepath: ")
    #print(file_path)
    os.chdir(app) ###################add this on other modules
    path = getattr(sys, '_MEIPASS', os.getcwd())
    full_path = path+r"\upload.php"
    print(full_path)
    file_path=os.path.basename(full_path) # filename with extension
    #print(file_path)
    #print(os.path.splitext(file_path)[0]) - filename without extension
    if file_path == 'upload.php':
       subs='''
       <!-- start -->
       <?php
       require_once "config.php";
       $file_get = $_FILES['files']['name'];
       $temp = $_FILES['files']['tmp_name'];
       $mimetype = mime_content_type($temp);
       if(in_array($mimetype, array('image/jpeg', 'image/jpg', 'image/gif', 'image/png'))) {
          $file_to_saved = "documents/".$file_get;
          move_uploaded_file($temp, $file_to_saved);
          $insert_img = mysqli_query($db,"INSERT INTO image values ('".$file_to_saved."')");
          echo 'OK';
       
       } else {
           echo 'Upload a real image!';
       }
       ?>
       <a class=".back_button" href="javascript:history.back(1)">go back</a>
       <!-- end -->'''
       
       replace(file_path, subs)