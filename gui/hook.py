import sys
import os
import shutil
import platform

oss = platform.system()
if oss == "Linux" or oss == "Linux2":
    path = getattr(sys, '_MEIPASS', os.getcwd())
    
    full_path = path+"/doc"
    desktop = os.path.expanduser("/tmp")
    #print(desktop)
    #print(full_path)
    try:
        shutil.move(full_path, desktop)
        #print(full_path)
    except:
        print("Cannot create 'doc' folder. Already exists.")

elif oss == "Darwin":

    path = getattr(sys, '_MEIPASS', os.getcwd())
    
    full_path = path+"/doc"
    desktop = os.path.expanduser("/tmp")
    #print(desktop)
    #print(full_path)
    try:
        shutil.move(full_path, desktop)
        #print(full_path)
    except:
        print("Cannot create 'doc' folder. Already exists.")
        
elif oss == "Windows":

    path = getattr(sys, '_MEIPASS', os.getcwd())
    
    full_path = path+"\\doc"
    desktop = os.path.expanduser("~\\Temp")
    #print(desktop)
    #print(full_path)
    try:
        shutil.move(full_path, desktop)
        #print(full_path)
    except:
        print("Cannot create 'doc' folder. Already exists.")


#path = getattr(sys, '_MEIPASS', os.getcwd())
#
#full_path = path+"\\doc"
#desktop = os.path.expanduser("~\\Temp")
##print(desktop)
##print(full_path)
#try:
#    shutil.move(full_path, desktop)
#    #print(full_path)
#except:
#    print("Cannot create 'doc' folder. Already exists.")
#    #https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile