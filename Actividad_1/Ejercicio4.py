#Ejercicio 4
#Leer un número y obtener su cuadrado y su cubo.
class Numero:
    def __init__(self, numero):
        #Atributos
        self.numero = numero
        self.cuadrado = 0
        self.cubo = 0
    def calcular_potencias(self):
        #Métodos
        self.cuadrado = self.numero ** 2
        self.cubo = self.numero ** 3
    def mostrar_resultados(self):
        print("Número: ", self.numero)
        print("Cuadrado: ", self.cuadrado)
        print("Cubo: ", self.cubo)
#Entrada
valor = int(input("Ingrese un número: "))
#Objeto número
numero = Numero(valor)
numero.calcular_potencias()
numero.mostrar_resultados()
