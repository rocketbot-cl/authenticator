



# authenticator
  
Obtener codigo de Factor de Doble autenticación del tipo TOPT (Time-based One Time Password) como Google y Microsoft Authenticator  

*Read this in other languages: [English](Manual_authenticator.md), [Português](Manual_authenticator.pr.md), [Español](Manual_authenticator.es.md)*
  
![banner](imgs/banner_authenticator.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Get code
  
Get the authentication code.
|Parameters|Description|example|
| --- | --- | --- |
|Secret|Enter the password.|secret32|
|Number of digits (Optional)|Number of digits that the returned code will have.|6|
|Interval|Number of digits that the returned code will have.|30|
|Assign result to variable|Assign connection result to variable.|result|
