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
    full_path = path+"\view.php"
    print(full_path)
    file_path=os.path.basename(full_path) # filename with extension
    #print(file_path)
    #print(os.path.splitext(file_path)[0]) - filename without extension
    if file_path == 'view.php':
       subs='''
       <!-- start -->
       <?php
       include "config.php";
       $con = mysqli_connect("db", "php_docker", "password", "php_docker");
       $sql = "SELECT * FROM commentsnew";
       $result = mysqli_query($con, $sql);
       while ($row = $result->fetch_assoc()) {
       	$row['name'] = htmlspecialchars($row['name'],ENT_QUOTES,'UTF-8');
       	$row['comment'] = htmlspecialchars($row['comment'],ENT_QUOTES,'UTF-8');
       	echo "name:"; echo $row['name']."<br>";
           echo "comment:"; echo $row['comment']."<br><br>";
       }
       ?>
       <!-- end -->'''
       
       replace(file_path, subs)