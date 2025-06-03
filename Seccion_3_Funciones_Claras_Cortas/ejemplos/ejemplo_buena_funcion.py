# Ejemplo de funciones separadas y claras

def filtrar_positivos(lista):
    return [x for x in lista if x > 0]

def sumar_lista(lista):
    return sum(lista)

def mostrar_resultado(valor):
    print("La suma es:", valor)

numeros = [1, -2, 3, 4, -5]
positivos = filtrar_positivos(numeros)
resultado = sumar_lista(positivos)
mostrar_resultado(resultado)
