import random
"""
Función excFact
Se invoca con un raise excFact y tira un error
Entradas: exception, msg: exception siendo un ValueError, msg siendo string del texto que se mostrará
Salidas: exception(msg)
Restricciones: exception, msg : exception siendo un ValueError y msg sinedo tipo str
"""
def excFact(exception, msg):
    return exception(msg)


limite = 100
colores = ('Tanglewood', 'Opal Basil', 'Vocal Violet', 'Night Image', 'Lilac Murmur', 'Blue Sage', 'Harvest Moon', 
'Apple Gold', 'Sea Star', 'Lime Slice', 'Garden Room', 'Flamingo', 'Kona Orange', 'Metro Brown', 
'Cozy Peach', 'April Green', 'Safari Brown') 
lista=[x for x in colores]
for i in range(2):
    eliminar=random.choice(lista)
    lista.remove(eliminar)
diccionario={x:0 for x in lista}


""" 
Función procesarPedido
Guarda un pedido en el diccionario de pedidos
Entradas: color: nombre del color, cantidadGalones: cantidad de galones para hacer el pedido.
Salidas: N/A
Restricciones: N/A
"""
def procesarPedido (color, cantidadGalones):
    global diccionario, limite
    try:
        color = color.upper().strip() 
        encontrado = False

        for llaves in diccionario.keys():
            if llaves.upper().strip() == color:
                encontrado = True
                break
        
        if not(encontrado):
            print(excFact(ValueError, "El color no puede ser preparado."))
    except:
        print(excFact(ValueError, "El color no puede ser preparado."))
    
    try:
        cantidadGalones = int(cantidadGalones)
        sumaPedidos = 0
        for valor in diccionario.values():
            sumaPedidos += valor
    
        if cantidadGalones <= 0:
            print(excFact(ValueError, "El valor no es entero positivo."))
        elif cantidadGalones >= limite or cantidadGalones + sumaPedidos >= limite:
            print(excFact(ValueError, "El valor rebasa el máximo permitido de pedidos por semana."))
        else:
            for llave, valor in diccionario.items():
                if llave.upper().strip() == color:
                    llave = valor + cantidadGalones

    except:
        print(excFact(ValueError, "El valor no es entero positivo."))
    
def mostrar_colores_solicitados(diccionario):
    diccionario_final = {}
    for x in diccionario: 
        if diccionario[x] > 0:
            diccionario_final[x] = diccionario[x]
    return diccionario_final

#Menú
opcion = 1
while opcion != 0:
    print("0-Salir\n1-Solicitar un encargo")
    opcion = int(input())
    if opcion == 1:
        print("Colores disponibles:")
        for x in lista:
            print(x)
        print("Escriba el nombre del color a encargar")
        Color = input()
        try:
            Cantidad = int(input("Digite la cantidad que desea encargar\n"))
            procesarPedido(Color, Cantidad)
        except:
            print(excFact(ValueError,"El valor no es entero positivo."))
    elif opcion == 0:
        pedido = mostrar_colores_solicitados(diccionario)
        for llave, valor in pedido.items():
            print(llave, ":", valor)
        
        diccionario = dict()
    else:
        print("Esta no es una opci+on válida.")