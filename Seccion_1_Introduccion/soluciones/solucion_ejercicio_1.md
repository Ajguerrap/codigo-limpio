# Solución sugerida - Ejercicio 1

## Ejemplo práctico 1 (código claro)

```python
def multiplicar(numero1, numero2):
    return numero1 * numero2

producto = multiplicar(3, 4)
print(producto)
```

El código claro usa nombres descriptivos y muestra la intención de la función.

## Ejemplo práctico 2 (código claro)

```python
def sumar(primer_numero, segundo_numero):
    return primer_numero + segundo_numero

resultado = sumar(5, 7)
print(resultado)
```

El segundo ejemplo es más fácil de entender porque los nombres explican el propósito de la función y las variables.

## Solución adicional

Si no se siguen principios de código limpio, el código se vuelve difícil de mantener, propenso a errores y costoso de modificar.

### Ejemplo mejorado

```python
def procesar_numero(numero):
    """Multiplica por 2 si es mayor a 10, suma 2 si no."""
    if numero > 10:
        return numero * 2
    else:
        return numero + 2
```
