# Ejemplo de función que hace demasiado

def procesar_lista(lista):
    lista_filtrada = []
    for elemento in lista:
        if elemento > 0:
            lista_filtrada.append(elemento)
    suma = 0
    for numero in lista_filtrada:
        suma += numero
    print("La suma es:", suma)
    return suma
