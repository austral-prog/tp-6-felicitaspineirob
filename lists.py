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

def add_elemets(lista):
    lista.insert(0,'Pink')
    lista.append('Yellow')
    print(lista)
lista2= ['Red', 'Green', 'White', 'Black']
add_elemets(lista2)

def is_empty(lista):
    if len(lista) == 0:
        return "Esta vacia"
    else:
        return "No esta vacia"
lista3= [ ]
print(is_empty(lista3))

def check_list(lista1, lista2):
    if len(lista1)<3 or len(lista2)<3:
        return False
    else:
        return lista1[2] ==lista2[2]
lista1= ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
lista2= ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
result= check_list(lista1, lista2)
print(result)
lista3= ['Black', 'Pink', 'Green', 'White']
lista4= ['Red', 'Green', 'Yellow', 'Black', 'Pink']
result2= check_list(lista3, lista4)
print(result2)
