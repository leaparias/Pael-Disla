### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inciialmente es un dicionario

my_other_set = {"Pael", "Disla", 23}
print(type(my_other_set)) #Ahora es un Set

print(len(my_other_set))

# Insercion

my_other_set.add("MoureDev")

print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("MoureDev")  # Un set no admite repetidos

print(my_other_set)

# Busqueda

print("Pael" in my_other_set)#busca si existe o no
print("Paela" in my_other_set)

#eliminar

my_other_set.remove("MoureDev")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set