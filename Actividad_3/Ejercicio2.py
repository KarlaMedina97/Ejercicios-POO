import math
import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import messagebox


class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_volumen(self):
        pass

    @abstractmethod
    def calcular_superficie(self):
        pass


class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        return math.pi * self.radio**2 * self.altura

    def calcular_superficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)


class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        return (4 / 3) * math.pi * self.radio**3

    def calcular_superficie(self):
        return 4 * math.pi * self.radio**2


class Piramide(FiguraGeometrica):
    def __init__(self, area_base, altura, apotema):
        self.area_base = area_base
        self.altura = altura
        self.apotema = apotema

    def calcular_volumen(self):
        return self.area_base * self.altura / 3

    def calcular_superficie(self):
        lado_base = math.sqrt(self.area_base)
        perimetro_base = 4 * lado_base
        area_lateral = perimetro_base * self.apotema / 2
        return self.area_base + area_lateral


class VentanaFiguras:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Volumen y superficie de figuras")
        self.ventana.resizable(False, False)
        self.campos = {}

        formulario = tk.Frame(ventana, padx=15, pady=15)
        formulario.grid(row=0, column=0, sticky="ew")

        tk.Label(
            formulario,
            text="Ingrese las dimensiones en centimetros:",
            font=("Arial", 12, "bold"),
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

        dimensiones = (
            ("Radio del cilindro (cm):", "radio_cilindro"),
            ("Altura del cilindro (cm):", "altura_cilindro"),
            ("Radio de la esfera (cm):", "radio_esfera"),
            ("Area de la base cuadrada de la piramide (cm^2):", "area_base"),
            ("Altura de la piramide (cm):", "altura_piramide"),
            ("Apotema de la piramide (cm):", "apotema"),
        )
        for fila, (etiqueta, nombre) in enumerate(dimensiones, start=1):
            tk.Label(formulario, text=etiqueta).grid(
                row=fila, column=0, sticky="w", padx=(0, 10), pady=4
            )
            campo = tk.Entry(formulario, width=18)
            campo.grid(row=fila, column=1, sticky="ew", pady=4)
            self.campos[nombre] = campo

        tk.Button(
            formulario,
            text="Calcular",
            command=self.calcular,
        ).grid(row=len(dimensiones) + 1, column=0, columnspan=2, pady=(12, 4))

        self.resultado = tk.Label(
            ventana,
            text=(
                "Cilindro: volumen -- cm^3 | superficie -- cm^2\n"
                "Esfera: volumen -- cm^3 | superficie -- cm^2\n"
                "Piramide: volumen -- cm^3 | superficie -- cm^2"
            ),
            justify="left",
            font=("Arial", 10),
        )
        self.resultado.grid(row=1, column=0, sticky="w", padx=15, pady=(0, 15))

    def calcular(self):
        dimensiones = {}
        try:
            for nombre, campo in self.campos.items():
                valor = float(campo.get().strip().replace(",", "."))
                if not math.isfinite(valor) or valor <= 0:
                    raise ValueError
                dimensiones[nombre] = valor
        except ValueError:
            messagebox.showerror(
                "Entrada no valida",
                "Ingrese un numero mayor que cero en cada dimension.",
            )
            return

        figuras = (
            (
                "Cilindro",
                Cilindro(
                    dimensiones["radio_cilindro"],
                    dimensiones["altura_cilindro"],
                ),
            ),
            ("Esfera", Esfera(dimensiones["radio_esfera"])),
            (
                "Piramide",
                Piramide(
                    dimensiones["area_base"],
                    dimensiones["altura_piramide"],
                    dimensiones["apotema"],
                ),
            ),
        )
        lineas = [
            f"{nombre}: volumen {figura.calcular_volumen():.2f} cm^3"
            f" | superficie {figura.calcular_superficie():.2f} cm^2"
            for nombre, figura in figuras
        ]
        self.resultado.config(text="\n".join(lineas))


def main():
    ventana = tk.Tk()
    VentanaFiguras(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
