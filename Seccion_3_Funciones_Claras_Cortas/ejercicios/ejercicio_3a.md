# Ejercicio 3a: Dividir función en funciones claras

```python
def manejar_texto(texto):
    texto_limpio = texto.strip().lower()
    palabras = texto_limpio.split()
    cantidad_palabras = len(palabras)
    print(f"El texto tiene {cantidad_palabras} palabras.")
    return cantidad_palabras
```

*Objetivo:* Refactoriza la función para separar responsabilidades.

## Ejercicio adicional

Divide la siguiente función en funciones más pequeñas y claras:

```python
def analizar_lista(lista):
    positivos = [x for x in lista if x > 0]
    negativos = [x for x in lista if x < 0]
    print(f"Positivos: {len(positivos)} | Negativos: {len(negativos)}")
    return positivos, negativos
```
