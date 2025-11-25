def suma ():
    a = float(input("Digite su primer numero: "))
    b = float (input("Digite su segundo numero: "))

    total = a+b

    print (f"La suma total es {total}")

def resta ():
    a = float(input("Digite su primer numero: "))
    b = float (input("Digite su segundo numero: "))

    total = a-b

    print (f"La resta total es {total}")

def mult ():
    a = float(input("Digite su primer multiplo: "))
    b = float (input("Digite su segundo multiplo: "))

    total = a*b

    print (f"La multiplicacion es {total}")

def div ():
    a = float(input("Digite su divisor: "))
    b = float (input("Digite su segundo cociente: "))

    while b==0:
        print("No se puede dividir entre 0...")
        b = float(input("Introduzca un nuevo cociente: "))

    total = a/b
    print (f"El total es {total}")
    


    