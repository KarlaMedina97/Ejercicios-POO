class Persona:
	def __init__(
		self,
		nombre,
		apellido,
		numero_documento,
		anio_nacimiento,
		pais_nacimiento,
		genero,
	):
		if genero not in ("H", "M"):
			raise ValueError("El genero debe ser 'H' o 'M'.")

		self.nombre = nombre
		self.apellido = apellido
		self.numero_documento = numero_documento
		self.anio_nacimiento = anio_nacimiento
		self.pais_nacimiento = pais_nacimiento
		self.genero = genero

	def imprimir(self):
		print(f"Nombre = {self.nombre}")
		print(f"Apellidos = {self.apellido}")
		print(f"N\u00famero de documento de identidad = {self.numero_documento}")
		print(f"A\u00f1o de nacimiento = {self.anio_nacimiento}")
		print(f"Pa\u00eds de nacimiento = {self.pais_nacimiento}")
		print(f"G\u00e9nero = {self.genero}")


def main():
	persona1 = Persona("Pedro", "P\u00e9rez", "1053121010", 1998, "Colombia", "H")
	persona2 = Persona("Luis", "Le\u00f3n", "1053223344", 2001, "Colombia", "H")
	persona1.imprimir()
	print()
	persona2.imprimir()


if __name__ == "__main__":
	main()