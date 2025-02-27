from tkinter import  Button, Canvas, Entry, Label, Radiobutton, StringVar, Tk, messagebox, ttk, NW,IntVar,Checkbutton
from tkcalendar import DateEntry
#import sqlite3

from datetime import datetime
from subir_datos_sheets import *
from validar_datos import verificar_cedula
from PIL import Image,ImageTk
from data_base import insertar_datos

def iniciar_gui():
    
    
    root = Tk()
    root.title("Registro de usuarios")
    root.geometry("800x650")
    #rgb_color=(188,188,188)
    
    canvas=Canvas(root,width=800,height=650)
    image=ImageTk.PhotoImage(Image.open("./logo5.png"))
    canvas.create_image(0,0,anchor=NW,image=image)
    canvas.pack()
    
    ###############Definir variables para almacenar los datos ingresados###############
    
    #definir variable para la cedula
    cedula_var = StringVar()
    proceso_var=StringVar()
    proceso_var.set(" ")
    #definir fecha de nacimiento
    fecha_nac_var = StringVar()
    
    #definir variables para los nombres y apellidos
    nombre_var = StringVar()
    apellido_var = StringVar()
    
    #definir variables para los combobox acerca del canton
    canton_var = StringVar()
    canton_var.set("Seleccione un canton")
    """
    opciones_parroquia=["El Vecino","San Sebastian","Yanuncay","Totoracocha","San Blas",
                        "Sucre","Monay","El Batan","Baños","Huaynacapac","Sagrario","Bellavista",
                        "Valle","Hermano Miguel","Ramirez Davalos","Cañaribamba","Ricaurte",
                        "San Joaquin","Sinincay","Turi","Nabon","Sidcay","Sayausi","jasdkas"]
    """
    
    
    opciones_canton = ["Camilo Ponce Enríquez","Chordeleg","Cuenca","El Pan",
                       "Girón","Guachapala","Gualaceo","Nabón","Oña","Paute",
                       "Pucará","San Fernando","Santa Isabel","Sevilla de Oro","Sígsig"]
    
    #definir el tipo de colegio del que proviene el estudiante
    tipo_colegio_var = StringVar()
    tipo_colegio_var.set("Su colegio es: ")
    
    #definir el correo del estudiante
    correo_var = StringVar()
    
    #definir el telefono del estudiante
    telefono_var = StringVar()
    
    #definir tipo de jornada preferida
    jornada_var = StringVar()
    jornada_var.set("Seleccione una jornada")
    
    #defirnir el tipo de modalidad
    modalidad_var = StringVar()
    modalidad_var.set("Seleccione una modalidad")
    
    #definir oferta academica
    carrera1_var = StringVar()
    carrera1_var.set("primera opcion")
    carrera2_var = StringVar()
    carrera2_var.set("segunda opcion")
    carrera3_var = StringVar()
    carrera3_var.set("tercera opcion")
    #opciones de carreras del Tec Azuay
    opciones_carreras=["Big Data","Tributacion","Ciberseguridad","Desarrollo de Software",
                       "Produccion Audiovisual","Seguridad y prevencion de riesgos laborales",
                       "Gestion del patrimonio historico cultural",
                       "Metalmecanica","Mantenimiento electrico y control industrial","Mecatronica",
                       "Administracion de estructuras y plataformas tecnologicas","Entrenamiento deportivo","Desarrollo infanti integral"]
    
    
    
    ##########condicion en caso de que el estudiante no sepa la cedula
    ######## se usara un checkbox para habilitar o deshabilitar la cedula
   
    #Etiqueta y campo para los nombres del estudiante, crear widgets en el canvas
    Label(root, text="Nombre:",bg="white").place(x=50,y=50)
    Entry(root, textvariable=nombre_var).place(x=150,y=50)
    
    #Etiqueta y campo para los apellidos
    Label(root, text="Apellido:").place(x=50,y=100)
    Entry(root, textvariable=apellido_var).place(x=150,y=100)
    
    #Label(root,text="Recuerda su cedula?").place(x=350,y=133)
    #Checkbutton(root,text="Si",variable=conoce_cedula_var,onvalue=1,offvalue=0).place(x=350,y=150)
    #Checkbutton(root,text="No",variable=conoce_cedula_var,value=0).place(x=382,y=150)
    
    Label(root, text="Cedula:").place(x=50,y=150)
    Entry(root,textvariable=cedula_var).place(x=150,y=150)
    #cedula_entry=Entry(root,textvariable=cedula_var,state="enabled")
    #cedula_entry.place(x=150,y=150)
    #conoce_cedula_var.trace_add("write",actualizar_estado_cedula)
        
    #Entry(root, textvariable=cedula_var,state=estado).place(x=150,y=150)
    #Etiqueta y campo para la cedula
   
    #Etiqueta y campo para el canton
    Label(root, text="Canton:").place(x=50, y=200)
    ttk.Combobox(root,values=opciones_canton,textvariable=canton_var).place(x=150,y=200)
    
    #eti y campo para el tipo de colegio
    Label(root, text="Tipo de Colegio:").place(x=50, y=250)
    Radiobutton(root,text="Fiscal",variable=tipo_colegio_var,value="Fiscal").place(x=150,y=250)
    Radiobutton(root,text="Fiscomisional",variable=tipo_colegio_var,value="Fiscomisional").place(x=250,y=250)
    Radiobutton(root,text="Particular",variable=tipo_colegio_var,value="Particular").place(x=350,y=250)
    
    #ingresar fecha de nacimiento
    Label(root, text="Fecha de Nacimiento:").place(x=50, y=300)	
    DateEntry(root, textvariable=fecha_nac_var, width=12, bg="darkblue", fg="white", year=2007).place(x=200, y=300)
    
    #etiqueta y campo para el correo
    Label(root, text="Correo:").place(x=50, y=350)
    Entry(root, textvariable=correo_var).place(x=150, y=350)
    
    Label(root, text="Telefono:").place(x=50, y=400)
    Entry(root, textvariable=telefono_var).place(x=150, y=400)
    
    #etiqueta para el tipo de jornada
    Label(root, text="Jornada:").place(x=50, y=450)
    #select=ttk.Combobox(root,values=["Matutina","Vespertina","Nocturna"],textvariable=jornada_var).grid(row=7, column=1, padx=10, pady=5)
    Radiobutton(root,text="Matutina",variable=jornada_var,value="Matutina").place(x=150,y=450)
    Radiobutton(root,text="Vespertina",variable=jornada_var,value="Vespertina").place(x=250,y=450)
    Radiobutton(root,text="Nocturna",variable=jornada_var,value="Nocturna").place(x=350,y=450)
    
    #etiqueta para la modalidad
    Label(root, text="Modalidad:").place(x=50, y=500)
    Radiobutton(root,text="Presencial",variable=modalidad_var,value="Presencial").place(x=150,y=500)
    Radiobutton(root,text="Dual",variable=modalidad_var,value="Virtual").place(x=250,y=500)
    Radiobutton(root,text="Hibrida",variable=modalidad_var,value="Semi-Presencial").place(x=350,y=500)
    #etiqueta para saber si se conoce el proceso de admision
    Label(root,text="Conoce el proceso de postulacion al TecAzuay?").place(x=500,y=450)
    Radiobutton(root,text="Si",variable=proceso_var,value="Si").place(x=500,y=500)
    Radiobutton(root,text="No",variable=proceso_var,value="No").place(x=550,y=500)
    #etiqueta para las carreras
    Label(root, text="Carreras:").place(x=50, y=550)
    #escoge las 3 carreras que mas le interesan
    ttk.Combobox(root,values=opciones_carreras,textvariable=carrera1_var, width=30).place(x=150,y=575)
    ttk.Combobox(root,values=opciones_carreras,textvariable=carrera2_var,width=30).place(x=350,y=575)
    ttk.Combobox(root,values=opciones_carreras,textvariable=carrera3_var,width=30).place(x=550,y=575)
    
    #botones para guardar y cancelar
    Button(root, text="Guardar", command=lambda: guardar_datos(nombre_var.get(),apellido_var.get(),cedula_var.get(),
                                                               canton_var.get(),
                                                               tipo_colegio_var.get(),
                                                               correo_var.get(),
                                                               telefono_var.get(),
                                                               jornada_var.get(),
                                                               modalidad_var.get(),
                                                               carrera1_var.get(),
                                                               carrera2_var.get(),
                                                               carrera3_var.get(),
                                                               fecha_nac_var.get(),
                                                               proceso_var.get())).place(x=50, y=600)
    Button(root, text="Cancelar",command=lambda:cancelar(nombre_var,cedula_var,apellido_var,canton_var,tipo_colegio_var,correo_var,telefono_var,jornada_var
                                                         ,modalidad_var,carrera1_var,
                                                         carrera2_var,
                                                         carrera3_var,fecha_nac_var)).place(x=150, y=600)
    
    Button(root,text="Limpiar",command=lambda:limpiar(nombre_var,cedula_var,apellido_var,canton_var
                                                      ,tipo_colegio_var,correo_var,telefono_var,
                                                          jornada_var
                                                         ,modalidad_var,carrera1_var,
                                                         carrera2_var,carrera3_var,fecha_nac_var)).place(x=250,y=600)
    root.mainloop()

