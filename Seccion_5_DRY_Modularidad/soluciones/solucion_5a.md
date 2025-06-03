# Solución sugerida - Ejercicio 5a

```python
def notificar(usuario, mensaje, canal):
    if canal == 'email':
        print(f"Enviando email a {usuario}: {mensaje}")
    elif canal == 'sms':
        print(f"Enviando SMS a {usuario}: {mensaje}")
    elif canal == 'push':
        print(f"Enviando notificación push a {usuario}: {mensaje}")
    else:
        print(f"Canal desconocido para {usuario}: {mensaje}")
```

Solución adicional:

```python
def calcular_area(figura, *args):
    if figura == 'cuadrado':
        return args[0] * args[0]
    elif figura == 'rectangulo':
        return args[0] * args[1]
    elif figura == 'triangulo':
        return (args[0] * args[1]) / 2
    else:
        return None
```
