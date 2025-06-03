# Ejercicio 4b: Mejorar función que pide edad

```python
def obtener_edad_usuario():
    edad = input("Ingresa tu edad: ")
    edad_numero = int(edad)
    if edad_numero >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    return edad_numero
```

*Objetivo:* Mejorar la función con manejo de errores y validación.
