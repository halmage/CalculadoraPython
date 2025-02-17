class Operaciones:
    def suma(self):
        # Suma de numeros 1 + 1 = 2
        return int(self.num1) + int(self.num2)

    def resta(self):
        # Resta de numeros 2 - 1 = 1
        return int(self.num1) - int(self.num2)

    def multiplicacion(self):
        # Multiplicacion de numeros 2 * 2 = 4
        return int(self.num1) * int(self.num2)

    def division(self):
        # Division de numeros 6 / 2 = 3
        if self.num2 != "0":
            return int(self.num1) / int(self.num2)
        else:
            return False
