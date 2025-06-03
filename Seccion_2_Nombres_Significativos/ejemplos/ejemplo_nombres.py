# Ejemplo de malos nombres

def calc(x, y, z):
    if x > 0:
        if z == 1:
            return x * y * 0.1
        else:
            return x * y * 0.05
    return 0

# Ejemplo de buenos nombres

def calcular_descuento(precio_base, cantidad, es_cliente_premium):
    if precio_base <= 0:
        return 0
    tasa_descuento = 0.1 if es_cliente_premium else 0.05
    return precio_base * cantidad * tasa_descuento
