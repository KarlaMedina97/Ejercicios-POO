import math
import tkinter as tk
from tkinter import messagebox


class VentanaNotas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Estadisticas de notas")
        self.ventana.resizable(False, False)

        tk.Label(
            ventana,
            text="Ingrese las cinco notas del estudiante:",
            font=("Arial", 12, "bold"),
        ).grid(row=0, column=0, columnspan=2, padx=15, pady=(15, 10))

        self.entradas = []
        for indice in range(5):
            tk.Label(ventana, text=f"Nota {indice + 1}:").grid(
                row=indice + 1, column=0, sticky="e", padx=(15, 5), pady=4
            )
            entrada = tk.Entry(ventana, width=15)
            entrada.grid(row=indice + 1, column=1, sticky="w", padx=(5, 15), pady=4)
            self.entradas.append(entrada)

        tk.Button(
            ventana,
            text="Calcular",
            command=self.calcular_estadisticas,
        ).grid(row=6, column=0, columnspan=2, pady=12)

        self.resultado = tk.Label(
            ventana,
            text="Promedio: --\nDesviacion estandar: --\nNota mayor: --\nNota menor: --",
            justify="left",
            font=("Arial", 10),
        )
        self.resultado.grid(
            row=7, column=0, columnspan=2, sticky="w", padx=15, pady=(0, 15)
        )

    def calcular_estadisticas(self):
        try:
            notas = [float(entrada.get().replace(",", ".")) for entrada in self.entradas]
        except ValueError:
            messagebox.showerror(
                "Entrada no valida",
                "Ingrese un valor numerico en cada una de las cinco notas.",
            )
            return

        if not all(math.isfinite(nota) for nota in notas):
            messagebox.showerror(
                "Entrada no valida",
                "Las notas deben ser numeros finitos.",
            )
            return

        promedio = sum(notas) / len(notas)
        desviacion = math.sqrt(
            sum((nota - promedio) ** 2 for nota in notas) / len(notas)
        )
        nota_mayor = max(notas)
        nota_menor = min(notas)

        self.resultado.config(
            text=(
                f"Promedio: {promedio:.2f}\n"
                f"Desviacion estandar: {desviacion:.2f}\n"
                f"Nota mayor: {nota_mayor:.2f}\n"
                f"Nota menor: {nota_menor:.2f}"
            )
        )


def main():
    ventana = tk.Tk()
    VentanaNotas(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()