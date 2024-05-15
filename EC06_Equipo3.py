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


