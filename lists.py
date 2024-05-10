def remove_elemets(lista):
    if len(lista) >= 6:
          del lista[5]
          del lista[4]
          del lista [0]
          print (lista)
    elif len(lista) >=5:
        del lista[4]
        del lista[0]
        print (lista)
    else:
       del lista[0]
       print (lista)

lista1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
remove_elemets(lista1)

