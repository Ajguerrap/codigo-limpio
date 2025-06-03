# Ejemplo de código DRY

def calcular_descuento(precio, porcentaje):
    descuento = precio * porcentaje
    precio_final = precio - descuento
    print(f"Descuento aplicado: ${descuento}")
    print(f"Precio final: ${precio_final}")
    return precio_final
