"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")
Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json
Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")
Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)
Para obtener la Opcion seleccionada:
    opcion = GetParams("option")
Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    pip install <package> -t .
"""
import os
import sys
import traceback

GetParams = GetParams #pylint: disable=undefined-variable,self-assigning-variable
SetVar = SetVar #pylint: disable=undefined-variable,self-assigning-variable
PrintException = PrintException #pylint: disable=undefined-variable,self-assigning-variable

# Add the libs folder to the system path
base_path = tmp_global_obj["basepath"]
cur_path = os.path.join(base_path, 'modules', 'authenticator', 'libs')

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)

if sys.maxsize > 2**32 and cur_path_x64 not in sys.path:
        sys.path.append(cur_path_x64)
elif sys.maxsize <= 2**32 and cur_path_x86 not in sys.path:
        sys.path.append(cur_path_x86)

import pyotp

module = GetParams("module")

if module == "get_code":
    key = GetParams("secret")
    digits = GetParams("digits")
    interval = GetParams("interval")
    result = GetParams("result")
    
    if not digits:
        digits = 6
    else:
        digits = int(digits)
    if not interval:
        interval = 30
    else:
        interval = int(interval)
    
    try:
        # otpauth://totp/20200033:rpa?secret=JI3GQTDUNV3XGOCDKBLHMMBWOYYWW6L2&digits=6&algorithm=SHA1&issuer=20200033&period=30
        
        
        #totp = pyotp.TOTP(s="JI3GQTDUNV3XGOCDKBLHMMBWOYYWW6L2", digits = 6, interval=interval, issuer="20200033", name="rpa", digest="sha1")
        
        totp = pyotp.TOTP(key, digits = digits, interval=interval)
        code = totp.now()
        SetVar(result, code)
    except Exception as e:
        traceback.print_exc()
        SetVar(result, False)
        raise e
    
if module == "get_code_QR":
    path = GetParams("path")
    result = GetParams("result")
    
    def read_qr_code(filename):
        import cv2

        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        
        return value
    
    try:
        data = read_qr_code(path)
        if data:
            totp = pyotp.parse_uri(data)
            
            code = totp.now()
            SetVar(result, code)   
        else:
            SetVar(result, "QR code cannot be read")   
  
    except Exception as e:
        traceback.print_exc()
        SetVar(result, False)
        raise e