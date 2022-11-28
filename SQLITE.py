import sqlite3

#crear tabla SQLITE
def create_table_sqlite():
    with sqlite3.connect("CLASE_sqlite/bd_btf.db") as conexion:
        try:
            sentencia = ''' create  table puntajes
                            (
                                    id integer primary key autoincrement,
                                    nombre text,
                                    puntaje real
                            )
                        '''
            conexion.execute(sentencia)
            print("Se creo la tabla puntajes")                       
        except sqlite3.OperationalError:
            print("La tabla puntajes ya existe")

#insertar filas
def add_rows_sqlite(nombre,puntaje):
    with sqlite3.connect("CLASE_sqlite/bd_btf.db") as conexion:
        try:
            conexion.execute("insert into puntajes(nombre,puntaje) values (?,?)", ("{0}".format(nombre),"{0}".format(puntaje)))
            conexion.commit()# Actualiza los datos realmente en la tabla
        except:
            print("Error")
 

#recuperar filas
def view_rows_sqlite():
    with sqlite3.connect("CLASE_sqlite/bd_btf.db") as conexion:
        cursor=conexion.execute("SELECT * FROM puntajes")
        for fila in cursor:
            print(fila)







