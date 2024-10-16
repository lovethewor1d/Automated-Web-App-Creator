import re
import os
import string
import secrets
import random
import shutil
import module.globals
import sys
app = module.globals.DirCheck() 

def replacing():
    def replace(filePath, subs, flags=0):
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
            #shutil.copy(file_path, app) 
            #print("Code Replacement Process Successful \n")
            print("Please check the apps folder for your newly modified file")
    #file_path=input("Please enter the filepath: ")
    #print(file_path)
    os.chdir(app) ###################add this on other modules
    path = getattr(sys, '_MEIPASS', os.getcwd())
    full_path = path+r"\upload.php"
    print(full_path)
    file_path=os.path.basename(full_path) # filename with extension
    #print(file_path)
    #print(os.path.splitext(file_path)[0]) - filename without extension
    if file_path == 'upload.php':
       subs='''
       <!-- start -->
       <?php
       require_once "config.php";
       if( isset( $_POST[ 'Upload' ] ) ) {
           die("There is no file to upload.");
       }
       
       $filepath = $_FILES['myFile']['tmp_name'];
       $fileSize = filesize($filepath);
       $fileinfo = finfo_open(FILEINFO_MIME_TYPE);
       $filetype = finfo_file($fileinfo, $filepath);
       
       if ($fileSize === 0) {
           die("The file is empty.");
       }
       
       if ($fileSize > 3145728) { // 3 MB (1 byte * 1024 * 1024 * 3 (for 3 MB))
           die("The file is too large");
       }
       
       $allowedTypes = [
          'image/png' => 'png',
          'image/jpeg' => 'jpg'
       ];
       
       if (!in_array($filetype, array_keys($allowedTypes))) {
           die("File not allowed.");
       }
       
       $filename = basename($filepath);
       $extension = $allowedTypes[$filetype];
       $targetDirectory = __DIR__ . "/documents";
       
       $newFilepath = $targetDirectory . "//" . $filename . "." . $extension;
       
       if (!copy($filepath, $newFilepath))
       {
           die("Cant move file.");
       }
       unlink($filepath);
       ?>
       <a class=".back_button" href="javascript:history.back(1)">go back</a>
       <!-- end -->'''
       
       replace(file_path, subs)