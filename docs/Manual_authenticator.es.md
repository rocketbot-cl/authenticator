



# authenticator
  
Obtain Double Factor Authentication code of type TOPT (Time-based One Time Password) like Google and Microsoft Authenticator  

*Read this in other languages: [English](Manual_authenticator.md), [Português](Manual_authenticator.pr.md), [Español](Manual_authenticator.es.md)*
  
![banner](imgs/Banner_authenticator.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## Como usar este modulo

El modulo cuenta con 2 opciones para obtener el código de autenticación:
1. Obtener código desde Secreto
2. Obtener código desde QR
Algunas aplicaciones otorgar explícitamente el secreto o permiten al usuario la definición del mismo y en otros casos solo brinda un código QR el cual al leerlo registra la aplicación en el Autenticador. Para probar ambas opciones puede utilizar su cuenta de google que brinda tanto QR como Secreto:
   1. Ingresar a "Gestionar tu cuenta de Google"
   2. Ingresar a la sección "Seguridad"
   3. Seleccionar "Verificación en dos pasos" dentro del recuadro "Cómo inicias sesión en Google"
   4. Seleccionar "Aplicación Authenticator"
   5. Clickear en "+ Configurar Autenticador"
   6. Aparecera la imagen de un código QR, realizar click derecho y guarda la imagen.
   7. Para obtener el Secreto generado clickear "¿No puedes escanearlo?" y copiar el código que allí se indica.



## Descripción de los comandos

### Obtener codigo
  
Obtén el codigo de autenticación.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Secret|Ingrese la contraseña.|secret32|
|Cantidad de digitos (Opcional)|Cantidad de dígitos que tendrá el código retornado.|6|
|Intervalo|Cantidad de dígitos que tendrá el código retornado.|30|
|Asignar resultado a variable|Asignar resultado de la conexión a variable.|result|

### Obtener código desde QR
  
Lee un código QR a partir de un archivo PNG y obtén el codigo de autenticación.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta de la imagen QR|Ruta a archivo PNG con código QR.|C:\Users\user\Documents\QR_image.png|
|Asignar resultado a variable|Asignar resultado de la conexión a variable.|result|
