# Solución sugerida - Ejercicio 4a

```python
def calcular_promedio_mejorado(numeros):
    if not numeros:
        print("Error: lista vacía.")
        return None
    try:
        suma = sum(numeros)
        promedio = suma / len(numeros)
        return promedio
    except TypeError:
        print("Error: la lista debe contener solo números.")
        return None
```

Solución adicional:

```python
def dividir_seguro(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        return None
    except TypeError:
        print("Error: Los argumentos deben ser números.")
        return None
```