def guardar_datos(nombre, apellido, cedula, canton, tipo_colegio, correo, telefono, jornada, modalidad, carrera1, carrera2, carrera3, fecha_nacimiento,proceso):
    datos = [nombre, apellido, canton, tipo_colegio, jornada, modalidad, carrera1, carrera2, carrera3, fecha_nacimiento,proceso]
    carreras=[carrera1,carrera2,carrera3]
    
    if all(datos):
        if verificar_cedula(cedula)==True:
            if len(carreras)==len(set(carreras)):
                try:
                    insertar_datos(cedula,nombre,apellido, canton, tipo_colegio, correo, telefono, jornada, modalidad, carrera1, carrera2, carrera3, fecha_nacimiento,proceso)
                    upload_to_sheets(nombre, apellido, cedula, canton, tipo_colegio, correo, telefono, jornada, modalidad, carrera1, carrera2, carrera3, fecha_nacimiento,proceso)
                    messagebox.showinfo("Registro de usuarios","Registro exitoso")
                except Exception as e:
                    print(f"Ha ocurrido un error al ingresar los datos {e}")
                    
            else:
                messagebox.showerror("Registro de usuarios","Seleccione carreras diferentes")
            
              
        else:
            messagebox.showerror("Registro de usuarios","Cedula no valida")
    else:
        messagebox.showerror("Registro de usuarios","Los campos no pueden estar vacios")
    
    

