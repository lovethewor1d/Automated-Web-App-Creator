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
    full_path = path+"\include.php"
    print(full_path)
    file_path=os.path.basename(full_path) # filename with extension
    #print(file_path)
    #print(os.path.splitext(file_path)[0]) - filename without extension
    if file_path == 'include.php':
       subs='''
       <!-- start -->
       <?php
       require_once "config.php";
       header("X-XSS-Protection: 0");
       //$id = $_GET['id'];
       //include($id);
       //$blacklist = array(" ","&","&&","|","||","@","%",",","/","~","^");
       //$input = str_replace($blacklist,"", $id);
       //$blacklist = array("ls","dir","cat","type","whoami","pwd","echo","ipconfig","ifconfig","nc","netcat");
       //$input = str_replace($blacklist,"", $id);
       //$input = htmlspecialchars($input);
       //echo "<font color='black'>".$id."</font>";
       //$output = shell_exec("nslookup " . $input);
       //echo "<b>".htmlspecialchars($output,ENT_QUOTES,'UTF-8');
       
       //code for Local File Inclusion
       $id = $_GET[ 'id' ].".php";
       include($id);
       if( $id != "include.php" && $id != "file1.php" && $id != "file2.php" && $id != "file3.php" ) {
           // This isn't the page we want!
           echo "ERROR: File not found!";
           exit;
       } 
       ?>
       <!-- end -->'''
       
       replace(file_path, subs)