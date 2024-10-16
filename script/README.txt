Step 1: Modifying the application files:
----------------------------------------------------------------------------------------------------------------------------------------
A. SQL Injection: A tester can be use Union-Based SQLi to retrive information from the DB.

Reference: https://portswigger.net/web-security/sql-injection/union-attacks

Code can be used in any of the following files:

- login.php
- products.php


----------------------------------------------------------------------------------------------------------------------------------------
B. XSS: A tester can use malicious javascript payloads so the browser will execute arbitrary javascript.

Reference: https://portswigger.net/web-security/cross-site-scripting

Code can be used in any of the following files:

- search.php
- comment.php
- view.php

----------------------------------------------------------------------------------------------------------------------------------------
C. File Upload: A tester can upload malicious files leading to command execution, defacement, etc.

Reference: https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload

Code can be used in any of the following files:
- upload.php

----------------------------------------------------------------------------------------------------------------------------------------
D. RCE: Remote commands can be executed by the tester if the webapp is vulnerable to RCE.
   LFI: The tester can include and read sensitive local files present in the web sever.

Reference: RCE: https://www.bugcrowd.com/glossary/remote-code-execution-rce/
           LFI: https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion

Code can be used in any of the following files:

- include.php

----------------------------------------------------------------------------------------------------------------------------------------
E. Cookies containing the Flag can be set on any of the files listed in the above lines.

- By default: All the important PHP files have cookies in them.
   
----------------------------------------------------------------------------------------------------------------------------------------
F. Cars, Bikes, Planes, Laptops, Headphones products are available to include/exclude in the application.

- By default: All the products are included in the current version of the webapp.

----------------------------------------------------------------------------------------------------------------------------------------
G. CSS style can be modified for any of the following files:

- index.php, home.html, comment.php, view.php, products.html, products.php, search.php, search.html, include.php, signup.php, feedback.html, upload.html

CSS options (all the three CSS variations have different background, header, text color):

- style.css
- style1.css
- style2.css

----------------------------------------------------------------------------------------------------------------------------------------
Step 2: Creating the ZIP file (for backup - optional):

- You can zip the app folder by choosing ZIPtheFiles option from the Menu

----------------------------------------------------------------------------------------------------------------------------------------
Step 3: Create a deployable file with Docker:

- You can create the deployable .exe file by choosing DeployDockerfile option from the Menu
- To deploy the file with Logging capabilities, please choose DeployDockerfile_WithLogs option. This option will send the logs to your chosen S3 bucket.
  Note: Don't forget to replace your AWS Access Key, Secret Access Key & bucket name in the file DeployDockerfile_WithLogs.py.