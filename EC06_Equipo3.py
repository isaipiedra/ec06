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
lista = [x for x in colores]

"""
Función inciarSemana
Devuelve el diccionario con los colores disponibles en la semana
Entradas: lista, la lista de colores
Salidas: un diccionario con los pedidos iniciados en 0
"""
def inciarSemana(lista):
    listaAux = lista

    for i in range(2):
        eliminar = random.choice(listaAux)
        listaAux.remove(eliminar)
    return {x:0 for x in listaAux}


""" 
Función procesarPedido
Guarda un pedido en el diccionario de pedidos
Entradas: color: nombre del color, cantidadGalones: cantidad de galones para hacer el pedido.
Salidas:El mensaje correspondiente al estado de procesamiento del pedido
Restricciones: N/A
"""
def procesarPedido (color, cantidadGalones):
    global pedidos, limite
    try:
        encontrado = False

        for llaves in pedidos.keys():
            if llaves.upper().strip() == color:
                encontrado = True
                break
        
        if not(encontrado):
            return excFact(ValueError, "El color no puede ser preparado.")
    except:
        return excFact(ValueError, "El color no puede ser preparado.")
    
    try:
        cantidadGalones = int(cantidadGalones)
        sumaPedidos = 0
        for valor in pedidos.values():
            sumaPedidos += valor
    
        if cantidadGalones <= 0:
            return excFact(ValueError, "El valor no es entero positivo.")
        elif cantidadGalones >= limite or cantidadGalones + sumaPedidos >= limite:
            return excFact(ValueError, "El valor rebasa el máximo permitido de pedidos por semana.")
        else:
            for llave, valor in pedidos.items():
                if llave.upper().strip() == color:
                    pedidos[llave] = valor + cantidadGalones

            return "Pedido procesado."

    except:
        return excFact(ValueError, "El valor no es entero positivo.")

""" 
Función mostrar_colores_solicitados
Retorna un diccionario con los pedidos diferentes a 0
Entradas: diccionario: el diccionario de todos los pedidos.
Salidas: N/A
Restricciones: N/A
"""
def mostrar_colores_solicitados(diccionario):
    diccionario={x:diccionario[x] for x in diccionario if diccionario[x]>0}
    
    return diccionario

pedidos = inciarSemana(lista)

#Menú
opcion = "1"
while opcion != "X":
    print("-------- BIENVENIDOS AL MENU DE PEDIDOS --------")
    print("1-Solicitar un encargo\n0-Mostrar pedidos y limpiar semana\nX-Salir")
    opcion = input().upper()
    if opcion == "1":
        print("----------- Colores disponibles -----------")

        for coloresDisponibles in pedidos.keys():
            print(coloresDisponibles)

        print("-------------------------------------------")

        print("Escriba el nombre del color a encargar:")
        color = input()
        try:
            cantidad = int(input("Digite la cantidad que desea encargar:"))
            print(procesarPedido(color.upper().strip(), cantidad))
        except:
            print(excFact(ValueError,"El valor no es entero positivo."))
    elif opcion == "0":
        print("------ PEDIDOS DE LA SEMANA ------")
        pedido = mostrar_colores_solicitados(pedidos)
        for llave, valor in pedido.items():
            print(llave, ":", valor)

        print("------ FINAL DE LA SEMANA ------\n")
        
        
        pedidos = dict() #limpiar el diccionario
        lista = [x for x in colores]
        pedidos = inciarSemana(lista) #vuelve a iniciar la semana
    elif opcion == "X":
        print("Terminando, gracias por usar.")
    else:
        print("Esta no es una opción válida.")