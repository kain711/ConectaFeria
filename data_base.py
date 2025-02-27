# Crear la tabla en la base de datos
import psycopg2
from psycopg2 import OperationalError
def insertar_datos(cedula,nombre, apellido, 
                   canton, tipo_colegio, correo, 
                   telefono, jornada, 
                   modalidad, carrera1, carrera2,
                   carrera3, fecha_nac, proceso):
    """
    Funcion para insertar datos en la base de datos
    parametros:
        cedula,nombre,apellido,modalidad,carrera1,carrera2,carrera3,fecha_nac,proceso
    return:
        Inserta los datos en la tabla datos_usuarios dentro de la base de datos Usuarios en PostgreSQL
    """
    try:
        """
        Conexion a la base de datos, es necesrio instalar la extension SQLTools para poder 
        acceder de forma facil a la base 
        """
        conexion = psycopg2.connect(
            dbname="usuarios",
            user='soporte',
            password='******',
            host='************************************',
            port="**********"
        )
        cursor = conexion.cursor()
        # Insertar datos
        cursor.execute("""
            INSERT INTO datos_usuarios (cedula, nombre, 
            apellido, canton, tipo_colegio, correo, telefono, 
            jornada, modalidad, carrera1, carrera2, carrera3, fecha_nac, proceso)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (cedula,nombre, apellido, canton, tipo_colegio,
              correo, telefono, jornada, modalidad, carrera1, 
              carrera2, carrera3, fecha_nac, proceso))
        conexion.commit()
        cursor.close()
        conexion.close()
    except psycopg2.DatabaseError as e:
        print(f"Ha ocurrido un error con la base de datos {e}")
    except psycopg2.OperationalError as e:
        print(f"Ha ocurrido un error {e}")
        

def crear_tabla_postgres():
    """
    Funcion para crear la tabla en la base de datos
    parametros:
        None    
    return:
        Crea la tabla datos_usuarios dentro de la base de datos Usuarios en PostgreSQL
    """
    db_name='usuarios'
    db_user='soporte'
    db_password='*********'
    db_host='**********'
    db_port='*********'
    
    create_table_query="""
        CREATE TABLE IF NOT EXISTS datos_usuarios(    
        id SERIAL PRIMARY KEY,
        cedula VARCHAR(100) UNIQUE,
        nombre VARCHAR(50),
        apellido VARCHAR(50),
        canton VARCHAR(50),
        tipo_colegio VARCHAR(50),
        correo VARCHAR(50), 
        telefono VARCHAR(15),
        jornada VARCHAR(25), 
        modalidad VARCHAR(25), 
        carrera1 VARCHAR(50), 
        carrera2 VARCHAR(50), 
        carrera3 VARCHAR(50),
        fecha_nac DATE, 
        proceso VARCHAR(5)
        );
        """
    try:
        conexion=psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor=conexion.cursor()
        cursor.execute(create_table_query)
        conexion.commit()
        print("Tabla creada correctamente ")
    except OperationalError as e:
        print(f"Error de ejecucion {e}")
    finally:
        if conexion:
            cursor.close()
            conexion.close()
            print("Conexion cerrada")
            
