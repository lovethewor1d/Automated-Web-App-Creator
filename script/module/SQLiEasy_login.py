import re
import os
import string
import secrets
import random
import shutil
import module.globals
import sys

app = module.globals.DirCheck() 
#
def replacing():
    def replace(filePath, subs, flags=0):
        with open(file_path, "r+") as file:
            x = file_contents = file.read()
            y = re.findall("[^\n].*<!-- end -->[^\n]*", x, re.DOTALL)
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
    full_path = path+"\login.php"
    print(full_path)
    file_path=os.path.basename(full_path) # filename with extension
    #print(file_path)
    #print(os.path.splitext(file_path)[0]) - filename without extension
    if file_path == 'login.php':
       subs='''
       <?php
              require_once "config.php";
       if(isset($_GET["id_submit"]))
       {    
           $username=$_GET['username'];  
           $password=$_GET['password'];  
           $query=mysqli_query($db,"SELECT * FROM users WHERE username='$username' AND password='$password'");
           if(mysqli_num_rows($query) > 0){
               while($data = mysqli_fetch_assoc($query)){
                   header("Location: home.php");}  
           }else{
                echo '<span style="color:white;text-align:center;">Invalid username and password</span>';
           } 	
       }	
       ?>
       <!-- end -->'''
       
       replace(file_path, subs)  
    #print(file_path)      