from googleapiclient.discovery import build
from google.oauth2 import service_account
"""
Archivo que almacena la funcion upload_to_sheets, que carga los datos
recogidos por la interfaz grafica, y los almacena en una hoja de calculo de google

"""
def upload_to_sheets(nombre, apellido, cedula, canton, tipo_colegio, correo, telefono, jornada, modalidad, carrera1, carrera2, carrera3, fecha_nacimiento,proceso):

    SCOPES=['https://www.googleapis.com/auth/spreadsheets']#direccion por defecto de la api de las hojas de calculo
    try:
        KEY='./key.json'#llave de la api creada en los proyectos de google cloud
<<<<<<< HEAD
        SPREADSHEET_ID='id de la hoja de calculo'#id de la hoja de calculo
=======
        SPREADSHEET_ID='**********************'#id de la hoja de calculo
>>>>>>> 17f274b31b6616273b4403bb07c704e7e6ec3d9d
        creds=None#inicializa la variable
        creds=service_account.Credentials.from_service_account_file(KEY,scopes=SCOPES)#se indica que el 
        #servicio se va a ejecutar con las credenciales en la direccion de la api
        service=build('sheets','v4',credentials=creds)#se esocge la version de la api con las credenciales
        sheet=service.spreadsheets()#se llama la funcion para escribir datos en sheets
        values=[[nombre,apellido,cedula,canton,
                 tipo_colegio,correo,telefono,
                 jornada,modalidad,carrera1,
                 carrera2,carrera3,fecha_nacimiento,proceso]]#valores a ingresar
        result=sheet.values().append(spreadsheetId=SPREADSHEET_ID,range='A1',
                                    valueInputOption='USER_ENTERED',
                                    body={'values':values}).execute()
        #se cargan los valores a la hoja de calculo, se coloca A1 pues indica el orden de las filas
        #como se iran llenando automaticamente
    except Exception as e:
        print(f"Ha ocurrido un error al momento de ejecutar este programa {e}")
        
        
<<<<<<< HEAD
=======
#upload_to_sheets('Samantha','Bueno',"0103229001",'Cuenca','Fiscal','samybueno499@gmail.com','4088091','matutina','presencial','desarrollo','big data','mecatronica','26/05/2007')
>>>>>>> 17f274b31b6616273b4403bb07c704e7e6ec3d9d
