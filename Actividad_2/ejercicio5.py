from enum import Enum


class TipoCuenta(Enum):
	AHORROS = "Ahorros"
	CORRIENTE = "Corriente"


class CuentaBancaria:
	def __init__(
		self,
		nombres_titular: str,
		apellidos_titular: str,
		numero_cuenta: str,
		tipo_cuenta: TipoCuenta,
	):
		self.nombres_titular = nombres_titular
		self.apellidos_titular = apellidos_titular
		self.numero_cuenta = numero_cuenta
		self.tipo_cuenta = tipo_cuenta
		self.saldo = 0.0

	def imprimir(self) -> None:
		print(f"Nombres del titular: {self.nombres_titular}")
		print(f"Apellidos del titular: {self.apellidos_titular}")
		print(f"Numero de cuenta: {self.numero_cuenta}")
		print(f"Tipo de cuenta: {self.tipo_cuenta.value}")
		print(f"Saldo: ${self.saldo:.2f}")

	def consultar_saldo(self) -> float:
		return self.saldo

	def consignar(self, valor: float) -> None:
		if valor <= 0:
			raise ValueError("El valor a consignar debe ser mayor que cero.")
		self.saldo += valor

	def retirar(self, valor: float) -> bool:
		if valor <= 0:
			raise ValueError("El valor a retirar debe ser mayor que cero.")
		if valor > self.saldo:
			return False
		self.saldo -= valor
		return True


def main():
	cuenta = CuentaBancaria(
		"Pedro",
		"Perez",
		"1234567890",
		TipoCuenta.AHORROS,
	)

	print("Datos iniciales de la cuenta:")
	cuenta.imprimir()

	cuenta.consignar(500000)
	print(f"\nSaldo despues de consignar: ${cuenta.consultar_saldo():.2f}")

	if cuenta.retirar(125000):
		print("Retiro realizado correctamente.")
	else:
		print("No hay saldo suficiente para realizar el retiro.")

	if cuenta.retirar(400000):
		print("Retiro realizado correctamente.")
	else:
		print("No hay saldo suficiente para realizar el retiro.")

	print(f"Saldo final: ${cuenta.consultar_saldo():.2f}")


if __name__ == "__main__":
	main()
