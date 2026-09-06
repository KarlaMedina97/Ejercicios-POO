#Ejercicio sin nada
# Entrada
ed_juan = float(input("Ingrese la edad de Juan: "))
#Proceso
ed_alberto = int(2 * ed_juan / 3)
ed_ana = int(4 * ed_juan / 3)
ed_mama = ed_juan + ed_alberto + ed_ana
#salida
print("Las edades son: ")
print("Alberto: ", ed_alberto)
print("Juan: ", ed_juan)
print("Ana: ", ed_ana)
print("Mamá: ", ed_mama)
print()

#Ejercicio con Clases
#Entrada
class Edades:
    def __init__(self, edad_juan):
        #Atributos
        self.edad_juan = edad_juan
        self.edad_alberto = 0
        self.edad_ana = 0
        self.edad_mama = 0
    def calcular_edades(self):
        #métodos
        self.edad_alberto = int(2 * self.edad_juan / 3)
        self.edad_ana = int(4 * self.edad_juan / 3)
        self.edad_mama = (
            self.edad_juan + self.edad_alberto + self.edad_ana
        )
    def mostrar_edades(self):
        print("Las edades son: ")
        print("Alberto: ", self.edad_alberto)
        print("Juan: ", self.edad_juan)
        print("Ana: ", self.edad_ana)
        print("Mamá: ", self.edad_mama )
edad = int(input("Ingrese la edad de Juan: "))
#Objeto Familia
familia = Edades(edad)
familia.calcular_edades()
familia.mostrar_edades()