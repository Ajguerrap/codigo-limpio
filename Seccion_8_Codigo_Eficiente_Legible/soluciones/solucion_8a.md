# Solución sugerida - Ejercicio 8a

```python
def encontrar_duplicados(lista):
    vistos = set()
    duplicados = set()
    for elemento in lista:
        if elemento in vistos:
            duplicados.add(elemento)
        else:
            vistos.add(elemento)
    return list(duplicados)
```

Solución adicional:

```python
def calcular_estadisticas(numeros):
    suma = sum(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    promedio = suma / len(numeros)
    return suma, promedio, minimo, maximo
```
