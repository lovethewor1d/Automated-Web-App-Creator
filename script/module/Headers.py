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
    def replace(filePath, x, subs, flags=0):
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
            print("Please check the apps folder for your newly generated file")
    file_path=input("Please enter the filepath: ")
    x = input("Please enter the Header name: \n")
    #print(file_path)
    os.chdir(app)
    file_path=os.path.basename(file_path) # filename with extension
    #print(os.path.splitext(file_path)[0]) - filename without extension
    if file_path == 'headers.html':
       subs=x
       replace(file_path, x, subs)