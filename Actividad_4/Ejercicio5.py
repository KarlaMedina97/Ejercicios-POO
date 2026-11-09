import io
import os
import tkinter as tk
from tkinter import filedialog


class LeerArchivo:
    """Lee los datos presentes en un archivo de texto con extension .txt."""

    @staticmethod
    def leer(nombre_archivo):
        lineas = []
        try:
            # FileIO es el flujo de bytes (equivalente de FileInputStream)
            archivo = io.FileIO(nombre_archivo, "r")
            # BufferedReader agrega el buffer de lectura
            filtro = io.BufferedReader(archivo)
            # TextIOWrapper convierte los bytes en texto (equivalente de InputStreamReader)
            conversor = io.TextIOWrapper(filtro, encoding="utf-8", errors="replace")
            linea = conversor.readline()
            while linea != "":
                lineas.append(linea.rstrip("\n"))  # Guarda una linea del archivo
                linea = conversor.readline()  # Lee la siguiente linea
            conversor.close()  # Cierra el archivo
        except OSError:  # Equivalente de IOException
            return "No se pudo leer el archivo."
        return "\n".join(lineas)


class VentanaLeerArchivo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Leer archivo")
        self.ventana.resizable(False, False)

        tk.Label(
            ventana,
            text="Seleccione el archivo de texto a leer:",
            font=("Arial", 12, "bold"),
        ).grid(row=0, column=0, columnspan=3, padx=15, pady=(15, 10))

        tk.Label(ventana, text="Archivo:").grid(
            row=1, column=0, sticky="e", padx=(15, 5), pady=4
        )
        self.entrada = tk.Entry(ventana, width=45)
        self.entrada.grid(row=1, column=1, sticky="w", padx=5, pady=4)
        self.entrada.insert(
            0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "prueba.txt")
        )
        tk.Button(ventana, text="Examinar...", command=self.examinar).grid(
            row=1, column=2, sticky="w", padx=(5, 15), pady=4
        )

        tk.Button(ventana, text="Leer", width=12, command=self.leer_archivo).grid(
            row=2, column=0, columnspan=3, pady=12
        )

        marco_texto = tk.Frame(ventana)
        marco_texto.grid(row=3, column=0, columnspan=3, padx=15, pady=(0, 15))
        barra = tk.Scrollbar(marco_texto)
        barra.pack(side="right", fill="y")
        self.salida = tk.Text(
            marco_texto,
            width=60,
            height=12,
            font=("Consolas", 10),
            state="disabled",
            yscrollcommand=barra.set,
        )
        self.salida.pack(side="left")
        barra.config(command=self.salida.yview)

    def examinar(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
        )
        if ruta:
            self.entrada.delete(0, "end")
            self.entrada.insert(0, ruta)

    def leer_archivo(self):
        contenido = LeerArchivo.leer(self.entrada.get().strip())
        self.salida.config(state="normal")
        self.salida.delete("1.0", "end")
        self.salida.insert("end", contenido)
        self.salida.config(state="disabled")


def main():
    ventana = tk.Tk()
    VentanaLeerArchivo(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()