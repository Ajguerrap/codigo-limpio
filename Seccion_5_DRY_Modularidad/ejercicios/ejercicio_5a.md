# Ejercicio 5a: Refactorizar funciones repetidas de notificaciones

```python
def notificar_por_email(usuario, mensaje):
    print(f"Enviando email a {usuario}: {mensaje}")

def notificar_por_sms(usuario, mensaje):
    print(f"Enviando SMS a {usuario}: {mensaje}")

def notificar_por_push(usuario, mensaje):
    print(f"Enviando notificación push a {usuario}: {mensaje}")
```

*Objetivo:* Extraer una función general para notificaciones.

## Ejercicio adicional

Refactoriza el siguiente código para aplicar DRY y modularidad:

```python
def calcular_area_cuadrado(lado):
    return lado * lado

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2
```