def cancelar(nombre_var, cedula_var, apellido_var, canton_var, tipo_colegio_var, correo_var, telefono_var, jornada_var, modalidad_var, carrera1_var, carrera2_var, carrera3_var, fecha_nac_var):
    nombre_var.set("")
    apellido_var.set("")
    cedula_var.set("")
    canton_var.set("Seleccione un canton")
    tipo_colegio_var.set("Su colegio es: ")
    correo_var.set("")
    telefono_var.set("")
    jornada_var.set("Seleccione una jornada")
    modalidad_var.set("Seleccione una modalidad")
    carrera1_var.set("primera opcion")
    carrera2_var.set("segunda opcion")
    carrera3_var.set("tercera opcion")
    fecha_nac_var.set("")
    messagebox.showinfo("Registro de usuarios", "Registro cancelado")

def limpiar(nombre_var, cedula_var, apellido_var, canton_var, tipo_colegio_var, correo_var, telefono_var, jornada_var, modalidad_var, carrera1_var, carrera2_var, carrera3_var, fecha_nac_var):
    nombre_var.set("")
    apellido_var.set("")
    cedula_var.set("")
    canton_var.set("Seleccione un canton")
    tipo_colegio_var.set("Su colegio es: ")
    correo_var.set("")
    telefono_var.set("")
    jornada_var.set("Seleccione una jornada")
    modalidad_var.set("Seleccione una modalidad")
    carrera1_var.set("primera opcion")
    carrera2_var.set("segunda opcion")
    carrera3_var.set("tercera opcion")
    #fecha_actual=datetime.now()
    fecha_nac_var.set('22/05/2007')
    
