print("CALCULADORA BASICA EN PYTHON")

operacion=int(input("Por favor seleccione una Operacion a realizar: \n1. Suma \n2. Resta \n3. Multiplicacion \n4. Divicion\n" ))


if (operacion==1):
    num_1=int(input("Ingrese el primer numero: "))
    num_2=int(input("Ingrese el segundo numero: "))
    print("La suma es: ",num_1+num_2)
elif (operacion==2):
    num_1=int(input("Ingrese el primer numero: "))
    num_2=int(input("Ingrese el segundo numero: "))
    print("La Resta es: ",num_1-num_2)
elif (operacion==3):
    num_1=int(input("Ingrese el primer numero: "))
    num_2=int(input("Ingrese el segundo numero: "))
    print("El producto es: ",num_1*num_2)
elif (operacion==4):
    num_1=int(input("Ingrese el primer numero: "))
    num_2=int(input("Ingrese el segundo numero: "))
    print("El cociente es : ",num_1/num_2)
else:
    print("Esa opcion no existe")
    print("Vuelve a intentarlo")

