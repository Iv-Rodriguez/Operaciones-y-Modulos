import Operaciones

print("Calculadora Basica")
print("Suma = 1, Resta = 2, Mult = 3 y Div = 4")

operacion = input("Que operacion desea realizar? ")

if operacion == "1":
    print ("Ha elegido suma")
    Operaciones.suma()
elif operacion == "2":
    print ("Ha elegido resta")
    Operaciones.resta()
elif operacion == "3":
    print ("Ha elegido multiplicacion")
    Operaciones.mult()
elif operacion == "4":
    print ("Ha elegido division")
    Operaciones.div()
else:
    print("Hasta pronto!")