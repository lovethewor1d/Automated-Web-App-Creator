from InquirerPy import prompt
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import pyotp
import qrcode
import re
import os
import shutil
### add requirements.txt...
#import pyflyby
### can use pyflyby.. instead of above imports
import module.SQLiEasy
import module.SQLiMedium
import module.SQLiHard
import module.SQLiFixed
import module.XSSEasy
import module.XSSMedium
import module.XSSHard
import module.XSSFixed
import module.FileUploadEasy
import module.FileUploadMedium
import module.FileUploadHard
import module.FileUploadFixed
import module.RCEEasy
import module.RCEMedium
import module.RCEHard
import module.RCEFixed
import module.LFIEasy
import module.LFIMedium
import module.LFIHard
import module.LFIFixed
import module.CookieInject
import module.ProductCars
import module.ProductBikes
import module.ProductPlanes
import module.ProductLaptops
import module.ProductHeadphones
import module.menu
import module.globals
import module.CSSstyle1
import module.CSSstyle2
import module.CSSstyle3
import module.ZIPtheFiles
import module.DeployDockerfile

key = "test"

#importing globals.py to load the webapp directory
webapp = module.globals.DirCheck()

def main1():
#menu
    global result
    result = module.menu.replacing()
#If else based on user choice   
 
    if result[0] == "SQLiEasy":
        module.SQLiEasy.replacing()       
    elif result[0] == "SQLiMedium":
        module.SQLiMedium.replacing()
    elif result[0] == "SQLiHard":  
        module.SQLiHard.replacing()
    elif result[0] == "SQLiFixed":  
        module.SQLiFixed.replacing()
####
    elif result[0] == "XSSEasy":                     
        module.XSSEasy.replacing() 
    elif result[0] == "XSSMedium":  
        module.XSSMedium.replacing()
    elif result[0] == "XSSHard":  
        module.XSSHard.replacing()
    elif result[0] == "XSSFixed":  
        module.XSSFixed.replacing()
#####
    elif result[0] == "FileUploadEasy":               
        module.FileUploadEasy.replacing()
    elif result[0] == "FileUploadMedium":  
        module.FileUploadMedium.replacing()   
    elif result[0] == "FileUploadHard":  
        module.FileUploadHard.replacing() 
    elif result[0] == "FileUploadFixed":  
        module.FileUploadFixed.replacing()  
#####
    elif result[0] == "RCEEasy":
        module.RCEEasy.replacing()
    elif result[0] == "RCEMedium":  
        module.RCEMedium.replacing()           
    elif result[0] == "RCEHard":  
        module.RCEHard.replacing()          
    elif result[0] == "RCEFixed":  
        module.RCEFixed.replacing()
#####
    elif result[0] == "LFIEasy":
        module.LFIEasy.replacing()
    elif result[0] == "LFIMedium":  
        module.LFIMedium.replacing()
    elif result[0] == "LFIHard":  
        module.LFIHard.replacing()
    elif result[0] == "LFIFixed":  
        module.LFIFixed.replacing()
#####
    elif result[0] == "CookieInject": 
        module.CookieInject.replacing()
    elif result[0] == "ProductCars":
        module.ProductCars.replacing()
    elif result[0] == "ProductBikes":
        module.ProductBikes.replacing()
    elif result[0] == "ProductPlanes":
        module.ProductPlanes.replacing()
    elif result[0] == "ProductLaptops":
        module.ProductLaptops.replacing()
    elif result[0] == "ProductHeadphones":
        module.ProductHeadphones.replacing()
#####
    elif result[0] == "CSSstyle1":
        module.ProductCars.replacing()
    elif result[0] == "CSSstyle2":
        module.ProductCars.replacing()
    elif result[0] == "CSSstyle3":
#####
        module.ProductCars.replacing()
    elif result[0] == "ZIPtheFiles":
#####
        module.ZIPtheFiles.replacing()
    elif result[0] == "DeployDockerfile":
        module.DeployDockerfile.replacing() #DeployDockerfile.py uses deploy.py, create exe using below command:
        #pyinstaller  --onefile -F --add-data=doc;doc --runtime-hook=hook.py deploy.py
#####
    ##add the elif loop for the new vulnerabilities here##
    else:
       print("Please choose the correct option.")
        
if __name__ == "__main__":
    main1()