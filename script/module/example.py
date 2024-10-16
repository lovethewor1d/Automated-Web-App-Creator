import re
import os
import string
import secrets
import random
import shutil
import module.globals

app = module.globals.DirCheck() 
#
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
    file_path=input("Please enter the filepath: ")
    #print(file_path)
    os.chdir(app) 
    file_path=os.path.basename(file_path) # filename with extension
    #print(os.path.splitext(file_path)[0]) - filename without extension, not to use
    if file_path == 'index.php': #For ADMIN: change the file name depending in which file you need to add the vulnerability.
                                 #You can choose a new file or #use any existing files
       subs='''
       <!-- start -->
#Replace me: put your vulnerable code here#
       <!-- end -->'''
       
       replace(file_path, subs)  
    #print(file_path)       
    elif file_path == 'products.php': #by using the elif loop, you can specify multiple files, if required, else please remove the elif loop.
       subs='''
       <!-- start -->
       ##add your vulnerable code here##
       <!-- end -->'''
       
       replace(file_path, subs)