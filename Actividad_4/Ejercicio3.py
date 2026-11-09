import math
import tkinter as tk


class CalculosNumericos:
    """Permite calcular el logaritmo neperiano y la raiz cuadrada de un valor."""

    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        try:
            if valor <= 0:
                # Si el valor no es positivo, se genera una excepcion aritmetica
                raise ArithmeticError("El valor debe ser un numero positivo")
            resultado = math.log(valor)
            return f"Resultado = {resultado:.4f}"
        except ArithmeticError:
            return "El valor debe ser un numero positivo para calcular el logaritmo"

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        try:
            if valor < 0:
                # Si el valor es negativo, se genera una excepcion aritmetica
                raise ArithmeticError("El valor debe ser un numero positivo")
            resultado = math.sqrt(valor)
            return f"Resultado = {resultado:.4f}"
        except ArithmeticError:
            return "El valor debe ser un numero positivo para calcular la raiz cuadrada"


class VentanaCalculos:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculos numericos")
        self.ventana.resizable(False, False)

        tk.Label(
            ventana,
            text="Ingrese un valor numerico:",
            font=("Arial", 12, "bold"),
        ).grid(row=0, column=0, columnspan=2, padx=15, pady=(15, 10))

        tk.Label(ventana, text="Valor:").grid(
            row=1, column=0, sticky="e", padx=(15, 5), pady=4
        )
        self.entrada = tk.Entry(ventana, width=20)
        self.entrada.grid(row=1, column=1, sticky="w", padx=(5, 15), pady=4)

        tk.Button(
            ventana,
            text="Calcular",
            command=self.calcular,
        ).grid(row=2, column=0, columnspan=2, pady=12)

        self.resultado = tk.Label(
            ventana,
            text="Logaritmo neperiano: --\nRaiz cuadrada: --",
            justify="left",
            font=("Arial", 10),
        )
        self.resultado.grid(
            row=3, column=0, columnspan=2, sticky="w", padx=15, pady=(0, 15)
        )

    def calcular(self):
        texto = self.entrada.get().replace(",", ".")
        try:
            valor = float(texto)
            if not math.isfinite(valor):
                raise ValueError
        except ValueError:
            # Equivalente de InputMismatchException: el valor no es numerico
            self.resultado.config(
                text=(
                    "Logaritmo neperiano: El valor debe ser numerico para calcular el logaritmo\n"
                    "Raiz cuadrada: El valor debe ser numerico para calcular la raiz cuadrada"
                )
            )
            return

        self.resultado.config(
            text=(
                f"Logaritmo neperiano: {CalculosNumericos.calcular_logaritmo_neperiano(valor)}\n"
                f"Raiz cuadrada: {CalculosNumericos.calcular_raiz_cuadrada(valor)}"
            )
        )


def main():
    ventana = tk.Tk()
    VentanaCalculos(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()