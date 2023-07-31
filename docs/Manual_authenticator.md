



# authenticator
  
Obtener codigo de Factor de Doble autenticación del tipo TOPT (Time-based One Time Password) como Google y Microsoft Authenticator  

*Read this in other languages: [English](Manual_authenticator.md), [Português](Manual_authenticator.pr.md), [Español](Manual_authenticator.es.md)*
  
![banner](imgs/Banner_authenticator.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module

The module has 2 options to obtain the authentication code:
1. Get code from Secret
2. Get code from QR
Some applications explicitly grant the secret or allow the user to define it and in other cases it only provides a QR code which, when read, registers the application in the Authenticator. To test both options you can use your google account that provides both QR and Secret:
   1. Enter "Manage your Google account"
   2. Enter the "Security" section
   3. Select "2-Step Verification" in the "How do you sign in to Google" box
   4. Select "Authenticator App"
   5. Click on "+ Configure Authenticator"
   6. The image of a QR code will appear, right click and save the image.
   7. To get the generated Secret click "Can't you scan it?" and copy the code indicated there.


## Description of the commands

### Get code
  
Get the authentication code.
|Parameters|Description|example|
| --- | --- | --- |
|Secret|Enter the password.|secret32|
|Number of digits (Optional)|Number of digits that the returned code will have.|6|
|Interval|Number of digits that the returned code will have.|30|
|Assign result to variable|Assign connection result to variable.|result|

### Get code from QR
  
Read a QR code from a PNG file and get the authentication code.
|Parameters|Description|example|
| --- | --- | --- |
|QR image path|Path to PNG file with QR code.|C:\Users\user\Documents\QR_image.png|
|Assign result to variable|Assign connection result to variable.|result|
