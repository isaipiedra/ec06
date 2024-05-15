#presentar el registro de los pedidos y limpiar el diccionario

def mostrar_colores_solicitados(diccionario):
    diccionario_final = {}
    for x in diccionario: 
        if diccionario[x] > 0:
            diccionario_final[x] = diccionario[x]
    return diccionario_final
