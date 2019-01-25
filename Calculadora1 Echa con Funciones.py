#suma, resta, multiplicar y dividir
#Son las funciones
def suma(num1, num2):
    return num1 + num2
def resta(num1, num2):
    return num1 - num2
def multiplicar(num1, num2):
    return num1 * num2
def dividir(num1, num2):
    return num1 / num2

print("Por favor selecciona una operacion \n" \
      "1. Suma\n" \
       "2. Resta\n" \
       "3. Multiplicacion\n" \
       "4. Division\n")
opcion=int(input("Selecciona una Opcion: "))
num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa un segundo numero: "))

if opcion==1:
    print (num1, '+', num2, '=',
           suma(num1, num2))
elif opcion==2:
    print(num1, '-', num2, '=',
          resta(num1, num2))
elif opcion==3:
    print(num1, '*',num2, '=',
          multiplicar(num1, num2))
elif opcion==4:
    print(num1, '/', num2, '=',
          dividir(num1, num2))
else:
    print("Esa opcion no existe")

                        
           
