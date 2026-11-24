import os
import tkinter as tk
from enum import Enum
from tkinter import filedialog, messagebox, ttk


def formato_pesos(valor):
    return f"${valor:,.2f}"


class TipoCargo(Enum):
    """Tipos de cargo que puede tener un empleado."""

    DIRECTIVO = "Directivo"
    ESTRATEGICO = "Estratégico"
    OPERATIVO = "Operativo"


class TipoGenero(Enum):
    """Tipos de genero que puede tener un empleado."""

    MASCULINO = "Masculino"
    FEMENINO = "Femenino"


class Empleado:
    """Modela un empleado de una empresa y calcula su salario mensual."""

    MINIMO_DIAS = 1
    MAXIMO_DIAS = 31

    def __init__(
        self,
        nombre,
        apellidos,
        cargo,
        genero,
        salario_dia,
        dias_trabajados,
        otros_ingresos,
        pagos_salud,
        aporte_pensiones,
    ):
        if not self.MINIMO_DIAS <= dias_trabajados <= self.MAXIMO_DIAS:
            raise ValueError("Los días trabajados deben estar entre 1 y 31.")
        if min(salario_dia, otros_ingresos, pagos_salud, aporte_pensiones) < 0:
            raise ValueError("Los valores monetarios no pueden ser negativos.")
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.genero = genero
        self.salario_dia = salario_dia
        self.dias_trabajados = dias_trabajados
        self.otros_ingresos = otros_ingresos
        self.pagos_salud = pagos_salud
        self.aporte_pensiones = aporte_pensiones

    def calcular_nomina(self):
        return (
            self.dias_trabajados * self.salario_dia
            + self.otros_ingresos
            - self.pagos_salud
            - self.aporte_pensiones
        )


class ListaEmpleados:
    """Agrupa los empleados registrados y calcula el total de la nomina."""

    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def calcular_total_nomina(self):
        # El total se calcula cada vez para no acumular valores repetidos
        return sum(empleado.calcular_nomina() for empleado in self.empleados)

    def convertir_texto(self):
        bloques = []
        for empleado in self.empleados:
            bloques.append(
                f"Nombre = {empleado.nombre}\n"
                f"Apellidos = {empleado.apellidos}\n"
                f"Cargo = {empleado.cargo.value}\n"
                f"Género = {empleado.genero.value}\n"
                f"Salario por día = {formato_pesos(empleado.salario_dia)}\n"
                f"Días trabajados = {empleado.dias_trabajados}\n"
                f"Otros ingresos = {formato_pesos(empleado.otros_ingresos)}\n"
                f"Pagos salud = {formato_pesos(empleado.pagos_salud)}\n"
                f"Aporte pensiones = {formato_pesos(empleado.aporte_pensiones)}\n"
                f"Salario mensual = {formato_pesos(empleado.calcular_nomina())}\n"
                "---------"
            )
        bloques.append(f"Total nómina = {formato_pesos(self.calcular_total_nomina())}")
        return "\n".join(bloques)


