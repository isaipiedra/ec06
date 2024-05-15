import random
limite=100
colores=('Tanglewood', 'Opal Basil', 'Vocal Violet', 'Night Image', 'Lilac Murmur', 'Blue Sage', 'Harvest Moon', 
'Apple Gold', 'Sea Star', 'Lime Slice', 'Garden Room', 'Flamingo', 'Kona Orange', 'Metro Brown', 
'Cozy Peach', 'April Green', 'Safari Brown') 
lista=[x for x in colores]
for i in range(2):
    eliminar=random.choice(lista)
    lista.remove(eliminar)
diccionario={x:0 for x in lista}


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
        if Color in lista:
            Cantidad = int(input("Digite la cantidad que desea encargar\n"))
        else:
            print("El color digitado no está disponible")
