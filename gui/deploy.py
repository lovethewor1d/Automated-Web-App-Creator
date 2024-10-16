from InquirerPy import prompt
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import re
import os
import string
import shutil
import subprocess
import glob
import platform

def main1():
#menu
    questions = [
            {
                "type": "confirm",
                "message": "\n Using this, you can deploy and run the webapp via Docker \n"
                           #"\n Once testing is done, end the program (ctrl+c) and start it again \n"
                           #"\n To get the Source Code, choose option 2  \n"
                           "\n Continue?",
                "qmark": "🤔",
                "amark": "😲",
                "name": "proceed",
                "default": True,
            },
            {
                "type": "confirm",
                "message": "Confirm?",
                "when": lambda result: result.get("1", False),
            },
        ]
        
    result = prompt(questions)
        
    questions = [
        {
            "type": "list",
            "message": "Select your choice:",
            "qmark": "🧐",
            "amark": "✨",
            "choices": ["Deploy"],
            #"choices": ["Deploy","Source Code"],
            "multiselect": False
        },
    ]
    result = prompt(questions=questions)

#If else based on user choice   
 
    if result[0] == "Deploy":

        oss = platform.system()
        if oss == "Linux" or oss == "Linux2":
            desktopdeploy = os.path.expanduser("/tmp")
            result = subprocess.run(["docker-compose", "up"], cwd=os.path.join(desktopdeploy, 'doc'), capture_output=False, text=True)        
            print(result.stdout) 
        
        elif oss == "Darwin":
            desktopdeploy = os.path.expanduser("/tmp")
            result = subprocess.run(["docker-compose", "up"], cwd=os.path.join(desktopdeploy, 'doc'), capture_output=False, text=True)        
            print(result.stdout) 
        
        elif oss == "Windows":
            print(oss)
            desktopdeploy = os.path.expanduser("~\\Temp")
            result = subprocess.run(["docker-compose", "up"], cwd=os.path.join(desktopdeploy, 'doc'), capture_output=False, text=True)        
            print(result.stdout) 
            
#user option to hide the source code and extract in Desktop, only when student chooses this option and enters the correct flag
    #elif result[0] == 'Source Code':
    #    flag = 'loveSDFVGHYT$@#!$%^$YRHgefrew3145t' ### replace with the flag of your choice ###
    #    user_flag = input("Please enter the Flag found while your assessment: ")
    #    if user_flag == flag:
    #        oss = platform.system()
    #        
    #        if oss == "linux" or oss == "linux2":
    #            desktopmv = os.path.expanduser("/tmp")
    #            #working_directory = os.getcwd()
    #            working_directory=os.path.join(desktopmv, 'doc')
    #            #print(working_directory)
    #            retain = "app.zip"
    #            
    #            z = os.chdir(working_directory)
    #            y = os.listdir(working_directory)
    #            z=os.path.basename(retain)
    #            #z = os.path.splitext(retain)[0]
    #            print(z)
    #            for item in y:
    #                if item in retain:
    #                    desktop = os.path.expanduser("~/Desktop")
    #                    print(desktop)
    #                    shutil.move(z, desktop) 
    #            
    #            file_path=input("Please enter the PATH of the zip file (It may be on your Desktop ;)): \n")
    #            extract_dir=os.getcwd()
    #            shutil.unpack_archive(file_path, extract_dir)
    #            print("Folder un-zipped successfully! Please check your current working directory.")
    #        
    #        elif oss == "darwin":
    #            desktopmv = os.path.expanduser("/tmp")
    #            #working_directory = os.getcwd()
    #            working_directory=os.path.join(desktopmv, 'doc')
    #            #print(working_directory)
    #            retain = "app.zip"
    #            
    #            z = os.chdir(working_directory)
    #            y = os.listdir(working_directory)
    #            z=os.path.basename(retain)
    #            #z = os.path.splitext(retain)[0]
    #            print(z)
    #            for item in y:
    #                if item in retain:
    #                    desktop = os.path.expanduser("~/Desktop")
    #                    print(desktop)
    #                    shutil.move(z, desktop) 
    #            
    #            file_path=input("Please enter the PATH of the zip file (It may be on your Desktop ;)): \n")
    #            extract_dir=os.getcwd()
    #            shutil.unpack_archive(file_path, extract_dir)
    #            print("Folder un-zipped successfully! Please check your current working directory.")
    #        
    #        elif oss == "windows":
    #            desktopmv = os.path.expanduser("~\\Temp")
    #            #working_directory = os.getcwd()
    #            working_directory=os.path.join(desktopmv, 'doc')
    #            #print(working_directory)
    #            retain = "app.zip"
    #            
    #            z = os.chdir(working_directory)
    #            y = os.listdir(working_directory)
    #            z=os.path.basename(retain)
    #            #z = os.path.splitext(retain)[0]
    #            print(z)
    #            for item in y:
    #                if item in retain:
    #                    desktop = os.path.expanduser("~\\Desktop")
    #                    print(desktop)
    #                    shutil.move(z, desktop) 
    #            
    #            file_path=input("Please enter the PATH of the zip file (It may be on your Desktop ;)): \n")
    #            extract_dir=os.getcwd()
    #            shutil.unpack_archive(file_path, extract_dir)
    #            print("Folder un-zipped successfully! Please check your current working directory.")
    #    else:
    #        print("It seems like your flag is incorrect, try harder :)")
    else:
       print('Please choose the correct option.')
        
if __name__ == "__main__":
    main1()
    