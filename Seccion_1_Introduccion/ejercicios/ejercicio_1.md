# Ejercicio 1: Discusión rápida

**Pregunta:** ¿Cuál de los dos códigos entenderías mejor dentro de 6 meses? ¿Por qué?

## Ejemplo práctico 1

```python
# Código poco claro
def fn(x, y):
    return x * y

resultado = fn(3, 4)
print(resultado)
```

*¿Cuál es más fácil de entender y por qué?*

## Ejemplo práctico 2

```python
# Código poco claro
def a(b, c):
    return b + c

x = 5
y = 7
z = a(x, y)
print(z)
```

*¿Qué ventajas tiene el segundo ejemplo sobre el primero?*

## Ejercicio adicional

**Pregunta:** ¿Qué problemas podrías encontrar si tu equipo no sigue principios de código limpio?

### Ejemplo práctico de problema

```python
# Código sin principios de código limpio
def p(x):
    if x > 10:
        return x * 2
    else:
        return x + 2

# ¿Qué hace la función p? ¿Cómo podrías mejorarla?
```