class VentanaAgregarEmpleado:
    """Cuadro de dialogo modal para ingresar los datos de un empleado."""

    CAMPOS_NUMERICOS = [
        "Salario por día",
        "Otros ingresos",
        "Pagos por salud",
        "Aporte pensiones",
    ]

    def __init__(self, ventana_padre, lista_empleados, al_agregar):
        self.lista_empleados = lista_empleados
        self.al_agregar = al_agregar
        self.ventana = tk.Toplevel(ventana_padre)
        self.ventana.title("Agregar empleado")
        self.ventana.resizable(False, False)
        # transient y grab_set hacen que el cuadro de dialogo sea modal
        self.ventana.transient(ventana_padre)
        self.ventana.grab_set()

        marco = tk.LabelFrame(
            self.ventana, text="Datos del empleado", font=("Arial", 11, "bold")
        )
        marco.grid(row=0, column=0, padx=15, pady=(15, 5), sticky="ew")

        self.entradas = {}
        for indice, campo in enumerate(["Nombre", "Apellidos"]):
            tk.Label(marco, text=f"{campo}:").grid(
                row=indice, column=0, sticky="e", padx=(10, 5), pady=4
            )
            entrada = tk.Entry(marco, width=25)
            entrada.grid(row=indice, column=1, sticky="w", padx=(5, 10), pady=4)
            self.entradas[campo] = entrada

        tk.Label(marco, text="Cargo:").grid(
            row=2, column=0, sticky="e", padx=(10, 5), pady=4
        )
        self.cargo = ttk.Combobox(
            marco,
            values=[cargo.value for cargo in TipoCargo],
            state="readonly",
            width=22,
        )
        self.cargo.grid(row=2, column=1, sticky="w", padx=(5, 10), pady=4)

        tk.Label(marco, text="Género:").grid(
            row=3, column=0, sticky="e", padx=(10, 5), pady=4
        )
        self.genero = tk.StringVar()
        marco_genero = tk.Frame(marco)
        marco_genero.grid(row=3, column=1, sticky="w", padx=(5, 10), pady=4)
        for genero in TipoGenero:
            tk.Radiobutton(
                marco_genero, text=genero.value, variable=self.genero, value=genero.name
            ).pack(side="left")

        tk.Label(marco, text="Días trabajados:").grid(
            row=4, column=0, sticky="e", padx=(10, 5), pady=4
        )
        self.dias = tk.Spinbox(
            marco,
            from_=Empleado.MINIMO_DIAS,
            to=Empleado.MAXIMO_DIAS,
            width=5,
            state="readonly",
        )
        self.dias.grid(row=4, column=1, sticky="w", padx=(5, 10), pady=4)

        for indice, campo in enumerate(self.CAMPOS_NUMERICOS, start=5):
            tk.Label(marco, text=f"{campo}:").grid(
                row=indice, column=0, sticky="e", padx=(10, 5), pady=4
            )
            entrada = tk.Entry(marco, width=25)
            entrada.grid(row=indice, column=1, sticky="w", padx=(5, 10), pady=4)
            self.entradas[campo] = entrada

        marco_botones = tk.Frame(self.ventana)
        marco_botones.grid(row=1, column=0, pady=(5, 15))
        tk.Button(
            marco_botones, text="Agregar", width=12, command=self.anadir_empleado
        ).pack(side="left", padx=5)
        tk.Button(
            marco_botones, text="Limpiar", width=12, command=self.limpiar_campos
        ).pack(side="left", padx=5)

        self.limpiar_campos()

    def anadir_empleado(self):
        nombre = self.entradas["Nombre"].get().strip()
        apellidos = self.entradas["Apellidos"].get().strip()
        if not nombre or not apellidos or not self.cargo.get() or not self.genero.get():
            messagebox.showerror(
                "Entrada no valida",
                "Ingrese el nombre, los apellidos, el cargo y el género.",
                parent=self.ventana,
            )
            return

        try:
            valores = [
                float(self.entradas[campo].get())
                for campo in self.CAMPOS_NUMERICOS
            ]
        except ValueError:
            messagebox.showerror(
                "Entrada no valida",
                "Ingrese un valor numérico en el salario, los ingresos, "
                "la salud y las pensiones.",
                parent=self.ventana,
            )
            return

        salario_dia, otros_ingresos, pagos_salud, aporte_pensiones = valores
        try:
            empleado = Empleado(
                nombre,
                apellidos,
                TipoCargo(self.cargo.get()),
                TipoGenero[self.genero.get()],
                salario_dia,
                int(self.dias.get()),
                otros_ingresos,
                pagos_salud,
                aporte_pensiones,
            )
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=self.ventana)
            return

        self.lista_empleados.agregar_empleado(empleado)
        self.al_agregar()
        messagebox.showinfo(
            "Empleado agregado",
            f"Se agregó a {nombre} {apellidos} a la nómina.",
            parent=self.ventana,
        )
        self.limpiar_campos()

    def limpiar_campos(self):
        for entrada in self.entradas.values():
            entrada.delete(0, "end")
        self.cargo.set("")
        self.genero.set("")
        self.dias.config(state="normal")
        self.dias.delete(0, "end")
        self.dias.insert(0, str(Empleado.MINIMO_DIAS))
        self.dias.config(state="readonly")
        self.entradas["Nombre"].focus_set()


