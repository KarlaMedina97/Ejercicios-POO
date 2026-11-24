# Actividad 5

La Actividad 5 contiene dos ejercicios de interfaz grafica de usuario, tomados
del libro *Ejercicios de Programacion Orientada a Objetos con Java y UML*
(Leonardo Bermon Angarita), implementados en Python con Tkinter.

## Ejercicios

| Ejercicio | Archivo | Contenido |
| --- | --- | --- |
| 8.4 | `Ejercicio1.py` | Cuadros de dialogo: calculo de la nomina de los empleados de una empresa con un menu para agregar empleados, ver la nomina en una tabla y guardarla en el archivo `Nómina.txt`. |
| 8.5 | `Ejercicio2.py` | Gestion de contenidos: registro del ingreso y la salida de los huespedes de un hotel de diez habitaciones, organizando las ventanas con distintos administradores de diseno. |

## Ejecucion

Ejecuta el archivo correspondiente desde esta carpeta:

```bash
python Ejercicio1.py
python Ejercicio2.py
```

En el ejercicio 8.4 la ventana para agregar un empleado es un cuadro de dialogo
modal (`transient` y `grab_set`), mientras que la ventana de la nomina no es
modal y se actualiza al agregar empleados. El salario mensual se calcula como
`(dias trabajados * salario por dia) + otros ingresos - pagos por salud - aporte pensiones`.

En el ejercicio 8.5 las habitaciones 1 a 5 cuestan $120.000 por dia y las
habitaciones 6 a 10 cuestan $160.000 por dia. Las fechas se ingresan con el
formato `AAAA-MM-DD`. Los layouts de Java se representan con sus equivalentes
en Tkinter: `GridLayout` con `grid` en la cuadricula de habitaciones,
`BorderLayout` con `pack` por regiones en la ventana principal, `FlowLayout`
con `pack(side="left")` en las filas de botones y `GridBagLayout` con `grid` y
`sticky` en los formularios.
