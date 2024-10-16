from InquirerPy import prompt
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import pyotp
import qrcode
import re
import os
import string
import secrets
import random
import shutil
import module.globals

webapp = module.globals.DirCheck() 

def replacing():
    questions = [
        {
            "type": "confirm",
            "message": "\n SQL Injection code can be used in any of the following files: "
                       "\n comment.php \n index.php \n signup.php \n view.php \n types.php \n"
                       "\n XSS code can be used in any of the following files: "
                       "\n comment.php \n view.php \n"
                       "\n Malicious File Upload code can be used in any of the following files: "
                       "\n page2.php \n"
                       "\n RCE, LFI, RFI code can be used in any of the following files: "
                       "\n search.php \n",
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
                "SQLi - Easy","SQLi - Medium","SQLi-Hard","SQLi - Fixed","XSS - Easy", "XSS - Medium", "XSS - Hard", "XSS - Fixed", "Malicious File Upload - Easy", "Malicious File Upload - Medium", "Malicious File Upload - Hard", "Malicious File Upload - Fixed", "RCE - Easy","RCE - Medium","RCE - Hard","RCE - Fixed","LFI/RFI - Easy","LFI/RFI - Medium","LFI/RFI - Hard","LFI/RFI - Fixed", "Cookie - index.php", "Cookie - types.php", "Cookie - comment.php", "Cookie - view.php", "Cookie - page2.php", "Cookie - search.php", "Product Cars include/exclude", "Product Bikes include/exclude", "Product Planes include/exclude", "Product Laptops include/exclude", "Product Headphones include/exclude", "ZIP all the newly created files?"
            ],
            "multiselect": False
        },
    ]
    
    #result = prompt(questions=questions)
    x = questions[0]['choices']
    res = []
    #path = os.getcwd()
    #dir_list = os.listdir('module/')
    for file in os.listdir('module/'):
        if file.endswith('.py'):
            x.append(file.removesuffix('.py'))
    questions[0]['choices'] = x
    result = prompt(questions=questions)
    return result
    #print(result)