import tkinter as tk
from datetime import date
from tkinter import messagebox, simpledialog


def formato_pesos(valor):
    return f"${valor:,.0f}"


def leer_fecha(texto):
    """Convierte un texto con formato AAAA-MM-DD en una fecha."""
    try:
        return date.fromisoformat(texto.strip())
    except ValueError:
        raise ValueError("Ingrese la fecha con el formato AAAA-MM-DD.") from None


class Huesped:
    """Modela un huesped del hotel."""

    def __init__(self, nombres, apellidos, documento, fecha_ingreso):
        for campo in (nombres, apellidos):
            if any(caracter.isdigit() for caracter in campo):
                raise ValueError("Los nombres y apellidos no pueden tener dígitos.")
        if not documento.isdigit():
            raise ValueError("El documento de identidad debe ser numérico.")
        self.nombres = nombres
        self.apellidos = apellidos
        self.documento = documento
        self.fecha_ingreso = fecha_ingreso

    def calcular_dias_alojamiento(self, fecha_salida):
        dias = (fecha_salida - self.fecha_ingreso).days
        if dias <= 0:
            raise ValueError("La fecha de salida debe ser posterior a la de ingreso.")
        return dias


class Habitacion:
    """Modela una habitacion simple del hotel y el huesped que la ocupa."""

    def __init__(self, numero, precio_dia):
        self.numero = numero
        self.precio_dia = precio_dia
        self.huesped = None  # Inicialmente la habitacion esta desocupada

    @property
    def disponible(self):
        # La disponibilidad depende de si hay un huesped en la habitacion
        return self.huesped is None

    def ocupar(self, huesped):
        if not self.disponible:
            raise ValueError(f"La habitación {self.numero} no está disponible.")
        self.huesped = huesped

    def calcular_cobro(self, fecha_salida):
        dias = self.huesped.calcular_dias_alojamiento(fecha_salida)
        return dias, dias * self.precio_dia

    def liberar(self):
        self.huesped = None


class Hotel:
    """Modela un hotel compuesto por diez habitaciones simples."""

    TOTAL_HABITACIONES = 10
    PRECIO_ECONOMICO = 120000  # Habitaciones 1 a 5
    PRECIO_SUPERIOR = 160000  # Habitaciones 6 a 10

    def __init__(self):
        self.habitaciones = [
            Habitacion(
                numero,
                self.PRECIO_ECONOMICO if numero <= 5 else self.PRECIO_SUPERIOR,
            )
            for numero in range(1, self.TOTAL_HABITACIONES + 1)
        ]

    def buscar(self, numero):
        if not 1 <= numero <= self.TOTAL_HABITACIONES:
            raise ValueError("Ingrese un número de habitación entre 1 y 10.")
        return self.habitaciones[numero - 1]

    def buscar_ocupada(self, numero):
        habitacion = self.buscar(numero)
        if habitacion.disponible:
            raise ValueError(f"La habitación {numero} no está ocupada.")
        return habitacion


class VentanaHabitaciones:
    """Muestra las diez habitaciones y permite elegir la habitacion a ocupar."""

    COLUMNAS = 5

    def __init__(self, ventana_padre, hotel):
        self.ventana_padre = ventana_padre
        self.hotel = hotel
        self.ventana = tk.Toplevel(ventana_padre)
        self.ventana.title("Habitaciones")
        self.ventana.resizable(False, False)
        # Modal para que el estado mostrado no quede desactualizado
        self.ventana.transient(ventana_padre)
        self.ventana.grab_set()

        # Cuadricula de 2 x 5 (equivalente a GridLayout)
        marco_habitaciones = tk.Frame(self.ventana)
        marco_habitaciones.pack(side="top", padx=15, pady=(15, 5))
        for indice, habitacion in enumerate(hotel.habitaciones):
            celda = tk.LabelFrame(
                marco_habitaciones,
                text=f"Habitación {habitacion.numero}",
                font=("Arial", 10, "bold"),
            )
            celda.grid(
                row=indice // self.COLUMNAS,
                column=indice % self.COLUMNAS,
                padx=5,
                pady=5,
                sticky="nsew",
            )
            estado = "Disponible" if habitacion.disponible else "No disponible"
            color = "dark green" if habitacion.disponible else "red"
            tk.Label(celda, text=estado, fg=color, width=14).pack(padx=5, pady=(4, 0))
            tk.Label(celda, text=f"{formato_pesos(habitacion.precio_dia)} / día").pack(
                padx=5, pady=(0, 4)
            )

        # Fila de seleccion (equivalente a FlowLayout)
        marco_seleccion = tk.Frame(self.ventana)
        marco_seleccion.pack(side="bottom", pady=(5, 15))
        tk.Label(marco_seleccion, text="Habitación a ocupar:").pack(side="left", padx=5)
        self.seleccion = tk.Spinbox(
            marco_seleccion,
            from_=1,
            to=Hotel.TOTAL_HABITACIONES,
            width=5,
            state="readonly",
        )
        self.seleccion.pack(side="left", padx=5)
        tk.Button(
            marco_seleccion, text="Aceptar", width=10, command=self.seleccionar
        ).pack(side="left", padx=5)

    def seleccionar(self):
        habitacion = self.hotel.buscar(int(self.seleccion.get()))
        if not habitacion.disponible:
            messagebox.showerror(
                "Habitación ocupada",
                f"La habitación {habitacion.numero} no está disponible.",
                parent=self.ventana,
            )
            return
        self.ventana.destroy()
        VentanaIngreso(self.ventana_padre, habitacion)


