# Ejercicio 7a: Elegir estructura adecuada

Para cada caso, elige la estructura de datos más apropiada y justifica tu elección:

1. Carrito de compras donde puede haber productos repetidos.
2. Votación donde cada usuario puede votar solo una vez.
3. Configuración de aplicación con parámetros clave-valor.
4. Lista de tareas que debe mantener el orden de inserción.
5. Catálogo de productos con búsqueda rápida por nombre.

## Ejercicio adicional

Refactoriza la siguiente función para usar la estructura de datos más eficiente:

```python
def contar_usuarios_repetidos(lista_usuarios):
    conteo = 0
    for i in range(len(lista_usuarios)):
        for j in range(i+1, len(lista_usuarios)):
            if lista_usuarios[i] == lista_usuarios[j]:
                conteo += 1
    return conteo
```
