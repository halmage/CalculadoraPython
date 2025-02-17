# Librerias del sistema
from database.CalculadoraTable import CalculadoraTable
from package.Operaciones import Operaciones
from package.Otros import Otros


# Librerias externa
from os import system
import time


class Calculadora:
    """
    Calculadora
    """

    def ingresoDeDatos(self):
        # Ingreso de datos
        self.num1 = input("Ingrese primer numero:")
        while self.num1.isdigit() == False:
            # VERIFICANDO LA VARIABLE num1
            print("ERROR: la variable num1 tiene que ser numerico")
            self.num1 = input("Ingrese primer numero: ")
        self.num2 = input("Ingrese segudo numero numero:")
        while self.num2.isdigit() == False:
            # VERIFICANDO LA VARIABLE num1
            print("ERROR: la variable num2 tiene que ser numerico")
            self.num2 = input("Ingrese segundo numero: ")

    def menu(self):
        # Menu de operaciones
        print("Menu de operaciones")
        print("0.Crear base de datos")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Mostrar resultados")
        print("6. Salir")
        self.opcion = input("Ingrese una opcion: ")
        while self.opcion.isdigit() == False:
            # VERIFICANDO LA VARIABLE num1
            print("ERROR: la variable opcion tiene que ser numerico")
            self.opcion = input("Ingrese una opcion: ")

    def operacion(self, opcion):
        # Operaciones que se relieazara en el sistema para calculos
        if opcion == "1":  # Suma
            return {
                "num1": self.num1,
                "num2": self.num2,
                "operacion": "+",
                "resultado": Operaciones.suma(self),
            }
        if opcion == "2":  # Resta
            return {
                "num1": self.num1,
                "num2": self.num2,
                "operacion": "-",
                "resultado": Operaciones.resta(self),
            }
        if opcion == "3":  # Multiplicacion
            return {
                "num1": self.num1,
                "num2": self.num2,
                "operacion": "*",
                "resultado": Operaciones.multiplicacion(self),
            }
        if opcion == "4":  # Division
            return {
                "num1": self.num1,
                "num2": self.num2,
                "operacion": "/",
                "resultado": Operaciones.division(self),
            }

    def mostrarTodosLosResultados(self):
        # Mostrar todos los resultados guardados en la base de datos
        calculadora_table = CalculadoraTable()
        resultado = calculadora_table.all()
        i = int(0)  # Contador de para saber la cantidad de operaciones realizada
        if len(resultado) == 0:  # No hay registros en la base de datos
            print("No hay resultados registrados.")
            Otros.cargando(self)
        else:  # Muestra todos los registros
            anuncio = """
            ****************************************
            |TODOS LOS RESULADOS DE LAS OPERACIONES|
            ****************************************
            """
            print(anuncio)
            for row in resultado:
                i += 1
                print(f"{i}) {row[1]}  {row[3]} {row[2]} = {row[4]}")
            Otros.seguir(self)

    def operaciones(self):
        # Operaciones que se realizara en el modulo calculadora
        while True:
            Calculadora.menu(self)
            if self.opcion == "0":
                # Creacion de la base de datos
                matematica = CalculadoraTable()
                matematica.createDatabase()
                time.sleep(2)  # Pausa de 1 segundo par1a visualizar el resultado
                system("clear")
                continue
            if self.opcion == "6":  # Salir del sistema
                Otros.cargando(self)
                print("Gracias por usar nuestra calculadora!")
                time.sleep(1)
                system("clear")
                break
            elif self.opcion == "5":
                # Mostrar todos los resultados guardados en la base de datos
                Calculadora.mostrarTodosLosResultados(self)
                system("clear")
                continue
            ################################################################
            Calculadora.ingresoDeDatos(self)  # Funcion de ingreso de datos
            calculadora_table = (  # Llamada de la clase CalculadoraTable()
                CalculadoraTable()
            )
            resultado = Calculadora.operacion(self, self.opcion)
            if self.opcion == "1":
                # Suma de numeros
                print(
                    f"El resultado de la suma de {resultado['num1']} {resultado['operacion']} {resultado['num2']} es: {resultado['resultado']}"
                )
                calculadora_table.create(resultado)
                Otros.cargando(self)
            elif self.opcion == "2":
                # Resta de numeros
                print(
                    f"El resultado de la resta de {resultado['num1']} {resultado['operacion']} {resultado['num2']} es: {resultado['resultado']}"
                )
                calculadora_table.create(resultado)
                Otros.cargando(self)
            elif self.opcion == "3":
                # Multiplicacion de numeros
                print(
                    f"El resultado de la multiplicacion de {resultado['num1']} {resultado['operacion']} {resultado['num2']} es: {resultado['resultado']}"
                )
                calculadora_table.create(resultado)
                Otros.cargando(self)
            elif self.opcion == "4":
                # Division de numeros
                if resultado == False:
                    print("Error: No se puede dividir por cero.")
                    Otros.cargando(self)
                else:
                    print(
                        f"El resultado de la division de {resultado['num1']} {resultado['operacion']} {resultado['num2']} es: {resultado['resultado']}"
                    )
                    calculadora_table.create(resultado)
                    Otros.cargando(self)
            else:
                print("Opcion invalida, intente nuevamente.")
                Otros.cargando(self)
            time.sleep(1)  # Pausa de 1 segundo para visualizar el resultado
            system("clear")


calculadora = Calculadora()
calculadora.operaciones()
