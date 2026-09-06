#Ejercicio 3
#Un empleado trabaja 48 horas a la semana a razón de $5.000 la hora.
#La retención en la fuente es del 12,5% del salario bruto.
#Se calcula el salario bruto, la retención y el salario neto.
class Empleado:
    def __init__(self, horas, valor_hora, porcentaje_retencion):
        #Atributos
        self.horas = horas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion
        self.salario_bruto = 0
        self.retencion = 0
        self.salario_neto = 0
    def calcular_salario(self):
        #Métodos
        self.salario_bruto = self.horas * self.valor_hora
        self.retencion = self.salario_bruto * self.porcentaje_retencion / 100
        self.salario_neto = self.salario_bruto - self.retencion
    def mostrar_salario(self):
        print("Salario bruto: ", self.salario_bruto)
        print("Retención en la fuente: ", self.retencion)
        print("Salario neto: ", self.salario_neto)
#Objeto empleado
empleado = Empleado(48, 5000, 12.5)
empleado.calcular_salario()
empleado.mostrar_salario()