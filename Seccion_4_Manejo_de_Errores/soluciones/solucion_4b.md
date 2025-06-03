# Solución sugerida - Ejercicio 4b

```python
def obtener_edad_usuario_mejorado():
    while True:
        edad = input("Ingresa tu edad: ")
        try:
            edad_numero = int(edad)
            if edad_numero < 0:
                print("Error: la edad no puede ser negativa.")
                continue
            if edad_numero >= 18:
                print("Eres mayor de edad")
            else:
                print("Eres menor de edad")
            return edad_numero
        except ValueError:
            print("Error: Por favor ingresa un número válido.")
```
