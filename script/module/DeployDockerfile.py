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

def replacing(): 
    oss = platform.system()
    if oss == "Linux" or oss =="Linux2":
        result = subprocess.run(["pyinstaller", "--onefile", "-F", "--add-data=doc:doc", "--runtime-hook=hook.py", "deploy.py"], capture_output=False, text=True)            
        print(result.stdout)
        print("Please share the .exe file in 'dist' folder with the students.")
    elif oss == "Darwin":
        result = subprocess.run(["pyinstaller", "--onefile", "-F", "--add-data=doc:doc", "--runtime-hook=hook.py", "deploy.py"], capture_output=False, text=True)            
        print(result.stdout)
        print("Please share the .exe file in 'dist' folder with the students.")
    elif oss == "Windows":
        result = subprocess.run(["pyinstaller", "--onefile", "-F", "--add-data=doc;doc", "--runtime-hook=hook.py", "deploy.py"], capture_output=False, text=True)            
        print(result.stdout)
        print("Please share the .exe file in 'dist' folder with the students.")