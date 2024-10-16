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
import module.SQLiEasy_login
import module.SQLiEasy_products
import module.SQLiMedium_login
import module.SQLiMedium_products
import module.SQLiHard_login
import module.SQLiHard_products
import module.SQLiFixed_login
import module.SQLiFixed_products
import module.XSSEasy_comment
import module.XSSEasy_view
import module.XSSEasy_search
import module.XSSMedium_comment
import module.XSSMedium_view
import module.XSSMedium_search
import module.XSSHard_comment
import module.XSSHard_view
import module.XSSHard_search
import module.XSSFixed_comment
import module.XSSFixed_view
import module.XSSFixed_search
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
import module.DeployDockerfile_WithLogs
key = "test"

#importing globals.py to load the webapp directory
webapp = module.globals.DirCheck()

def main1():
#menu
    global result
    result = module.menu.replacing()
#If else based on user choice   
 
    if result[0] == "SQLiEasy_login":
        module.SQLiEasy_login.replacing()    
    if result[0] == "SQLiEasy_products":
        module.SQLiEasy_products.replacing()         
    elif result[0] == "SQLiMedium_login":
        module.SQLiMedium_login.replacing()
    elif result[0] == "SQLiMedium_products":
        module.SQLiMedium_products.replacing()
    elif result[0] == "SQLiHard_login":  
        module.SQLiHard_login.replacing()
    elif result[0] == "SQLiHard_products":  
        module.SQLiHard_products.replacing()
    elif result[0] == "SQLiFixed_login":  
        module.SQLiFixed_login.replacing()
    elif result[0] == "SQLiFixed_products":  
        module.SQLiFixed_products.replacing()
####
    elif result[0] == "XSSEasy_comment":                     
        module.XSSEasy_comment.replacing() 
    elif result[0] == "XSSEasy_view":                     
        module.XSSEasy_view.replacing() 
    elif result[0] == "XSSEasy_search":                     
        module.XSSEasy_search.replacing() 
    elif result[0] == "XSSMedium_comment":  
        module.XSSMedium_comment.replacing()
    elif result[0] == "XSSMedium_view":  
        module.XSSMedium_view.replacing()
    elif result[0] == "XSSMedium_search":  
        module.XSSMedium_search.replacing()
    elif result[0] == "XSSHard_comment":  
        module.XSSHard_comment.replacing()
    elif result[0] == "XSSHard_view":  
        module.XSSHard_view.replacing()
    elif result[0] == "XSSHard_search":  
        module.XSSHard_search.replacing()
    elif result[0] == "XSSFixed_comment":  
        module.XSSFixed_comment.replacing()
    elif result[0] == "XSSFixed_view":  
        module.XSSFixed_view.replacing()
    elif result[0] == "XSSFixed_search":  
        module.XSSFixed_search.replacing()
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
        module.ZIPtheFiles.replacing()
#####
    elif result[0] == "DeployDockerfile":
        module.DeployDockerfile.replacing() #DeployDockerfile.py uses deploy.py, create exe using below command:
        #pyinstaller  --onefile -F --add-data=doc;doc --runtime-hook=hook.py deploy.py
    elif result[0] == "DeployDockerfile_WithLogs":
        module.DeployDockerfile_WithLogs.replacing()
#####
    ##add the elif loop for the new vulnerabilities here##
    ##elif result[0] == "Vulnerability Name Here":##
    ##    module.VulnerabilityName.replacing()##
        
if __name__ == "__main__":
    main1()