class VentanaNomina:
    """Ventana no modal que muestra la nomina de los empleados en una tabla."""

    COLUMNAS = ["Nombre", "Apellidos", "Salario mensual"]

    def __init__(self, ventana_padre, lista_empleados):
        self.lista_empleados = lista_empleados
        self.ventana = tk.Toplevel(ventana_padre)
        self.ventana.title("Nómina")
        self.ventana.resizable(False, False)

        tk.Label(
            self.ventana,
            text="Nómina mensual de los empleados",
            font=("Arial", 12, "bold"),
        ).grid(row=0, column=0, columnspan=2, padx=15, pady=(15, 10))

        self.tabla = ttk.Treeview(
            self.ventana, columns=self.COLUMNAS, show="headings", height=8
        )
        for columna in self.COLUMNAS:
            self.tabla.heading(columna, text=columna)
            self.tabla.column(columna, width=150)
        self.tabla.column("Salario mensual", anchor="e")
        self.tabla.grid(row=1, column=0, columnspan=2, padx=15)

        # El total de la nomina se muestra en la parte inferior de la ventana
        self.total = tk.Label(self.ventana, font=("Arial", 10, "bold"))
        self.total.grid(
            row=2, column=0, columnspan=2, sticky="e", padx=15, pady=(10, 15)
        )

        self.actualizar()

    def actualizar(self):
        self.tabla.delete(*self.tabla.get_children())
        for empleado in self.lista_empleados.empleados:
            self.tabla.insert(
                "",
                "end",
                values=(
                    empleado.nombre,
                    empleado.apellidos,
                    formato_pesos(empleado.calcular_nomina()),
                ),
            )
        total = self.lista_empleados.calcular_total_nomina()
        self.total.config(text=f"Total nómina mensual: {formato_pesos(total)}")


class VentanaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Nómina")
        self.ventana.resizable(False, False)
        self.lista_empleados = ListaEmpleados()
        self.ventana_nomina = None

        barra_menu = tk.Menu(ventana)
        menu_opciones = tk.Menu(barra_menu, tearoff=0)
        menu_opciones.add_command(label="Agregar empleado", command=self.agregar_empleado)
        menu_opciones.add_command(label="Calcular nómina", command=self.calcular_nomina)
        menu_opciones.add_separator()
        menu_opciones.add_command(label="Guardar archivo", command=self.guardar_archivo)
        barra_menu.add_cascade(label="Opciones", menu=menu_opciones)
        ventana.config(menu=barra_menu)

        tk.Label(
            ventana,
            text="Cálculo de la nómina de empleados",
            font=("Arial", 12, "bold"),
        ).grid(row=0, column=0, padx=30, pady=(20, 5))
        tk.Label(ventana, text="Use el menú Opciones para comenzar.").grid(
            row=1, column=0, padx=30, pady=5
        )
        self.resultado = tk.Label(ventana, font=("Arial", 10))
        self.resultado.grid(row=2, column=0, padx=30, pady=(5, 20))
        self.mostrar_resumen()

    def agregar_empleado(self):
        VentanaAgregarEmpleado(self.ventana, self.lista_empleados, self.al_agregar)

    def al_agregar(self):
        self.mostrar_resumen()
        # Si la ventana de nomina esta abierta, la tabla se actualiza
        if self.ventana_nomina and self.ventana_nomina.ventana.winfo_exists():
            self.ventana_nomina.actualizar()

    def calcular_nomina(self):
        if self.ventana_nomina and self.ventana_nomina.ventana.winfo_exists():
            self.ventana_nomina.ventana.lift()
            return
        self.ventana_nomina = VentanaNomina(self.ventana, self.lista_empleados)

    def guardar_archivo(self):
        if not self.lista_empleados.empleados:
            messagebox.showwarning(
                "Sin empleados", "Agregue al menos un empleado antes de guardar."
            )
            return

        carpeta = filedialog.askdirectory(title="Seleccione la carpeta de destino")
        if not carpeta:
            return

        ruta = os.path.join(carpeta, "Nómina.txt")
        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                archivo.write(self.lista_empleados.convertir_texto())
        except OSError:
            messagebox.showerror("Error", "No se pudo guardar el archivo.")
            return
        messagebox.showinfo("Archivo guardado", f"Se guardó la nómina en:\n{ruta}")

    def mostrar_resumen(self):
        cantidad = len(self.lista_empleados.empleados)
        self.resultado.config(text=f"Empleados registrados: {cantidad}")


def main():
    ventana = tk.Tk()
    VentanaPrincipal(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
