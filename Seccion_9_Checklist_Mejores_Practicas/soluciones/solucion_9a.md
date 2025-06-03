# Solución sugerida - Ejercicio 9a

Mejoras posibles:

1. Usar nombres más descriptivos para la función y variables.
2. Separar la lógica de suma y resta en funciones distintas.
3. Añadir manejo de errores para datos no numéricos.
4. Incluir docstring explicativo.
5. Añadir pruebas automatizadas para validar el comportamiento.

Código refactorizado:

```python
def calcular_resultado(datos):
    """
    Calcula la suma de los positivos y resta los negativos de una lista de números.
    Args:
        datos (list of int/float): Lista de números.
    Returns:
        int/float: Resultado final.
    """
    resultado = 0
    for valor in datos:
        if valor > 0:
            resultado += valor
        else:
            resultado -= valor
    print("Resultado:", resultado)
    return resultado
```
