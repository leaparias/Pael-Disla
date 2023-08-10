#este es el inicio del curso de python y veremos lo que podemos hacer.
### String ###

var_string = "string 1"
var_string1 = 'String 2'

print (len(var_string)+ len(var_string1))

print(var_string+" y "+ var_string1)

new_line_string = "este string hace \n un salto de linea"
print (new_line_string)

tab_string = "\t este string continene tabulaciones"
print (tab_string)

my_scape = '\t Este es un strin \n escapado'
print (my_scape)

#Formateo
name, surname, age = 'Pael','Disla', 28


print("My name is {} {} y mi edad es {}".format(name,surname,age))
print("My name is %s %s y mi edad es %d" %(name, surname,age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) ###Una manera no recomendable de hacerlo###
print(f"My name is {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

#Division   
languaje_slice = language[1:3]
print(languaje_slice)

languaje_slice = language[1]
print(languaje_slice)

languaje_slice = language[-2]
print(languaje_slice)

#Reverse

reverse_languaje = language[::-1]
print(reverse_languaje)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo