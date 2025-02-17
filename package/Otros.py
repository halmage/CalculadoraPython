# Librerias externa
import time
from os import system


class Otros:
    def cargando(self):
        for i in range(2):
            print(".")
            time.sleep(0.5)  # Pausa de 1 segundo para visualizar el resultado

    def seguir(self):
        # Funcion para seguir con la ejecucion del programa
        print("\nPresione Enter para continuar...")
        input()
        system("clear")
