def remove_elemets(list):
    if list == []:
        return list
    del list_to_remove_elements[0]
    
if len(list_to_remove_elements) > 3:
    del list_to_remove_elements[3]
else:
    return list_to_remove_elements

if len(list_to_remove_elements) > 3:
    del list_to_remove_elements[3]
        return list_to_remove_elements
else:
    return list_to_remove_elements

list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_elements(list))

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
