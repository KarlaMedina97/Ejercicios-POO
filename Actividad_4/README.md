# Actividad 4

La Actividad 4 contiene cinco ejercicios de manejo de excepciones y lectura de
archivos, tomados del libro *Ejercicios de Programacion Orientada a Objetos con
Java y UML* (Leonardo Bermon Angarita), implementados en Python con interfaz
grafica en Tkinter.

## Ejercicios

| Ejercicio | Archivo | Contenido |
| --- | --- | --- |
| 4.1 | `Ejercicio1.py` | Ejecucion de dos bloques `try` que lanzan una excepcion aritmetica y una excepcion general, mostrando que se imprime en pantalla. |
| 4.2 | `Ejercicio2.py` | Registro de un vendedor con nombre, apellidos y edad, verificando que la edad sea mayor de 18 y no supere 120. |
| 4.3 | `Ejercicio3.py` | Calculo del logaritmo neperiano y la raiz cuadrada de un valor, con excepciones para valores no validos. |
| 4.4 | `Ejercicio4.py` | Conformacion de un equipo para una maraton de programacion de 2 a 3 integrantes, validando nombres y apellidos. |
| 4.5 | `Ejercicio5.py` | Lectura de un archivo de texto mediante un flujo de bytes y visualizacion de su contenido. |

## Ejecucion

Ejecuta el archivo correspondiente desde esta carpeta:

```bash
python Ejercicio1.py
python Ejercicio2.py
python Ejercicio3.py
python Ejercicio4.py
python Ejercicio5.py
```

Las excepciones de Java se representan con sus equivalentes en Python:
`ArithmeticException` con `ArithmeticError`, `IllegalArgumentException` con
`ValueError` e `IOException` con `OSError`. En el ejercicio 4.5 se lee por
defecto el archivo `prueba.txt` de esta carpeta; con el boton "Examinar..." se
puede seleccionar otro archivo `.txt`.