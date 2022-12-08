import sqlite3

#crear tabla SQLITE
def create_table_sqlite():
    with sqlite3.connect("rankings_game.db") as conexion:
        try:
            conexion.execute(''' create  table rankings
                            (
                                    id integer primary key autoincrement,
                                    nombre text,
                                    puntaje integer
                            )
                        ''')
            print("Se creo la tabla rankings")                       
        except sqlite3.OperationalError:
            print("La tabla rankings ya existe")

#insertar filas
def add_rows_sqlite(nombre,puntaje):
    with sqlite3.connect("rankings_game.db") as conexion:
        try:
            conexion.execute("insert into rankings(nombre,puntaje) values (?,?)",
            (nombre,puntaje))
            conexion.commit()# Actualiza los datos realmente en la tabla
        except:
            print("Error")
 

#recuperar filas
def view_rows_sqlite():
    with sqlite3.connect("rankings_game.db") as conexion:
        cursor=conexion.execute('''SELECT id, nombre, puntaje
                                FROM rankings
                                ORDER BY puntaje DESC
                                LIMIT 10
                                ''')
        lista = []
        for fila in cursor:
            print(fila)
            lista.append(fila)
        return lista
        