class VentanaIngreso:
    """Formulario para registrar el ingreso de un huesped a una habitacion."""

    CAMPOS = ["Fecha de ingreso", "Nombres", "Apellidos", "Documento de identidad"]

    def __init__(self, ventana_padre, habitacion):
        self.habitacion = habitacion
        self.ventana = tk.Toplevel(ventana_padre)
        self.ventana.title("Ingreso de huésped")
        self.ventana.resizable(False, False)
        self.ventana.transient(ventana_padre)
        self.ventana.grab_set()

        # Formulario con grid y sticky (equivalente a GridBagLayout)
        marco = tk.LabelFrame(
            self.ventana,
            text=f"Habitación {habitacion.numero}",
            font=("Arial", 11, "bold"),
        )
        marco.grid(row=0, column=0, padx=15, pady=(15, 5), sticky="ew")

        self.entradas = {}
        for indice, campo in enumerate(self.CAMPOS):
            tk.Label(marco, text=f"{campo}:").grid(
                row=indice, column=0, sticky="e", padx=(10, 5), pady=4
            )
            entrada = tk.Entry(marco, width=25)
            entrada.grid(row=indice, column=1, sticky="w", padx=(5, 10), pady=4)
            self.entradas[campo] = entrada
        self.entradas["Fecha de ingreso"].insert(0, date.today().isoformat())
        tk.Label(marco, text="Formato de fecha: AAAA-MM-DD", fg="gray").grid(
            row=len(self.CAMPOS), column=0, columnspan=2, pady=(0, 6)
        )

        tk.Button(
            self.ventana, text="Registrar ingreso", command=self.registrar
        ).grid(row=1, column=0, pady=(5, 15))

    def registrar(self):
        datos = {campo: entrada.get().strip() for campo, entrada in self.entradas.items()}
        if not all(datos.values()):
            messagebox.showerror(
                "Entrada no valida",
                "Todos los campos son obligatorios.",
                parent=self.ventana,
            )
            return

        try:
            huesped = Huesped(
                datos["Nombres"],
                datos["Apellidos"],
                datos["Documento de identidad"],
                leer_fecha(datos["Fecha de ingreso"]),
            )
            self.habitacion.ocupar(huesped)
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=self.ventana)
            return

        messagebox.showinfo(
            "Registro exitoso",
            f"{huesped.nombres} {huesped.apellidos} ingresó a la habitación "
            f"{self.habitacion.numero}.",
            parent=self.ventana,
        )
        self.ventana.destroy()


