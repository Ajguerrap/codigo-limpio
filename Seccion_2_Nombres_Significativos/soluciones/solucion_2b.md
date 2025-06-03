# Solución sugerida - Ejercicio 2b

```python
def sumar_precios_productos(productos):
    total = 0
    for producto in productos:
        if producto['categoria'] == 'A':
            total += producto['precio'] * 0.9
        else:
            total += producto['precio']
    return total

productos = [
    {'name': 'laptop', 'precio': 1000, 'categoria': 'A'},
    {'name': 'mouse', 'precio': 20, 'categoria': 'B'}
]
total = sumar_precios_productos(productos)
```
