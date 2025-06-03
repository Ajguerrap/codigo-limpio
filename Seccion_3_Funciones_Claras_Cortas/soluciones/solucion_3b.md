# Solución sugerida - Ejercicio 3b

```python
from collections import defaultdict

def calcular_total_ventas(ventas):
    return sum(v['monto'] for v in ventas)

def agrupar_ventas_por_mes(ventas):
    ventas_mes = defaultdict(float)
    for v in ventas:
        ventas_mes[v['fecha'].month] += v['monto']
    return dict(ventas_mes)

def producto_mas_vendido(ventas):
    cantidades = defaultdict(int)
    for v in ventas:
        cantidades[v['producto']] += v['cantidad']
    if not cantidades:
        return None
    return max(cantidades, key=cantidades.get)

def mostrar_resumen(total, ventas_por_mes, top_producto):
    print(f"Total de ventas: ${total}")
    print(f"Producto más vendido: {top_producto}")
    print(f"Ventas por mes: {ventas_por_mes}")

def analizar_ventas(ventas):
    total = calcular_total_ventas(ventas)
    ventas_mes = agrupar_ventas_por_mes(ventas)
    top = producto_mas_vendido(ventas)
    mostrar_resumen(total, ventas_mes, top)
    return {
        'total': total,
        'por_mes': ventas_mes,
        'top_producto': top
    }
```
