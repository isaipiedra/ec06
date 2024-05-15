"""
Función excFact
Se invoca con un raise excFact y tira un error
Entradas: exception, msg: exception siendo un ValueError, msg siendo string del texto que se mostrará
Salidas: exception(msg)
Restricciones: exception, msg : exception siendo un ValueError y msg sinedo tipo str
"""
def excFact(exception, msg):
    return exception(msg)
