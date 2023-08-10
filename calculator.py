#prueba de como hacer una calculadora aritmetica

n: int = input('dime un numero ')
n1: int = input('dime otro numero ')

print ('Escribe que tipo de operacion prefieres  de las sig: \n + \n - \n * \n /')
operacion = input('')

if (operacion == '+'):
    suma = int(n + n1) 
  
elif (operacion == '-'):
    suma = int(n - n1) 
  
elif(operacion == '*'):
    suma = int(n * n1) 
  
else:
    suma = int(n / n1)
    # comment: 
print (n, operacion, n1,'=', suma)


