import math


class Circulo:
	def __init__(self, radio: float):
		if radio <= 0:
			raise ValueError("El radio debe ser mayor que cero.")
		self.radio = radio

	def calcular_area(self) -> float:
		return math.pi * self.radio**2

	def calcular_perimetro(self) -> float:
		return 2 * math.pi * self.radio


class Rectangulo:
	def __init__(self, base: float, altura: float):
		if base <= 0 or altura <= 0:
			raise ValueError("La base y la altura deben ser mayores que cero.")
		self.base = base
		self.altura = altura

	def calcular_area(self) -> float:
		return self.base * self.altura

	def calcular_perimetro(self) -> float:
		return 2 * (self.base + self.altura)


class Cuadrado:
	def __init__(self, lado: float):
		if lado <= 0:
			raise ValueError("El lado debe ser mayor que cero.")
		self.lado = lado

	def calcular_area(self) -> float:
		return self.lado**2

	def calcular_perimetro(self) -> float:
		return 4 * self.lado


class TrianguloRectangulo:
	def __init__(self, base: float, altura: float):
		if base <= 0 or altura <= 0:
			raise ValueError("La base y la altura deben ser mayores que cero.")
		self.base = base
		self.altura = altura

	def calcular_hipotenusa(self) -> float:
		return math.hypot(self.base, self.altura)

	def calcular_area(self) -> float:
		return self.base * self.altura / 2

	def calcular_perimetro(self) -> float:
		return self.base + self.altura + self.calcular_hipotenusa()

	def determinar_tipo(self) -> str:
		hipotenusa = self.calcular_hipotenusa()
		lados = (self.base, self.altura, hipotenusa)
		if math.isclose(lados[0], lados[1]) and math.isclose(lados[1], lados[2]):
			return "Equilatero"
		if any(
			math.isclose(lado1, lado2)
			for indice, lado1 in enumerate(lados)
			for lado2 in lados[indice + 1 :]
		):
			return "Isosceles"
		return "Escaleno"


class PruebaFiguras:
	@staticmethod
	def main() -> None:
		circulo = Circulo(5)
		rectangulo = Rectangulo(4, 6)
		cuadrado = Cuadrado(4)
		triangulo = TrianguloRectangulo(3, 4)

		print("Circulo:")
		print(f"Area = {circulo.calcular_area():.2f} cm^2")
		print(f"Perimetro = {circulo.calcular_perimetro():.2f} cm")

		print("\nRectangulo:")
		print(f"Area = {rectangulo.calcular_area():.2f} cm^2")
		print(f"Perimetro = {rectangulo.calcular_perimetro():.2f} cm")

		print("\nCuadrado:")
		print(f"Area = {cuadrado.calcular_area():.2f} cm^2")
		print(f"Perimetro = {cuadrado.calcular_perimetro():.2f} cm")

		print("\nTriangulo rectangulo:")
		print(f"Area = {triangulo.calcular_area():.2f} cm^2")
		print(f"Hipotenusa = {triangulo.calcular_hipotenusa():.2f} cm")
		print(f"Perimetro = {triangulo.calcular_perimetro():.2f} cm")
		print(f"Tipo = {triangulo.determinar_tipo()}")


if __name__ == "__main__":
	PruebaFiguras.main()
