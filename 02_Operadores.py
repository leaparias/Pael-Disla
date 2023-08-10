#este es el inicio del curso de python y veremos lo que podemos hacer.
### operadores ###

print (3 + 2)
print (2 - 1)
print (3 * 9)
print (8 / 2)
print (10 % 1)
print (7 // 5)
print (2 ** 3)

#podemos hacer calculos complejos
print(2 ** 3 + 3 - 7 / 1 // 4)

#podemos usar operaciones de concatenar y usar valores para afectar str
# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))

# Operaciones mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))

# en esta operacion mixta usamos variables y cambio de valores en ella
my_float = 2.5 * 2
print("Hola " * int(my_float))

###Operadores Comparativos###

print (5 < 6)
print (5 > 6)
print (5 <= 6)
print (5 >= 6)
print (6 == 6)
print (5 != 6)

# Operaciones Comparativos con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

###Operadores Logicos###

print (5 < 6 and "Hola" > "Python")
print (5 < 6 or "Hola" > "Python")
print ( not "Hola" > "Python")