class VentanaSalida:
    """Registra la salida de un huesped y calcula el total a pagar."""

    def __init__(self, ventana_padre, habitacion):
        self.habitacion = habitacion
        huesped = habitacion.huesped
        self.ventana = tk.Toplevel(ventana_padre)
        self.ventana.title("Salida de huésped")
        self.ventana.resizable(False, False)
        self.ventana.transient(ventana_padre)
        self.ventana.grab_set()

        marco = tk.LabelFrame(
            self.ventana,
            text=f"Habitación {habitacion.numero}",
            font=("Arial", 11, "bold"),
        )
        marco.grid(row=0, column=0, padx=15, pady=(15, 5), sticky="ew")

        datos = [
            ("Huésped:", f"{huesped.nombres} {huesped.apellidos}"),
            ("Documento:", huesped.documento),
            ("Fecha de ingreso:", huesped.fecha_ingreso.isoformat()),
            ("Precio por día:", formato_pesos(habitacion.precio_dia)),
        ]
        for indice, (etiqueta, valor) in enumerate(datos):
            tk.Label(marco, text=etiqueta).grid(
                row=indice, column=0, sticky="e", padx=(10, 5), pady=3
            )
            tk.Label(marco, text=valor).grid(
                row=indice, column=1, sticky="w", padx=(5, 10), pady=3
            )

        tk.Label(marco, text="Fecha de salida:").grid(
            row=4, column=0, sticky="e", padx=(10, 5), pady=4
        )
        self.fecha_salida = tk.StringVar()
        # Cada cambio en la fecha vuelve a validar si se puede calcular
        self.fecha_salida.trace_add("write", self.validar_fecha)
        tk.Entry(marco, width=15, textvariable=self.fecha_salida).grid(
            row=4, column=1, sticky="w", padx=(5, 10), pady=4
        )
        self.aviso = tk.Label(marco, text="Formato de fecha: AAAA-MM-DD", fg="gray")
        self.aviso.grid(row=5, column=0, columnspan=2, pady=(0, 6))

        marco_botones = tk.Frame(self.ventana)
        marco_botones.grid(row=1, column=0, pady=5)
        self.boton_calcular = tk.Button(
            marco_botones,
            text="Calcular",
            width=14,
            state="disabled",
            command=self.calcular,
        )
        self.boton_calcular.pack(side="left", padx=5)
        self.boton_registrar = tk.Button(
            marco_botones,
            text="Registrar salida",
            width=14,
            state="disabled",
            command=self.registrar_salida,
        )
        self.boton_registrar.pack(side="left", padx=5)

        self.resultado = tk.Label(
            self.ventana,
            text="Días de alojamiento: --\nTotal a pagar: --",
            justify="left",
            font=("Arial", 10),
        )
        self.resultado.grid(row=2, column=0, sticky="w", padx=15, pady=(5, 15))

    def validar_fecha(self, *_):
        # Al cambiar la fecha se descarta el calculo anterior
        self.boton_registrar.config(state="disabled")
        self.resultado.config(text="Días de alojamiento: --\nTotal a pagar: --")
        try:
            self.habitacion.calcular_cobro(leer_fecha(self.fecha_salida.get()))
        except ValueError as error:
            self.boton_calcular.config(state="disabled")
            self.aviso.config(text=str(error), fg="red")
            return
        self.boton_calcular.config(state="normal")
        self.aviso.config(text="Fecha válida", fg="dark green")

    def calcular(self):
        dias, total = self.habitacion.calcular_cobro(
            leer_fecha(self.fecha_salida.get())
        )
        self.resultado.config(
            text=f"Días de alojamiento: {dias}\nTotal a pagar: {formato_pesos(total)}"
        )
        self.boton_registrar.config(state="normal")

    def registrar_salida(self):
        self.habitacion.liberar()
        messagebox.showinfo(
            "Salida registrada",
            f"La habitación {self.habitacion.numero} quedó disponible.",
            parent=self.ventana,
        )
        self.ventana.destroy()


class VentanaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Hotel")
        self.ventana.resizable(False, False)
        self.hotel = Hotel()

        barra_menu = tk.Menu(ventana)
        menu_opciones = tk.Menu(barra_menu, tearoff=0)
        menu_opciones.add_command(
            label="Consultar habitaciones", command=self.consultar_habitaciones
        )
        menu_opciones.add_command(
            label="Salida de huéspedes", command=self.salida_huespedes
        )
        barra_menu.add_cascade(label="Opciones", menu=menu_opciones)
        ventana.config(menu=barra_menu)

        # Distribucion por regiones con pack (equivalente a BorderLayout)
        tk.Label(
            ventana,
            text="Gestión de huéspedes del hotel",
            font=("Arial", 12, "bold"),
        ).pack(side="top", padx=30, pady=(20, 5))
        tk.Label(
            ventana,
            text=(
                f"Habitaciones 1 a 5: {formato_pesos(Hotel.PRECIO_ECONOMICO)} por día\n"
                f"Habitaciones 6 a 10: {formato_pesos(Hotel.PRECIO_SUPERIOR)} por día"
            ),
            justify="left",
        ).pack(side="top", padx=30, pady=5)
        tk.Label(ventana, text="Use el menú Opciones para comenzar.").pack(
            side="bottom", padx=30, pady=(5, 20)
        )

    def consultar_habitaciones(self):
        VentanaHabitaciones(self.ventana, self.hotel)

    def salida_huespedes(self):
        texto = simpledialog.askstring(
            "Salida de huéspedes",
            "Ingrese el número de la habitación a entregar:",
            parent=self.ventana,
        )
        if texto is None:  # El usuario cancelo el cuadro de dialogo
            return

        try:
            numero = int(texto)
        except ValueError:
            messagebox.showerror(
                "Entrada no valida",
                "Ingrese un número de habitación válido.",
                parent=self.ventana,
            )
            return

        try:
            habitacion = self.hotel.buscar_ocupada(numero)
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=self.ventana)
            return
        VentanaSalida(self.ventana, habitacion)


def main():
    ventana = tk.Tk()
    VentanaPrincipal(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
