import tkinter as tk
from tkinter import messagebox


class Vendedor:
    """Modela un vendedor que tiene como atributos un nombre, apellidos y una edad."""

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0

    def imprimir(self):
        return (
            f"Nombre del vendedor = {self.nombre}\n"
            f"Apellidos del vendedor = {self.apellidos}\n"
            f"Edad del vendedor = {self.edad}"
        )

    def verificar_edad(self, edad):
        # ValueError es el equivalente en Python de IllegalArgumentException
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        if edad <= 120:
            self.edad = edad
        else:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")


class VentanaVendedor:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registro de vendedor")
        self.ventana.resizable(False, False)

        tk.Label(