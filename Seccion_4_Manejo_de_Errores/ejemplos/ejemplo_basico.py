# Ejemplo básico de manejo de errores

def dividir(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        return None
