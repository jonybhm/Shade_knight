import sqlite3

#crear tabla SQLITE
def create_table_sqlite()->None:
    '''
    Creates a table on sqlite with an id, name and score
    Arguments: None
    Returns: None
    '''
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
def add_rows_sqlite(nombre:str,puntaje:int)->None:
    '''
    Adds info in the table, name and score
    Arguments: nombre (str), puntaje (str) representing the name and score for each run
    Returns: None
    '''
    with sqlite3.connect("rankings_game.db") as conexion:
        try:
            conexion.execute("insert into rankings(nombre,puntaje) values (?,?)",
            (nombre,puntaje))
            conexion.commit()# Actualiza los datos realmente en la tabla
        except:
            print("Error")
 

#recuperar filas
def view_rows_sqlite()->list:
    '''
    Orders and obtains a top 10 score from database and returns a list with those values 
    Arguments: None
    Returns: list
    '''
    with sqlite3.connect("rankings_game.db") as conexion:
        cursor=conexion.execute('''SELECT id, nombre, puntaje
                                FROM rankings
                                ORDER BY puntaje DESC
                                LIMIT 10
                                ''')
        lista_top_10 = []
        for fila in cursor:
            lista_top_10.append(fila)
        return lista_top_10
        







