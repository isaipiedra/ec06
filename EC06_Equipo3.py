colores=('Tanglewood', 'Opal Basil', 'Vocal Violet', 'Night Image', 'Lilac Murmur', 'Blue Sage', 'Harvest Moon', 
'Apple Gold', 'Sea Star', 'Lime Slice', 'Garden Room', 'Flamingo', 'Kona Orange', 'Metro Brown', 
'Cozy Peach', 'April Green', 'Safari Brown') 
lista=[x for x in colores]
print(lista)
for i in range(2):
    eliminar=random.choice(lista)
    lista.remove(eliminar)
print(lista)

diccionario={x:0 for x in lista}
print(diccionario)
limite=100
for x in diccionario:
    cantidad=int(input(f'Cuantos galones desea para {x}'))
    cantidad+=cantidad
    if cantidad>limite:
        print('ya no se pueden más galones')
        break
    diccionario[x]=cantidad

print(diccionario)
