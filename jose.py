#presentar el registro de los pedidos y limpiar el diccionario; se puede usar cualquiera de las dos opciones, 
#sin embargo, la segunda no es capaz de limpiar el diccionario

'''def mostrar_colores_solicitados(diccionario):
    diccionario_final = {}
    for x in diccionario: 
        if diccionario[x] > 0:
            diccionario_final[x] = diccionario[x]
    diccionario.clear()
    return diccionario_final
'''
def mostrar_colores_solicitados(diccionario):
    diccionario={x:diccionario[x] for x in diccionario if diccionario[x]>0}
    return diccionario
#recordar limpiar el diccionario en la página principal después de llamar a la función
