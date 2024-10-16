from InquirerPy import prompt
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import pyotp
import qrcode
import re
import os
#import string
#import secrets
#import random
import shutil
import module.globals

#webapp = module.globals.DirCheck() 
#webapp template: https://www.free-css.com/free-css-templates/page240/air

def replacing():
    global result
    questions = [
        {
            "type": "confirm",
            "message": "\n Please read the README.txt file before proceeding ahead!"
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
            "choices": [
                Separator("\n Vulnerabilities: \n"), "SQLiEasy_login", "SQLiEasy_products", "SQLiMedium_login" , "SQLiMedium_products", "SQLiHard_login", "SQLiHard_products", "SQLiFixed_login", "SQLiFixed_products", "XSSEasy_comment", "XSSEasy_view", "XSSEasy_search", "XSSMedium_comment", "XSSMedium_view", "XSSMedium_search", "XSSHard_comment", "XSSHard_view", "XSSHard_search", "XSSFixed_comment", "XSSFixed_view", "XSSFixed_search", "FileUploadEasy", "FileUploadMedium", "FileUploadHard", "FileUploadFixed", "RCEEasy","RCEMedium","RCEHard","RCEFixed","LFIEasy","LFIMedium","LFIHard","LFIFixed", "CookieInject", "ProductCars", "ProductBikes", "ProductPlanes", "ProductLaptops", "ProductHeadphones", Separator(" \n CSS: \n"), "CSSstyle1", "CSSstyle2", "CSSstyle3", Separator(" \n ZIP/Deploy: \n"), "ZIPtheFiles", "DeployDockerfile", "DeployDockerfile_WithLogs", Separator(" \n Misc: \n")
            ],
            "multiselect": False
        },
    ]
    #result = prompt(questions=questions)
    x = questions[0]['choices']
    res = []
    temp = []
    nreq = ["menu.py", "menuOTP.py", "globals.py", "headers.html"]
    #path = os.getcwd()
    #dir_list = os.listdir('module/')
    for file in os.listdir('module/'):
        if file.endswith('.py'):
            if file not in nreq:
                x.append(file.removesuffix('.py'))
            for new in x:
                if new not in temp:
                    temp.append(new)
    questions[0]['choices'] = temp
    result = prompt(questions=questions)
    return result