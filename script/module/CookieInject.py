import re
import os
import string
import secrets
import random
import shutil
import module.globals

app = module.globals.DirCheck() 

def replacing():
    def replace(filePath, subs, flags=0):
        with open(file_path, "r+") as file:
            x = file_contents = file.read()
            y = re.findall("[^\n].*<!-- Cookieend -->[^\n]*", x, re.DOTALL)
            result = '\n'.join(y)
            text_pattern = re.compile(re.escape(result), flags)
            file_contents = text_pattern.sub(subs, file_contents)
            file.seek(0)
            file.truncate()
            file.write(file_contents)
            file.close()
            #shutil.copy(file_path, app) 
            #print("Code Replacement Process Successful \n")
            print("Please check the apps folder for your newly generated file")
    file_path=input("Please enter the filepath: ")
    #print(file_path)
    os.chdir(app)
    file_path=os.path.basename(file_path)
    #print(file_path)
    #print(os.path.splitext(file_path)[0])
    if file_path == 'index.php':
       subs='''
             <?php
             $cookie_name = "{flag}";
             $x = random_int(100, 999);
             $y = md5($x);
             $cookie_value = $y;
             setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
             ?>
             <!-- Cookieend -->
            '''  
       replace(file_path, subs)  
    elif file_path == 'products.php':
       subs='''
             <?php
             $cookie_name = "{flag}";
             $x = random_int(100, 999);
             $y = md5($x);
             $cookie_value = $y;
             setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
             ?>
             <!-- Cookieend -->
            '''  
       replace(file_path, subs) 
    elif file_path == 'comment.php':
       subs='''
             <?php
             $cookie_name = "{flag}";
             $x = random_int(100, 999);
             $y = md5($x);
             $cookie_value = $y;
             setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
             ?>
             <!-- Cookieend -->
            '''  
       replace(file_path, subs)  
    elif file_path == 'view.php':
       subs='''
             <?php
             $cookie_name = "{flag}";
             $x = random_int(100, 999);
             $y = md5($x);
             $cookie_value = $y;
             setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
             ?>
             <!-- Cookieend -->
            '''  
       replace(file_path, subs)  
    elif file_path == 'page2.php':
       subs='''
             <?php
             $cookie_name = "{flag}";
             $x = random_int(100, 999);
             $y = md5($x);
             $cookie_value = $y;
             setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
             ?>
             <!-- Cookieend -->
            '''  
       replace(file_path, subs)   
    elif file_path == 'search.php':
       subs='''
             <?php
             $cookie_name = "{flag}";
             $x = random_int(100, 999);
             $y = md5($x);
             $cookie_value = $y;
             setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
             ?>
             <!-- Cookieend -->
            '''  
       replace(file_path, subs)