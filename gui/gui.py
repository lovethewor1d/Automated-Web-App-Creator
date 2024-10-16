import tkinter as tk
from tkinter import ttk
from tkinter import *
import ctypes
import tkinter.font as font
import sys
import os
import string
import random
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import re
import glob
import shutil
import platform 
import subprocess

#ctypes.windll.shcore.SetProcessDpiAwareness(1)
global win
def win():
    win = ttk.Window(themename="superhero")
    win.geometry("1500x600")
    win.title("Vulnerable App Creator for Pen-testing")
    font1=('Arial',10,'normal')   
    ######menu
    def about():
        newWindow = Toplevel(win)
        newWindow.title("About Ciphers")
        win.geometry("1500x1000")
        msg00 = ttk.Label(newWindow, text='Step 1: Modifying the application files:', bootstyle=INFO)
        msg00.grid(row=1,column=1,padx=5,pady=5,columnspan=1, sticky=W)
        msg001 = ttk.Label(newWindow, text='SQL Injection code can be used in "index.php" and "products.php"', bootstyle=INFO)
        msg001.grid(row=3,column=1,padx=5,pady=5,columnspan=1, sticky=W)
        msg002 = ttk.Label(newWindow, text='XSS code can be used in "search.php", "comment.php" and "view.php"', bootstyle=INFO)
        msg002.grid(row=5,column=1,padx=5,pady=5,columnspan=1, sticky=W)
        msg003 = ttk.Label(newWindow, text='File Upload code can be used in "page2.php"', bootstyle=INFO)
        msg003.grid(row=7,column=1,padx=5,pady=5,columnspan=1, sticky=W)
        msg004 = ttk.Label(newWindow, text='RCE and LFI code can be used in "include.php"', bootstyle=INFO)
        msg004.grid(row=9,column=1,padx=5,pady=5,columnspan=1, sticky=W)
        msg005 = ttk.Label(newWindow, text='Cookies containing flag can be set in "home.php"', bootstyle=INFO)
        msg005.grid(row=11,column=1,padx=5,pady=5,columnspan=1, sticky=W)
        msg006 = ttk.Label(newWindow, text='Cars, Bikes, Planes, Laptops, Headphones products are available to include/exclude in the application"', bootstyle=INFO)
        msg006.grid(row=13,column=1,padx=5,pady=5,columnspan=1, sticky=W)
        msg007 = ttk.Label(newWindow, text='CSS can be modified in index.php, home.html, comment.php, view.php, products.html, products.php, search.php, search.html, include.php, signup.php, feedback.html, upload.html', bootstyle=INFO)
        msg007.grid(row=15,column=1,padx=5,pady=5,columnspan=1, sticky=W)
        msg008 = ttk.Label(newWindow, text='Creating the ZIP file: ', bootstyle=INFO)
        msg008.grid(row=17,column=1,padx=5,pady=5,columnspan=1, sticky=W)
        msg009 = ttk.Label(newWindow, text='You can zip the app folder by choosing the "ZIP all the newly created files?" option in the menu', bootstyle=INFO)
        msg009.grid(row=19,column=1,padx=5,pady=5,columnspan=1, sticky=W)
        msg010 = ttk.Label(newWindow, text='You can create the deployable .exe file by choosing the "Create Docker File" in the menu. \n This file can be shared with the Students or Participants.', bootstyle=INFO)
        msg010.grid(row=21,column=1,padx=5,pady=5,columnspan=1, sticky=W)
    menubar = Menu(win, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')
    file = Menu(menubar, tearoff=1, background='#ffcc99', foreground='black')
    help = Menu(menubar, tearoff=0)  
    help.add_command(label="About", command=about)  
    menubar.add_cascade(label="Help", menu=help)  
    global StringVar
    sel=ttk.StringVar()
    msg0 = ttk.Label(win, text='Please select from the below options:', bootstyle=INFO)
    msg0.grid(row=1,column=100,padx=5,pady=5,columnspan=300)
    my_opts=["SQLi - Easy","SQLi - Medium","SQLi-Hard","SQLi - Fixed","XSS - Easy", "XSS - Medium", "XSS - Hard", "XSS - Fixed", "Malicious File Upload - Easy", "Malicious File Upload - Medium", "Malicious File Upload - Hard", "Malicious File Upload - Fixed", "RCE - Easy","RCE - Medium","RCE - Hard","RCE - Fixed","LFI - Easy","LFI - Medium","LFI - Hard","LFI - Fixed", "Cookie", "Modify Products", "ZIP all the newly created files?", "Create Docker File"]
    cb1 = ttk.Combobox(win, values=my_opts,width=25,height=10,
            textvariable=sel,font=font1, bootstyle=DANGER)
    cb1.grid(row=5,column=100,padx=5,pady=5,columnspan=3) 
    
    def my_upd(*args):
        for w in win.grid_slaves(2): 
            w.grid_remove() 
    
        if(sel.get()=='SQLi - Easy'):
            outmsg = StringVar()
            user_choice = IntVar() 
            def sqli_low_index():
              global file_path
              msg = ""
              message = msg
              def replace(subs, flags=re.DOTALL):
                 with open(file_path, "r+") as file:
                      x = file.read()
                      y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                      print(y)
                      result = '\n'.join(y)
                      text_pattern = re.compile(re.escape(result), flags)
                      file_contents = text_pattern.sub(subs, x)
                      file.seek(0)
                      file.truncate()
                      file.write(file_contents)
                    
              #file_path=input("Please enter the filepath: ")
              #file=os.path.basename(file)
              #print(os.path.splitext(file_path)[0])
              #if file_path == 'index.php':
              subs='''
              <!-- start -->
              <?php
                     require_once "auth_check.php";
                     require_once "config.php";
              if(isset($_GET["id_submit"]))
              {    
                  $username=$_GET['username'];  
                  $password=$_GET['password'];  
                  $query=mysqli_query($db,"SELECT * FROM users WHERE username='$username' AND password='$password'");
                  if(mysqli_num_rows($query) > 0){
                      while($data = mysqli_fetch_assoc($query)){
                          header("Location: home.html");}  
                  }else{
                       echo '<span style="color:white;text-align:center;">Invalid username and password</span>';
                  } 	
              }	
              ?>
              <!-- end -->'''
              
              replace(subs)
              mssg = "Done"
              outmsg.set(mssg)

            def sqli_low_products():
              global file_path
              msg = ""
              message = msg
              def replace(subs, flags=re.DOTALL):
                 with open(file_path, "r+") as file:
                      x = file.read()
                      y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                      print(y)
                      result = '\n'.join(y)
                      text_pattern = re.compile(re.escape(result), flags)
                      file_contents = text_pattern.sub(subs, x)
                      file.seek(0)
                      file.truncate()
                      file.write(file_contents)
                    
              #file_path=input("Please enter the filepath: ")
              #file=os.path.basename(file)
              #print(os.path.splitext(file_path)[0])
              #if file_path == 'index.php':
              subs='''
              <!-- start -->
              <?php
              require_once "auth_check.php";
              require_once "config.php";
              //require_once "protect.php";
		       if(isset($_GET["id"]))
		           {
              $id=$_GET['id'];
              $con = mysqli_connect("db", "php_docker", "password", "php_docker");
              $query="SELECT * FROM products WHERE id='$id'";
              $result = mysqli_query($con, $query);
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
              <!-- end -->'''
              
              replace(subs)
              mssg = "Done"
              outmsg.set(mssg)
            def upload_file():
              global file_path
              file_path = filedialog.askopenfilename()
              print("file is: ", file_path)
              if file:
                 pass            
              else:
                  print("No file selected") 
            def con():
              global file_path
              choice = user_choice.get()     
             
              file=os.path.basename(file_path)
              if choice == 0:
                  #file=os.path.basename(file_path)
                  #print(file)
                  if file == 'index.php':
                      sqli_low_index()
                  else:
                     mssg = "Please choose the correct file"
                     outmsg.set(mssg)               
              elif choice == 1:
                  if file =='products.php':
                      sqli_low_products()
                  else:
                     mssg = "Please choose the correct file"
                     outmsg.set(mssg)  
            msg1 = ttk.Radiobutton(win, text="index.php", variable=user_choice, value=0, bootstyle=DANGER).place(
                relx=0.75, rely=0.2, anchor=CENTER)
            msg2 = ttk.Radiobutton(win, text="products.php", variable=user_choice, value=1, bootstyle=DANGER).place(
                relx=0.75, rely=0.3, anchor=CENTER)
            b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
            b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
            msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
            msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
            stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
            stop.place(relx=0.10, rely=1, anchor=SE)
            
            
            out = Entry(win, text=outmsg).place(
                relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
            
            convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
            convert.place(relx=0.5, rely=0.4, anchor=CENTER)    
            
        elif(sel.get()=='SQLi - Medium'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def sqli_med_index():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            require_once "auth_check.php";
            require_once "config.php";
            if(isset($_GET["id_submit"]))
            {    
                $username=$_GET['username'];  
                $password=$_GET['password'];  
            	//$query=mysqli_query($db,"SELECT * FROM users WHERE username= $username AND passcode= $password"); - when using this, getting an error
                $query=mysqli_query($db,"SELECT * FROM admin WHERE username= $username AND password= $password");
                if(mysqli_num_rows($query) != 0) //if user:password from db then go to home.html, otherwise invalid.
            	{  
                header("Location: home.html");}  
            	else {  
                echo '<span style="color:white;text-align:center;">Invalid username and password</span>';
            	} 	
            }	
            ?>
              <!-- end -->'''
              
            replace(subs)
            mssg = "Done"
            outmsg.set(mssg)
          
          def sqli_med_products():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            require_once "auth_check.php";
            require_once "config.php";
            //require_once "protect.php";
		     if(isset($_GET["id"]))
		         {
            $id=$_GET['id'];
            $con = mysqli_connect("db", "php_docker", "password", "php_docker");
            $query="SELECT * FROM products WHERE id= $id";
            $result = mysqli_query($con, $query);
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
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'index.php':
                    sqli_med_index()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)               
            elif choice == 1:
                if file =='products.php':
                    sqli_med_products()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)  
          
          msg1 = ttk.Radiobutton(win, text="index.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          msg3 = ttk.Radiobutton(win, text="products.php", variable=user_choice, value=1, bootstyle=INFO).place(
              relx=0.76 , rely=0.4, anchor=CENTER)
          
          #msg1 = ttk.Label(win, text='Please upload the file', bootstyle=INFO)
          #msg1.place(relx=0.5, rely=0.05, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          
          
          
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER)
    
        elif(sel.get()=='SQLi - Hard'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def sqli_high_index():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
          <!-- start -->
          <?php
          require_once "auth_check.php";
          require_once "config.php";
          if(isset($_GET["id_submit"]))
          {    
              $username=$_GET['username'];  
              $password=$_GET['password'];
          	//$query=mysqli_query($db,"SELECT * FROM users WHERE username= $username LIMIT 1 AND passcode= $password LIMIT 1"); - when using this, getting an error
              $query=mysqli_query($db,"SELECT * FROM admin WHERE username= $username LIMIT 1 AND password= $password LIMIT 1");
              if(mysqli_num_rows($query) != 0) //if user:password from db then go to home.html, otherwise invalid.
          	{  
              header("Location: home.html");}  
          	else {  
              echo '<span style="color:white;text-align:center;">Invalid username and password</span>';
          	} 	
          }	
          ?>
          <!-- end -->'''
              
            replace(subs)
            mssg = "Done"
            outmsg.set(mssg)
          
          def sqli_high_products():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            require_once "auth_check.php";
            require_once "config.php";
            //require_once "protect.php";
		     if(isset($_GET["id"]))
		         {
            $id=$_GET['id'];
            $con = mysqli_connect("db", "php_docker", "password", "php_docker");
            $query="SELECT * FROM products WHERE id= $id LIMIT 1";
            $result = mysqli_query($con, $query);
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
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'index.php':
                    sqli_high_index()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)               
            elif choice == 1:
                if file =='products.php':
                    sqli_high_products()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)  
          
          msg1 = ttk.Radiobutton(win, text="index.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          msg3 = ttk.Radiobutton(win, text="products.php", variable=user_choice, value=1, bootstyle=INFO).place(
              relx=0.76 , rely=0.4, anchor=CENTER)
          
          #msg1 = ttk.Label(win, text='Please upload the file', bootstyle=INFO)
          #msg1.place(relx=0.5, rely=0.05, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          
          
          
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER)
          
        elif(sel.get()=='SQLi - Fixed'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def sqli_fixed_index():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
          <!-- start -->
          <?php
          require_once "auth_check.php";
          require_once "config.php";
          $con = mysqli_connect("localhost", "root", "", "database");
          if(isset($_GET["id_submit"]))
          {    
              $username=addslashes($_GET['username']);  
              $password=addslashes($_GET['password']);
          	$stmt = $con->prepare("SELECT * FROM admin WHERE username= ? LIMIT 1 AND password= ? LIMIT 1");
          	$stmt->bind_param("ss", $username, $password);
          	$stmt->execute();
          	$result = $stmt->get_result();
          	$stmt->close();
              if(mysqli_num_rows($result) != 0) //if user:password from db then go to home.html, otherwise invalid.
          	{  
              header("Location: home.html");}  
          	else {  
              echo '<span style="color:white;text-align:center;">Invalid username and password</span>';
          	} 	
          }	
          ?>
          <!-- end -->'''
              
            replace(subs)
            mssg = "Done"
            outmsg.set(mssg)
          
          def sqli_fixed_products():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            require_once "auth_check.php";
            require_once "config.php";
            //require_once "protect.php";
		     if(isset($_GET["id"]))
		         {
            $id=$_GET['id'];
            $pass = addslashes($_GET['id']);
            $con = mysqli_connect("db", "php_docker", "password", "php_docker");
            $stmt = $con->prepare("SELECT * FROM products WHERE id=? LIMIT 1");
            $stmt->bind_param("s", $pass);
            $stmt->execute();
            $result = $stmt->get_result();
            $stmt->close();
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
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'index.php':
                    sqli_fixed_index()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)               
            elif choice == 1:
                if file =='products.php':
                    sqli_fixed_products()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)  
          
          msg1 = ttk.Radiobutton(win, text="index.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          msg3 = ttk.Radiobutton(win, text="products.php", variable=user_choice, value=1, bootstyle=INFO).place(
              relx=0.76 , rely=0.4, anchor=CENTER)
          
          #msg1 = ttk.Label(win, text='Please upload the file', bootstyle=INFO)
          #msg1.place(relx=0.5, rely=0.05, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          
          
          
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER) 
    
        elif(sel.get()=='XSS - Easy'):
          def xss_low_comment():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            require_once "auth_check.php";
            require_once "config.php";
            $name = $_POST['name'];
            $comment = $_POST['comment'];
            $con = mysqli_connect("db", "php_docker", "password", "php_docker");
            $query = "INSERT INTO commentsnew (name, comment) VALUES ('$name', '$comment')";
            $result = mysqli_query($con, $query);
            echo("<script>location.href = 'feedback.html';</script>");
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          
          def xss_low_view():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            require_once "auth_check.php";
            require_once "config.php";
            $con = mysqli_connect("db", "php_docker", "password", "php_docker");
            $sql = "SELECT * FROM commentsnew";
            $result = mysqli_query($con, $sql);
            while ($row = $result->fetch_assoc()) {
            echo "name:"; echo $row['name']."<br>";
            echo "comment:"; echo $row['comment']."<br><br>";
            }
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def xss_low_search():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
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
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'comment.php':
                    xss_low_comment()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)               
            elif choice == 1:
                if file =='view.php':
                    xss_low_view()
            elif choice == 2:
                if file =='search.php':
                    xss_low_view()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)  
          
          msg1 = ttk.Radiobutton(win, text="comment.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          msg2 = ttk.Radiobutton(win, text="view.php", variable=user_choice, value=1, bootstyle=INFO).place(
              relx=0.75, rely=0.3, anchor=CENTER)
          msg3 = ttk.Radiobutton(win, text="search.php", variable=user_choice, value=2, bootstyle=INFO).place(
              relx=0.75, rely=0.3, anchor=CENTER)
          
          #msg1 = ttk.Label(win, text='Please upload the file', bootstyle=INFO)
          #msg1.place(relx=0.5, rely=0.05, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          
          
          
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER)
          
        elif(sel.get()=='XSS - Medium'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def xss_med_comment():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            require_once "auth_check.php";
            require_once "config.php";
            $name = $_POST['name'];
            $comment = $_POST['comment'];
            $strname = str_ireplace( '<script>', '', $_POST['name'] ); 
            $strcomment = str_ireplace( '<script>', '', $_POST['comment'] );
            $con = mysqli_connect("db", "php_docker", "password", "php_docker");
            $query = "INSERT INTO commentsnew (name, comment) VALUES ('$strname', '$strcomment')";
            $result = mysqli_query($con, $query);
            echo("<script>location.href = 'feedback.html';</script>");
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          
          def xss_med_view():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            require_once "auth_check.php";
            require_once "config.php";
            $con = mysqli_connect("db", "php_docker", "password", "php_docker");
            $sql = "SELECT * FROM commentsnew";
            $result = mysqli_query($con, $sql);
            while ($row = $result->fetch_assoc()) {
            echo "name:"; echo $row['name']."<br>";
            echo "comment:"; echo $row['comment']."<br><br>";
            }
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def xss_med_search():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            require_once "config.php";
            if(isset($_GET["id"]))
             {
            $id=$_GET['id'];
            $strname = str_ireplace( '<script>', '', $_GET["id"] );
            $con = mysqli_connect("db", "php_docker", "password", "php_docker");
            $stmt = $con->prepare("SELECT * FROM products WHERE name like ? OR type  like ?");
            $stmt->bind_param("ss", $strname, $strname);
            $stmt->execute();
            $result = $stmt->get_result();
            $stmt->close();
            echo $strname;
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
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'comment.php':
                    xss_med_comment()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)               
            elif choice == 1:
                if file =='view.php':
                    xss_med_view()
            elif choice == 2:
                if file =='search.php':
                    xss_med_view()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)  
          
          msg1 = ttk.Radiobutton(win, text="comment.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          msg2 = ttk.Radiobutton(win, text="view.php", variable=user_choice, value=1, bootstyle=INFO).place(
              relx=0.75, rely=0.3, anchor=CENTER)
          msg3 = ttk.Radiobutton(win, text="search.php", variable=user_choice, value=2, bootstyle=INFO).place(
              relx=0.75, rely=0.3, anchor=CENTER)
          
          #msg1 = ttk.Label(win, text='Please upload the file', bootstyle=INFO)
          #msg1.place(relx=0.5, rely=0.05, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          
          
          
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER)
    
        elif(sel.get()=='XSS - Hard'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def xss_hard_comment():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            require_once "auth_check.php";
            require_once "config.php";
            $name = $_POST['name'];
            $comment = $_POST['comment'];
            $strname = str_ireplace( '<script>', '', $_POST['name'] ); 
            $strcomment = str_ireplace( '<script>', '', $_POST['comment'] );
            $con = mysqli_connect("db", "php_docker", "password", "php_docker");
            $query = "INSERT INTO commentsnew (name, comment) VALUES ('$strname', '$strcomment')";
            $result = mysqli_query($con, $query);
            echo("<script>location.href = 'feedback.html';</script>");
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          
          def xss_hard_view():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            require_once "auth_check.php";
            require_once "config.php";
            $con = mysqli_connect("db", "php_docker", "password", "php_docker");
            $sql = "SELECT * FROM commentsnew";
            $result = mysqli_query($con, $sql);
            while ($row = $result->fetch_assoc()) {
            echo "name:"; echo $row['name']."<br>";
            echo "comment:"; echo $row['comment']."<br><br>";
            }
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def xss_hard_search():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            require_once "config.php";
            if(isset($_GET["id"]))
             {
            $id=$_GET['id'];
            $strname = str_ireplace( 'alert', '', $_GET["id"] );
            $con = mysqli_connect("db", "php_docker", "password", "php_docker");
            $stmt = $con->prepare("SELECT * FROM products WHERE name like ? OR type  like ?");
            $stmt->bind_param("ss", $strname, $strname);
            $stmt->execute();
            $result = $stmt->get_result();
            $stmt->close();
            echo $strname;
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
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'comment.php':
                    xss_hard_comment()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)               
            elif choice == 1:
                if file =='view.php':
                    xss_hard_view()
            elif choice == 2:
                if file =='search.php':
                    xss_hard_view()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)  
          
          msg1 = ttk.Radiobutton(win, text="comment.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          msg2 = ttk.Radiobutton(win, text="view.php", variable=user_choice, value=1, bootstyle=INFO).place(
              relx=0.75, rely=0.3, anchor=CENTER)
          msg3 = ttk.Radiobutton(win, text="search.php", variable=user_choice, value=2, bootstyle=INFO).place(
              relx=0.75, rely=0.3, anchor=CENTER)
          
          #msg1 = ttk.Label(win, text='Please upload the file', bootstyle=INFO)
          #msg1.place(relx=0.5, rely=0.05, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          
          
          
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER)
          
        elif(sel.get()=='XSS - Fixed'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def xss_fixed_comment():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            require_once "auth_check.php";
            require_once "config.php";
            $name = $_POST['name'];
            $comment = $_POST['comment'];
            $strname = str_ireplace( 'alert', '', $_POST['name'] ); 
            $strcomment = str_ireplace( 'alert', '', $_POST['comment'] );
            $con = mysqli_connect("db", "php_docker", "password", "php_docker");
            $stmt = $con->prepare("INSERT INTO commentsnew (name, comment) VALUES (?, ?)");
            $stmt->bind_param("ss", $strname, $strcomment);
            $stmt->execute();
            $result = $stmt->get_result();
            $stmt->close;
            echo("<script>location.href = 'feedback.html';</script>");
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          
          def xss_fixed_view():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            include "config.php";
            $con = mysqli_connect("db", "php_docker", "password", "php_docker");
            $sql = "SELECT * FROM commentsnew";
            $result = mysqli_query($con, $sql);
            while ($row = $result->fetch_assoc()) {
            	$row['name'] = htmlspecialchars($row['name'],ENT_QUOTES,'UTF-8');
            	$row['comment'] = htmlspecialchars($row['comment'],ENT_QUOTES,'UTF-8');
            	echo "name:"; echo $row['name']."<br>";
                echo "comment:"; echo $row['comment']."<br><br>";
            }
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def xss_fixed_search():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            require_once "config.php";
            if(isset($_GET["id"]))
             {
            $id=$_GET['id'];
            $strname = str_ireplace( 'alert', '', $_GET["id"] );
            $con = mysqli_connect("db", "php_docker", "password", "php_docker");
            $stmt = $con->prepare("SELECT * FROM products WHERE name like ? OR type  like ?");
            $stmt->bind_param("ss", $strname, $strname);
            $stmt->execute();
            $result = $stmt->get_result();
            $stmt->close();
            $row['strname'] = htmlspecialchars($row['strname'],ENT_QUOTES,'UTF-8');
            echo $row['strname']."<br>";
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
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'comment.php':
                    xss_fixed_comment()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)               
            elif choice == 1:
                if file =='view.php':
                    xss_fixed_view()
            elif choice == 2:
                if file =='search.php':
                    xss_fixed_view()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)  
          
          msg1 = ttk.Radiobutton(win, text="comment.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          msg2 = ttk.Radiobutton(win, text="view.php", variable=user_choice, value=1, bootstyle=INFO).place(
              relx=0.75, rely=0.3, anchor=CENTER)
          msg3 = ttk.Radiobutton(win, text="search.php", variable=user_choice, value=2, bootstyle=INFO).place(
              relx=0.75, rely=0.3, anchor=CENTER)
          
          #msg1 = ttk.Label(win, text='Please upload the file', bootstyle=INFO)
          #msg1.place(relx=0.5, rely=0.05, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          
          
          
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER)
    
        elif(sel.get()=='Malicious File Upload - Easy'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def file_low_page2():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            if(!empty($_FILES['myFile']))
            {
              $path = "documents/";
              $path = $path . basename( $_FILES['myFile']['name']);
            
              if(move_uploaded_file($_FILES['myFile']['tmp_name'], $path)) {
                echo "The file ".  basename( $_FILES['myFile']['name']). 
                " has been uploaded";
              } else{
                  echo "There was an error uploading the file, please try again!";
              }
            }
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'page2.php':
                    file_low_page2()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)               
          
          msg1 = ttk.Radiobutton(win, text="page2.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          
          #msg1 = ttk.Label(win, text='Please upload the file', bootstyle=INFO)
          #msg1.place(relx=0.5, rely=0.05, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          
          
          
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER)
          
        elif(sel.get()=='Malicious File Upload - Medium'):
          outmsg = StringVar()
          user_choice = IntVar() 
          outmsg = StringVar()
          user_choice = IntVar() 
          def file_med_page2():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            //require_once "auth_check.php";
            require_once "config.php";
            $file_get = $_FILES['files']['name'];
            $temp = $_FILES['files']['tmp_name'];
            $mimetype = mime_content_type($temp);
            if(in_array($mimetype, array('image/jpeg', 'image/jpg', 'image/gif', 'image/png'))) {
               $file_to_saved = "documents/".$file_get;
               move_uploaded_file($temp, $file_to_saved);
               $insert_img = mysqli_query($db,"INSERT INTO image values ('".$file_to_saved."')");
               echo 'OK';
            
            } else {
                echo 'Upload a real image!';
            }
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'page2.php':
                    file_med_page2()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)    
          
          msg1 = ttk.Radiobutton(win, text="page2.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          
          #msg1 = ttk.Label(win, text='Please upload the file', bootstyle=INFO)
          #msg1.place(relx=0.5, rely=0.05, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          
          
          
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER)
    
        elif(sel.get()=='Malicious File Upload - Hard'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def file_hard_page2():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            //require_once "auth_check.php";
            require_once "config.php";
            if( isset( $_POST[ 'Upload' ] ) ) {
                die("There is no file to upload.");
            }
            
            $filepath = $_FILES['myFile']['tmp_name'];
            $fileinfo = finfo_open(FILEINFO_MIME_TYPE);
            $filetype = finfo_file($fileinfo, $filepath);
            
            $allowedTypes = [
               'image/png' => 'png%00',
               'image/jpeg' => 'jpg%00'
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
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'page2.php':
                    file_hard_page2()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)    
          
          msg1 = ttk.Radiobutton(win, text="page2.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          
          #msg1 = ttk.Label(win, text='Please upload the file', bootstyle=INFO)
          #msg1.place(relx=0.5, rely=0.05, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          
          
          
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER) 
          
        elif(sel.get()=='Malicious File Upload - Fixed'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def file_fixed_page2():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            require_once "auth_check.php";
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
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'page2.php':
                    file_fixed_page2()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)    
          
          msg1 = ttk.Radiobutton(win, text="page2.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          
          #msg1 = ttk.Label(win, text='Please upload the file', bootstyle=INFO)
          #msg1.place(relx=0.5, rely=0.05, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          
          
          
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER)
          
        elif(sel.get()=='RCE - Easy'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def rce_low_include():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            //require_once "auth_check.php";
            require_once "config.php";
            header("X-XSS-Protection: 0");
            $id = $_GET['id'];
            include($id);
            //for rce/command exec
            echo "<font color='black'>".$id."</font>";
            $output = shell_exec($_GET["id"]);
            echo "<pre>$output</pre>";
            
            //code for Local File Inclusion
            //$id = $_GET['id'];
            //include($_GET["id"]);
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'include.php':
                    rce_low_include()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)   
          
          msg1 = ttk.Radiobutton(win, text="include.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER)
          
        elif(sel.get()=='RCE - Medium'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def rce_med_include():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            //require_once "auth_check.php";
            require_once "config.php";
            header("X-XSS-Protection: 0");
            $id = $_GET['id'];
            include($id);
            //for rce/command exec
            echo "<font color='black'>".$id."</font>";
            $output = shell_exec("nslookup " . $_GET["id"]);
            echo "<pre>$output</pre>";
            
            //code for Local File Inclusion
            //$id = $_GET[ 'id' ].".php"; ----- this can be used to read files: php://filter/convert.base64-encode/resource=file
            //include($_GET["id"]);
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'include.php':
                    rce_med_include()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)   
          
          msg1 = ttk.Radiobutton(win, text="include.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER)
    
        elif(sel.get()=='RCE - Hard'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def rce_low_include():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            //require_once "auth_check.php";
            require_once "config.php";
            header("X-XSS-Protection: 0");
            $id = $_GET['id'];
            include($id);
            //for rce/command exec
            $blacklist = array(" ","&","|","@","%",",","/");
            $input = str_replace($blacklist,"", $id);
            $blacklist = array("ls","dir","cat","type","whoami","pwd","echo","ipconfig","ifconfig","nc","netcat");
            $input = str_replace($blacklist,"", $id);
            echo "<font color='black'>".$id."</font>";
            $output = shell_exec("nslookup " . $input);
            echo "<pre>$output</pre>";
            
            //code for Local File Inclusion
            //$id = $_GET[ 'id' ].".php"; ----- this can be used to read files: php://filter/convert.base64-encode/resource=file
            //include($id);
            //if( !fnmatch( "id*", $id ) && $id != "include.php" ) {
            //
            //    echo "ERROR: File not found!";
            //    exit;
            //} 
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'include.php':
                    rce_hard_include()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)   
          
          msg1 = ttk.Radiobutton(win, text="include.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER)
          
        elif(sel.get()=='RCE - Fixed'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def rce_fixed_include():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            //require_once "auth_check.php";
            require_once "config.php";
            header("X-XSS-Protection: 0");
            $id = $_GET['id'];
            include($id);
            //for rce/command exec
            $blacklist = array(" ","&","&&","|","||","@","%",",","/","~","^");
            $input = str_replace($blacklist,"", $id);
            $blacklist = array("ls","dir","cat","type","whoami","pwd","echo","ipconfig","ifconfig","nc","netcat");
            $input = str_replace($blacklist,"", $id);
            $input = htmlspecialchars($input);
            echo "<font color='black'>".$id."</font>";
            $output = shell_exec("nslookup " . $input);
            echo "<b>".htmlspecialchars($output,ENT_QUOTES,'UTF-8');
            
            /*
            $id = $_GET[ 'id' ].".php";
            include($id);
            if( $id != "include.php" && $id != "file1.php" && $id != "file2.php" && $id != "file3.php" ) {
                // this can be used to read files: php://filter/convert.base64-encode/resource=file
                echo "ERROR: File not found!";
                exit;
            } */
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'include.php':
                    rce_fixed_include()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)   
          
          msg1 = ttk.Radiobutton(win, text="include.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER) 
    
        elif(sel.get()=='LFI - Easy'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def lfi_easy_include():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            //require_once "auth_check.php";
            require_once "config.php";
            header("X-XSS-Protection: 0");
            //$id = $_GET['id'];
            //include($id);
            ////for rce/command exec
            //echo "<font color='black'>".$id."</font>";
            //$output = shell_exec($_GET["id"]);
            //echo "<pre>$output</pre>";
            
            //code for Local File Inclusion
            $id = $_GET['id'];
            include($_GET["id"]);
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'include.php':
                    lfi_easy_include()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)   
          
          msg1 = ttk.Radiobutton(win, text="include.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER) 
          
        elif(sel.get()=='LFI - Medium'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def lfi_med_include():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            //require_once "auth_check.php";
            require_once "config.php";
            header("X-XSS-Protection: 0");
            //$id = $_GET['id'];
            //include($id);
            ////for rce/command exec
            //echo "<font color='black'>".$id."</font>";
            //$output = shell_exec("nslookup " . $_GET["id"]);
            //echo "<pre>$output</pre>";
            
            //code for Local File Inclusion
            $id = $_GET[ 'id' ].".php";
            include($_GET["id"]);
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'include.php':
                    lfi_med_include()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)   
          
          msg1 = ttk.Radiobutton(win, text="include.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER) 
    
        elif(sel.get()=='LFI - Hard'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def lfi_hard_include():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            //require_once "auth_check.php";
            require_once "config.php";
            header("X-XSS-Protection: 0");
            //$id = $_GET['id'];
            //include($id);
            ////for rce/command exec
            //$blacklist = array(" ","&","|","@","%",",","/");
            //$input = str_replace($blacklist,"", $id);
            //$blacklist = array("ls","dir","cat","type","whoami","pwd","echo","ipconfig","ifconfig","nc","netcat");
            //$input = str_replace($blacklist,"", $id);
            //echo "<font color='black'>".$id."</font>";
            //$output = shell_exec("nslookup " . $input);
            //echo "<pre>$output</pre>";
            
            //code for Local File Inclusion
            $id = $_GET[ 'id' ].".php";
            include($id);
            if( !fnmatch( "id*", $id ) && $id != "include.php" ) {
                // This isn't the page we want!
                echo "ERROR: File not found!";
                exit;
            }
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'include.php':
                    lfi_hard_include()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)   
          
          msg1 = ttk.Radiobutton(win, text="include.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER) 
          
        elif(sel.get()=='LFI - Fixed'):
          outmsg = StringVar()
          user_choice = IntVar() 
          def lfi_fixed_include():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n]*<!-- start -->.*?<!-- end -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <!-- start -->
            <?php
            //require_once "auth_check.php";
            require_once "config.php";
            header("X-XSS-Protection: 0");
            //$id = $_GET['id'];
            //include($id);
            //$blacklist = array(" ","&","&&","|","||","@","%",",","/","~","^");
            //$input = str_replace($blacklist,"", $id);
            //$blacklist = array("ls","dir","cat","type","whoami","pwd","echo","ipconfig","ifconfig","nc","netcat");
            //$input = str_replace($blacklist,"", $id);
            //$input = htmlspecialchars($input);
            //echo "<font color='black'>".$id."</font>";
            //$output = shell_exec("nslookup " . $input);
            //echo "<b>".htmlspecialchars($output,ENT_QUOTES,'UTF-8');
            
            //code for Local File Inclusion
            $id = $_GET[ 'id' ].".php";
            include($id);
            if( $id != "include.php" && $id != "file1.php" && $id != "file2.php" && $id != "file3.php" ) {
                // This isn't the page we want!
                echo "ERROR: File not found!";
                exit;
            } 
            ?>
            <!-- end -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'include.php':
                    lfi_fixed_include()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)   
          
          msg1 = ttk.Radiobutton(win, text="include.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER) 
          
        elif(sel.get()=='Cookie'): ### check logic for cookies, maybe only 1 cookie user option will be okay
          outmsg = StringVar()
          user_choice = IntVar() 
          def cookie_include():
            global file_path
            msg = ""
            message = msg
            def replace(subs, flags=re.DOTALL):
               with open(file_path, "r+") as file:
                    x = file.read()
                    y = re.findall("[^\n].*<!-- Cookieend -->[^\n]*", x, re.DOTALL)
                    print(y)
                    result = '\n'.join(y)
                    text_pattern = re.compile(re.escape(result), flags)
                    file_contents = text_pattern.sub(subs, x)
                    file.seek(0)
                    file.truncate()
                    file.write(file_contents)
                  
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            #if file_path == 'index.php':
            subs='''
            <?php
            $cookie_name = "{flag}";
            $x = random_int(100, 999);
            $y = md5($x);
            $cookie_value = $y;
            setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
            ?>
            <!-- Cookieend -->'''
              
          replace(subs)
          mssg = "Done"
          outmsg.set(mssg)
          def upload_file():
            global file_path
            file_path = filedialog.askopenfilename()
            print("file is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()     
           
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                if file == 'index.php':
                    cookie_include()
                if file == 'products.php':
                    cookie_include()
                if file == 'comment.php':
                    cookie_include()
                if file == 'view.php':
                    cookie_include()
                if file == 'page2.php':
                    cookie_include()
                if file == 'search.php':
                    cookie_include()
                else:
                   mssg = "Please choose the correct file"
                   outmsg.set(mssg)   
          
          #guiItems.replacing()  ###multiple gui radio buttons to add
          msg1 = ttk.Radiobutton(win, text="index.php", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)
          msg2 = ttk.Radiobutton(win, text="products.php", variable=user_choice, value=1, bootstyle=INFO).place(
              relx=0.75, rely=0.3, anchor=CENTER)
          msg3 = ttk.Radiobutton(win, text="comment.php", variable=user_choice, value=2, bootstyle=INFO).place(
              relx=0.76 , rely=0.4, anchor=CENTER)
          msg4 = ttk.Radiobutton(win, text="view.php", variable=user_choice, value=3, bootstyle=INFO).place(
              relx=0.75 , rely=0.5, anchor=CENTER)
          msg5 = ttk.Radiobutton(win, text="page2.php", variable=user_choice, value=4, bootstyle=INFO).place(
              relx=0.75 , rely=0.6, anchor=CENTER)
          msg6 = ttk.Radiobutton(win, text="search.php", variable=user_choice, value=5, bootstyle=INFO).place(
              relx=0.75 , rely=0.7, anchor=CENTER)
          
          #msg1 = ttk.Label(win, text='Please upload the file', bootstyle=INFO)
          #msg1.place(relx=0.5, rely=0.05, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          
          
          
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER)
    
          
        elif(sel.get()=='Products include/exclude'):  ### check logic for cookies, maybe only 1 cookie user option will be okay
          outmsg = StringVar()
          user_choice = IntVar() 
          Products.replacing()
          
          #guiItems.replacing()  ###multiple gui radio buttons to add
    
          
        elif(sel.get()=='ZIP all the newly created files?'):  #write logic and gui items for this
          outmsg = StringVar()
          user_choice = IntVar() 
          def zipFile():
            global file_path
            msg = ""
            #msg = fob
            message = msg
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
            shutil.make_archive('webapps', format='zip', root_dir=file_path)
            mssg = "File zipped successfully! Please check your current working directory"
            outmsg.set(mssg)
          
          def upload_file():
            global file_path
            file_path = filedialog.askdirectory()
            print("folder is: ", file_path)
            if file:
               pass            
            else:
                print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()      
            file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                zipFile()
            else:
               mssg = "Error!"
               outmsg.set(mssg)
          
          #guiItems.replacing()  ###multiple gui radio buttons to add
          msg1 = ttk.Radiobutton(win, text="ZIP the folder?", variable=user_choice, value=0, bootstyle=INFO).place(
              relx=0.75, rely=0.2, anchor=CENTER)      
          #msg1 = ttk.Label(win, text='Please upload the file', bootstyle=INFO)
          #msg1.place(relx=0.5, rely=0.05, anchor=CENTER)
          b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          
          
          
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          
          convert = ttk.Button(win, text='Convert', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER)

        elif(sel.get()=='Create Docker File'):  #write logic and gui items for this
          outmsg = StringVar()
          user_choice = IntVar() 
          def deploydocker():
            global file_path
            msg = ""
            #msg = fob
            message = msg
            #file_path=input("Please enter the filepath: ")
            #file=os.path.basename(file)
            #print(os.path.splitext(file_path)[0])
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
                result.stdout
            mssg = "Please share the .exe file in 'dist' folder with the students."
            outmsg.set(mssg)
          
          #def upload_file():
          #  global file_path
          #  file_path = filedialog.askdirectory()
          #  print("folder is: ", file_path)
          #  if file:
          #     pass            
          #  else:
          #      print("No file selected") 
          def con():
            global file_path
            choice = user_choice.get()      
            #file=os.path.basename(file_path)
            if choice == 0:
                #file=os.path.basename(file_path)
                #print(file)
                deploydocker()
            else:
               mssg = "Error!"
               outmsg.set(mssg)
          
          #guiItems.replacing()  ###multiple gui radio buttons to add
          #msg1 = ttk.Radiobutton(win, text="Deploy?", variable=user_choice, value=0, bootstyle=INFO).place(
          #    relx=0.75, rely=0.2, anchor=CENTER)      
          #msg1 = ttk.Label(win, text='Please upload the file', bootstyle=INFO)
          #msg1.place(relx=0.5, rely=0.05, anchor=CENTER)
          #b1 = ttk.Button(win, text='Please upload the file', width=20,command = lambda:upload_file())
          #b1.place(relx=0.5,rely=0.06, anchor=CENTER) 
          msg4 = ttk.Label(win, text='Status: ', bootstyle=PRIMARY)
          msg4.place(relx=0.5, rely=0.65, anchor=CENTER)
          #user_input_text = Entry(win)
          #user_input_text.place(relx=0.5, rely=0.15, anchor=CENTER, width=500, height=50)
          #user_input_text.focus_set()
          stop = ttk.Button(win, text='Exit', width=10, command=win.destroy, bootstyle="DANGER-OUTLINE")
          stop.place(relx=0.10, rely=1, anchor=SE)
          out = Entry(win, text=outmsg).place(
              relx=0.5, rely=0.75, anchor=CENTER,  width=500, height=50)
          convert = ttk.Button(win, text='Deploy', width=20, command=con, bootstyle="WARNING-OUTLINE")
          convert.place(relx=0.5, rely=0.4, anchor=CENTER)
    sel.trace('w',my_upd) # on change of string variable 
    win.config(menu=menubar)
    win.mainloop()  # Keep the window open
win()
    #return win
