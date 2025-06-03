# Ejercicio 2b: Mejorar nombres en función con diccionarios

```python
def calc_p(items):
    t = 0
    for i in items:
        if i['cat'] == 'A':
            t += i['pr'] * 0.9
        else:
            t += i['pr']
    return t

products = [
    {'name': 'laptop', 'pr': 1000, 'cat': 'A'},
    {'name': 'mouse', 'pr': 20, 'cat': 'B'}
]
total = calc_p(products)
```

*Objetivo:* Cambia los nombres de variables y claves para mayor claridad.
