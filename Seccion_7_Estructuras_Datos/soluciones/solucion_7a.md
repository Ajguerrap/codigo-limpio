# Solución sugerida - Ejercicio 7a

1. Carrito de compras: Lista (`list`), porque permite productos repetidos y mantiene el orden.
2. Votación: Set (`set`), para garantizar unicidad de usuarios.
3. Configuración: Diccionario (`dict`), para mapeo clave-valor.
4. Lista de tareas: Lista (`list`), para mantener el orden de inserción.
5. Catálogo: Diccionario (`dict`), para búsqueda rápida por nombre.

Solución adicional:

```python
def contar_usuarios_repetidos(lista_usuarios):
    return len(lista_usuarios) - len(set(lista_usuarios))
```
