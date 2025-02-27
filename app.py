from gui import iniciar_gui
from data_base import crear_tabla_postgres

if __name__ == "__main__":
    # Crear la tabla si no existe
    crear_tabla_postgres()
    # Iniciar la interfaz gráfica
    iniciar_gui()
   