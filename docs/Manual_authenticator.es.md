



# authenticator
  
Obtain Double Factor Authentication code of type TOPT (Time-based One Time Password) like Google and Microsoft Authenticator  

*Read this in other languages: [English](Manual_authenticator.md), [Português](Manual_authenticator.pr.md), [Español](Manual_authenticator.es.md)*
  
![banner](imgs/banner_authenticator.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Obtener codigo
  
Obtén el codigo de autenticación.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Secret|Ingrese la contraseña.|secret32|
|Cantidad de digitos (Opcional)|Cantidad de dígitos que tendrá el código retornado.|6|
|Intervalo|Cantidad de dígitos que tendrá el código retornado.|30|
|Asignar resultado a variable|Asignar resultado de la conexión a variable.|result|
