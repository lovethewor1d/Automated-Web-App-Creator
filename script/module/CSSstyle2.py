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
            print("Please check the apps folder for your newly generated file")
    file_path=input("Please enter the filepath: ")
    #print(file_path)
    os.chdir(app)
    file_path=os.path.basename(file_path)
    #print(file_path)
    #print(os.path.splitext(file_path)[0])
    if file_path == 'index.php':
       subs='''
             <link rel="stylesheet" href="style1.css">
            '''  
       replace(file_path, subs)  
    elif file_path == 'home.html':
       subs='''
             <link rel="stylesheet" href="style1.css">
            '''  
       replace(file_path, subs) 
    elif file_path == 'comment.php':
       subs='''
             <link rel="stylesheet" href="style1.css">
            '''  
       replace(file_path, subs)  
    elif file_path == 'view.php':
       subs='''
             <link rel="stylesheet" href="style1.css">
            '''  
       replace(file_path, subs)  
    elif file_path == 'products.html':
       subs='''
             <link rel="stylesheet" href="style1.css">
            '''  
       replace(file_path, subs)   
    elif file_path == 'products.php':
       subs='''
             <link rel="stylesheet" href="style1.css">
            '''  
       replace(file_path, subs)
    elif file_path == 'search.php':
       subs='''
             <link rel="stylesheet" href="style1.css">
            '''  
       replace(file_path, subs)
    elif file_path == 'signup.php':
       subs='''
             <link rel="stylesheet" href="style1.css">
            '''  
       replace(file_path, subs)
    elif file_path == 'feedback.html':
       subs='''
             <link rel="stylesheet" href="style1.css">
            '''  
       replace(file_path, subs)
    elif file_path == 'upload.html':
       subs='''
             <link rel="stylesheet" href="style1.css">
            '''  
       replace(file_path, subs)
    elif file_path == 'search.html':
       subs='''
             <link rel="stylesheet" href="style1.css">
            '''  
       replace(file_path, subs)