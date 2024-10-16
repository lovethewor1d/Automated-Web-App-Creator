import os
import string
import secrets
import random
import shutil


#print("Creating a new Directory called 'app' \n")
current_directory = os.getcwd()
final_directory1 = os.path.join(current_directory, r'doc')
final_directory2 = os.path.join(final_directory1, r'app')
#os.chdir(final_directory2)
#if not os.path.exists(final_directory):
   #os.makedirs(final_directory)
app = final_directory2
#print(app)


def DirCheck():
    return app