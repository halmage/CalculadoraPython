import sqlite3


class CalculadoraTable:
    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla 'operaciones' con los campos id, num1, num2, operacion y resultado
        conexion = sqlite3.connect("database/calculadora.db")
        try:
            conexion.execute(
                """
                create table operaciones (
                                    id integer primary key autoincrement,
                                    num1 integer, 
                                    num2 integer,
                                    operacion text,
                                    resultado integer
                                )"""
            )
            print("se creo la base de datos calculadora")
        except sqlite3.OperationalError:
            print("La base de datos calculadora ya existe")
        conexion.close()

    def create(self, resultado):
        # Insertar un nuevo resultado en la tabla 'operaciones'
        conexion = sqlite3.connect("database/calculadora.db")
        conexion.execute(
            "insert into operaciones(num1,num2,operacion,resultado) values (?,?,?,?)",
            (
                resultado["num1"],
                resultado["num2"],
                resultado["operacion"],
                resultado["resultado"],
            ),
        )
        conexion.commit()

    def all(self):
        # Obtener todos los resultados almacenados en la tabla 'operaciones'
        conexion = sqlite3.connect("database/calculadora.db")
        res = conexion.execute("SELECT * FROM operaciones")
        return res.fetchall()
        conexion.close()
