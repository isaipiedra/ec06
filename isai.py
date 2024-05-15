#procesar pedido
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
            raise excFact(ValueError, "El color no puede ser preparado.")
    except:
        raise excFact(ValueError, "El color no puede ser preparado.")
    
    try:
        cantidadGalones = int(cantidadGalones)
        sumaPedidos = 0
        for valor in diccionario.values():
            sumaPedidos += valor

        if cantidadGalones <= 0:
            raise excFact(ValueError, "El valor no es entero positivo.")
        elif cantidadGalones >= limite or cantidadGalones >= sumaPedidos:
            raise excFact(ValueError, "El valor rebasa el máximo permitido de pedidos por semana.")
        else:
            for llave, valor in diccionario.items():
                if llave.upper().strip() == color:
                    llave = valor + cantidadGalones

    except:
        raise excFact(ValueError, "El valor no es entero positivo.")