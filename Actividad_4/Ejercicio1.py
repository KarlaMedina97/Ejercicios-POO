import tkinter as tk


class PruebaExcepciones:
    """Lanza diferentes excepciones en situaciones especificas del programa.

    Los mensajes que se muestran ayudan a identificar la porción de código
    que se ejecutó o no.
    """

    def __init__(self, imprimir):
        self.imprimir = imprimir

    def main(self):
        # Primer bloque try
        try:
            self.imprimir("Ingresando al primer try")
            cociente = 10000 / 0  # Se lanza una excepcion
            self.imprimir("Despues de la division")  # Nunca se ejecuta
        except ArithmeticError:  # Se captura la excepcion
            self.imprimir("Division por cero")
        finally:
            # La sentencia finally siempre se ejecuta, ocurra o no una excepcion
            self.imprimir("Ingresando al primer finally")

        # Segundo bloque try
        try:
            self.imprimir("Ingresando al segundo try")
            objeto = None
            objeto.toString()  # type: ignore  # Se lanza una excepcion
            self.imprimir("Imprimiendo objeto")  # Nunca se ejecuta
        except ArithmeticError:  # La excepcion lanzada no es de este tipo
            self.imprimir("Division por cero")
        except Exception:  # Se captura la excepcion
            self.imprimir("Ocurrio una excepcion")
        finally:
            self.imprimir("Ingresando al segundo finally")


class VentanaPruebaExcepciones:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Prueba de excepciones")
        self.ventana.resizable(False, False)

        tk.Label(
            ventana,
            text="Resultado de la ejecucion del metodo main",
            font=("Arial", 12, "bold"),
        ).grid(row=0, column=0, columnspan=2, padx=15, pady=(15, 10))

        self.salida = tk.Text(
            ventana, width=45, height=8, font=("Consolas", 10), state="disabled"
        )
        self.salida.grid(row=1, column=0, columnspan=2, padx=15, pady=5)

        tk.Button(ventana, text="Ejecutar", width=12, command=self.ejecutar).grid(
            row=2, column=0, sticky="e", padx=5, pady=12
        )
        tk.Button(ventana, text="Limpiar", width=12, command=self.limpiar).grid(
            row=2, column=1, sticky="w", padx=5, pady=12
        )

    def imprimir(self, mensaje):
        self.salida.config(state="normal")
        self.salida.insert("end", mensaje + "\n")
        self.salida.config(state="disabled")

    def ejecutar(self):
        self.limpiar()
        PruebaExcepciones(self.imprimir).main()

    def limpiar(self):
        self.salida.config(state="normal")
        self.salida.delete("1.0", "end")
        self.salida.config(state="disabled")


def main():
    ventana = tk.Tk()
    VentanaPruebaExcepciones(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()