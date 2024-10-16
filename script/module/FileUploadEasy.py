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
       if(!empty($_FILES['myFile']))
       {
         $path = "documents/";
         $path = $path . basename( $_FILES['myFile']['name']);
       
         if(move_uploaded_file($_FILES['myFile']['tmp_name'], $path)) {
           echo "The file ".  basename( $_FILES['myFile']['name']). 
           " has been uploaded";
         } else{
             echo "There was an error uploading the file, please try again!";
         }
       }
       ?>
       <a class=".back_button" href="javascript:history.back(1)">go back</a>
       <!-- end -->'''
       
       replace(file_path, subs)
       