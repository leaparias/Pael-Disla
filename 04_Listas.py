
### Lists  ###


# Definición

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 61, 19, 23, 56 ,89 , 0 ]

print(my_list)
print(len(my_list))

my_other_list = [23, 1.80, 'PDA']

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print (my_other_list[0])
print (my_other_list[1])
print (my_other_list[-1])
print (my_other_list[-3])
print(my_list.count(35))
#print (my_other_list[-4])Error por falta de esos valores
#print (my_other_list[3]) Error por falta de esos valores

print(my_other_list.index("PDA"))

age, height, name = my_other_list
print(name)

name, height, age = my_other_list[2], my_other_list[1], my_other_list[0]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("DISLA")#inserta
print(my_other_list)

my_other_list.insert(1, "Negro")#inserta en donde le indicamos
print(my_other_list)

my_other_list[1] = "Rojo"#cambia el valor que indicquemos
print(my_other_list)

my_other_list.remove("Rojo")#elimina el valor mensionado
print(my_other_list)

my_list.remove(19)#elimina el valor mensionado
print(my_list)

print(my_list.pop())#saca el ultimo valor de la lista
print(my_list)

my_pop_element = my_list.pop(2)#saca el valor espciicado y lo guarda en esa vasriable
print(my_pop_element)
print(my_list)

del my_list[2] #Elimina un valor o una lista en especifico
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()#vacia o limpia una lista
print(my_list)
print(my_new_list)

my_new_list.reverse()#me voltea los parametros
print(my_new_list)

my_new_list.sort()#ordena los parametros de la lista
print(my_new_list)

my_list = 'hola python'
print(my_list)
print(type(my_list))