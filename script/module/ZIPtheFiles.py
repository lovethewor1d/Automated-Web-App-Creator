import os
import shutil
import time
#import module.globals

#webapp = module.globals.DirCheck() 

def replacing():
    file_path=input("Please enter the PATH of the folder to be zipped! \n")
    shutil.make_archive('app', format='zip', root_dir=file_path)
    print("The folder is being compressed, please wait !")
    #time.sleep(5)
    print("Folder zipped successfully! Please check your current working directory.")
    retain = "app.zip"  
    working_directory=os.getcwd()
    z = os.chdir(working_directory)
    y = os.listdir(working_directory)
    z=os.path.basename(retain)
    #z = os.path.splitext(retain)[0]
    #print(z)
    for item in y:
        if item in retain:
            shutil.copy(z, "doc") 