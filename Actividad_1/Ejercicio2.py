#Ejercicio 2
# Inicio
class OperacionSuma:
    def __init__(self):
        self.suma = 0
        self.x = 20
        self.y = 0
    def calcular (self):
        self.suma = self.suma + self.x
        self.y = 40
        self.x = self.x + self.y ** 2
        self.suma = self.suma + self.x / self.y
    def mostrar_resultado(self):
        print("El valor de la suma es: ", self.suma)
operacion = OperacionSuma()
operacion.calcular()
operacion.mostrar_resultado()

