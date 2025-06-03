# Solución sugerida - Ejercicio 3a

```python
def limpiar_texto(texto):
    return texto.strip().lower()

def contar_palabras(texto):
    return len(texto.split())

def mostrar_cantidad_palabras(cantidad):
    print(f"El texto tiene {cantidad} palabras.")

def manejar_texto(texto):
    texto_limpio = limpiar_texto(texto)
    cantidad = contar_palabras(texto_limpio)
    mostrar_cantidad_palabras(cantidad)
    return cantidad
```

Solución adicional:

```python
def obtener_positivos(lista):
    return [x for x in lista if x > 0]

def obtener_negativos(lista):
    return [x for x in lista if x < 0]

def mostrar_cantidad(positivos, negativos):
    print(f"Positivos: {len(positivos)} | Negativos: {len(negativos)}")

def analizar_lista(lista):
    positivos = obtener_positivos(lista)
    negativos = obtener_negativos(lista)
    mostrar_cantidad(positivos, negativos)
    return positivos, negativos
```
