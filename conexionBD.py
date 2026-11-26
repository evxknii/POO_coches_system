import mysql.connector
from tkinter import messagebox
try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_coches"
    )

    cursor = conexion.cursor(buffered=True)
except:
    messagebox.showerror(title="... Error de conexion ...",message=f"... Por el momento no es posible conctarse con la base de datos. Intentelo más tarde ...")

