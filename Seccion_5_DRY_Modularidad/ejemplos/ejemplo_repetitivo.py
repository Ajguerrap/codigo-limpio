# Ejemplo de código repetitivo

def calcular_descuento_estudiante(precio):
    descuento = precio * 0.15
    precio_final = precio - descuento
    print(f"Descuento aplicado: ${descuento}")
    print(f"Precio final: ${precio_final}")
    return precio_final

def calcular_descuento_senior(precio):
    descuento = precio * 0.20
    precio_final = precio - descuento
    print(f"Descuento aplicado: ${descuento}")
    print(f"Precio final: ${precio_final}")
    return precio_final
