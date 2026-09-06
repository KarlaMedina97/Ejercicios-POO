#Ejercicio 5
#Dado el radio de un círculo, obtener el área y la longitud de la circunferencia.
import math
class Circulo:
    def __init__(self, radio):
        #Atributos
        self.radio = radio
        self.area = 0
        self.longitud = 0
    def calcular(self):
        #Métodos
        self.area = round(math.pi * self.radio ** 2, 3)
        self.longitud = round(2 * math.pi * self.radio, 3)
    def mostrar_resultados(self):
        print("Radio: ", self.radio)
        print("Área del círculo: ", self.area)
        print("Longitud de la circunferencia: ", self.longitud)
#Entrada
radio = float(input("Ingrese el radio del círculo: "))
#Objeto círculo
circulo = Circulo(radio)
circulo.calcular()
circulo.mostrar_resultados()
