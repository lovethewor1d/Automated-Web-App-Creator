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
    full_path = path+"\search.php"
    print(full_path)
    file_path=os.path.basename(full_path) # filename with extension
    #print(file_path)
    #print(os.path.splitext(file_path)[0]) - filename without extension
    if file_path == 'search.php':
       subs='''
       <!-- start -->
       <?php
       require_once "config.php";
       if(isset($_GET["id"]))
        {
       $id=$_GET['id'];
       //$pass = addslashes($_GET['id']);
       $con = mysqli_connect("db", "php_docker", "password", "php_docker");
       $stmt = $con->prepare("SELECT * FROM products WHERE name like ? OR type  like ?");
       $stmt->bind_param("ss", $id, $id);
       $stmt->execute();
       $result = $stmt->get_result();
       $stmt->close();
       echo $id;
       echo "<table border='1' align='center'>
       <H2 align='center'> Products Table </h2>
       <tr>
       <th>Product Type</th>
       <th>Product Name</th>
       <th>Product Price</th>
       </tr>";
       while ($fetch = mysqli_fetch_array($result))
       {
       echo "<tr>";
       echo "<td>" . $fetch['type'] . "</td>";
       echo "<td>" . $fetch['name'] . "</td>";
       echo "<td>" . $fetch['price'] . "</td>";
       echo "</tr>";
       }
       echo "</table>";
       }
       ?>
       <!-- end -->
       '''
       replace(file_path, subs)