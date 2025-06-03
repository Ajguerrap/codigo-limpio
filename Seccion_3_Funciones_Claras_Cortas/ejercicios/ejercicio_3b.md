# Ejercicio 3b: Refactorizar función compleja de ventas

```python
def analizar_ventas(ventas):
    total_ventas = 0
    ventas_por_mes = {}
    producto_mas_vendido = None
    max_cantidad = 0
    for venta in ventas:
        total_ventas += venta['monto']
        mes = venta['fecha'].month
        if mes not in ventas_por_mes:
            ventas_por_mes[mes] = 0
        ventas_por_mes[mes] += venta['monto']
        if venta['cantidad'] > max_cantidad:
            max_cantidad = venta['cantidad']
            producto_mas_vendido = venta['producto']
    print(f"Total de ventas: ${total_ventas}")
    print(f"Producto más vendido: {producto_mas_vendido}")
    print(f"Ventas por mes: {ventas_por_mes}")
    return {
        'total': total_ventas,
        'por_mes': ventas_por_mes,
        'top_producto': producto_mas_vendido
    }
```

*Objetivo:* Refactoriza la función para separar responsabilidades y mejorar la claridad.
