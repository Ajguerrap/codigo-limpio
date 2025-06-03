# Ejercicio 8a: Optimizar función de duplicados

Optimiza la siguiente función para que sea más eficiente y mantenga la legibilidad:

```python
def encontrar_duplicados(lista):
    duplicados = []
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados
```

## Ejercicio adicional

Optimiza la siguiente función para calcular estadísticas básicas:

```python
def calcular_estadisticas(numeros):
    suma = 0
    minimo = numeros[0]
    maximo = numeros[0]
    for n in numeros:
        suma += n
        if n < minimo:
            minimo = n
        if n > maximo:
            maximo = n
    promedio = suma / len(numeros)
    return suma, promedio, minimo, maximo
```
