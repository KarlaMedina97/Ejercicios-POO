import tkinter as tk
from tkinter import messagebox


class Programador:
    """Modela un integrante de un equipo de la maraton de programacion."""

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    """Modela un equipo de programadores que participara en una maraton de programacion."""

    MINIMO_PROGRAMADORES = 2
    MAXIMO_PROGRAMADORES = 3

    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.tamano_equipo = 0  # El tamano del equipo inicialmente es cero
        self.programadores = [None] * self.MAXIMO_PROGRAMADORES

    def esta_lleno(self):
        return self.tamano_equipo == len(self.programadores)

    def anadir(self, programador):
        if self.esta_lleno():
            # Si el arreglo esta lleno, se genera la excepcion correspondiente
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores[self.tamano_equipo] = programador
        self.tamano_equipo += 1

    @staticmethod
    def validar_campo(campo):
        for caracter in campo:
            if caracter.isdigit():
                # Si el caracter es un digito se genera la excepcion correspondiente
                raise Exception("El nombre no puede tener dígitos.")
        if len(campo) >= 20:
            raise Exception("La longitud no debe ser igual o superior a 20 caracteres.")


class VentanaEquipo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Maraton de programacion")
        self.ventana.resizable(False, False)
        self.equipo = None

        marco_equipo = tk.LabelFrame(
            ventana, text="Datos del equipo", font=("Arial", 11, "bold")
        )
        marco_equipo.grid(row=0, column=0, padx=15, pady=(15, 5), sticky="ew")

        self.entradas_equipo = {}
        for indice, campo in enumerate(["Nombre del equipo", "Universidad", "Lenguaje"]):
            tk.Label(marco_equipo, text=f"{campo}:").grid(
                row=indice, column=0, sticky="e", padx=(10, 5), pady=4
            )
            entrada = tk.Entry(marco_equipo, width=25)
            entrada.grid(row=indice, column=1, sticky="w", padx=(5, 10), pady=4)
            self.entradas_equipo[campo] = entrada

        tk.Button(marco_equipo, text="Crear equipo", command=self.crear_equipo).grid(
            row=3, column=0, columnspan=2, pady=8
        )

        marco_integrante = tk.LabelFrame(
            ventana, text="Datos del integrante", font=("Arial", 11, "bold")
        )
        marco_integrante.grid(row=1, column=0, padx=15, pady=5, sticky="ew")

        self.entradas_integrante = {}
        for indice, campo in enumerate(["Nombre", "Apellidos"]):
            tk.Label(marco_integrante, text=f"{campo}:").grid(
                row=indice, column=0, sticky="e", padx=(10, 5), pady=4
            )
            entrada = tk.Entry(marco_integrante, width=25, state="disabled")
            entrada.grid(row=indice, column=1, sticky="w", padx=(5, 10), pady=4)
            self.entradas_integrante[campo] = entrada

        self.boton_anadir = tk.Button(
            marco_integrante,
            text="Añadir integrante",
            command=self.anadir_integrante,
            state="disabled",
        )
        self.boton_anadir.grid(row=2, column=0, columnspan=2, pady=8)

        self.resultado = tk.Label(
            ventana,
            text="Cree un equipo para empezar.",
            justify="left",
            font=("Arial", 10),
        )
        self.resultado.grid(row=2, column=0, sticky="w", padx=15, pady=(5, 15))

    def crear_equipo(self):
        datos = [entrada.get().strip() for entrada in self.entradas_equipo.values()]
        if not all(datos):
            messagebox.showerror(
                "Entrada no valida",
                "Ingrese el nombre del equipo, la universidad y el lenguaje.",
            )
            return

        self.equipo = EquipoMaratonProgramacion(*datos)
        for entrada in self.entradas_integrante.values():
            entrada.config(state="normal")
            entrada.delete(0, "end")
        self.boton_anadir.config(state="normal")
        self.mostrar_equipo()

    def anadir_integrante(self):
        nombre = self.entradas_integrante["Nombre"].get().strip()
        apellidos = self.entradas_integrante["Apellidos"].get().strip()
        if not nombre or not apellidos:
            messagebox.showerror(
                "Entrada no valida",
                "Ingrese el nombre y los apellidos del integrante.",
            )
            return

        try:
            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellidos)
            self.equipo.anadir(Programador(nombre, apellidos))
        except Exception as error:
            messagebox.showerror("Error", str(error))
            return

        for entrada in self.entradas_integrante.values():
            entrada.delete(0, "end")
        self.mostrar_equipo()

    def mostrar_equipo(self):
        equipo = self.equipo
        lineas = [
            f"Equipo: {equipo.nombre_equipo}",
            f"Universidad: {equipo.universidad}",
            f"Lenguaje: {equipo.lenguaje_programacion}",
            f"Integrantes ({equipo.tamano_equipo}/{len(equipo.programadores)}):",
        ]
        for programador in equipo.programadores[: equipo.tamano_equipo]:
            lineas.append(f"  - {programador.nombre} {programador.apellidos}")

        if equipo.esta_lleno():
            lineas.append("Estado: equipo completo")
        elif equipo.tamano_equipo >= EquipoMaratonProgramacion.MINIMO_PROGRAMADORES:
            lineas.append("Estado: puede participar (admite un integrante mas)")
        else:
            lineas.append("Estado: necesita minimo 2 integrantes para participar")

        self.resultado.config(text="\n".join(lineas))


def main():
    ventana = tk.Tk()
    VentanaEquipo(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()