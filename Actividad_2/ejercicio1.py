class Persona:
	def __init__(self, nombre, apellido, numero_documento, anio_nacimiento):
		self.nombre = nombre
		self.apellido = apellido
		self.numero_documento = numero_documento
		self.anio_nacimiento = anio_nacimiento

	def mostrar_atributos(self):
		print(f"Nombre: {self.nombre}")
		print(f"Apellido: {self.apellido}")
		print(f"Numero de documento: {self.numero_documento}")
		print(f"Anio de nacimiento: {self.anio_nacimiento}")


def main():
	persona1 = Persona("Ana", "Gomez", "123456789", 2000)
	persona2 = Persona("Carlos", "Rodriguez", "987654321", 1998)

	print("Persona 1:")
	persona1.mostrar_atributos()
	print("\nPersona 2:")
	persona2.mostrar_atributos()


if __name__ == "__main__":
	main()
