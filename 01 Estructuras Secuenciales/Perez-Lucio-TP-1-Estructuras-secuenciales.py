#TP N°1 - Estructuras secuenciales - Programacion I - UTN
# Nombre del alumno: Pérez Lucio Gabriel
#-------------------------------------------------------------------------
#EJERCICIOS:

#  1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”:
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

import math
radio = float(input("Ingrese el radio de un círculo: "))
pi = math.pi
perimetro = 2*radio*pi
area = pi*(radio**2)
print(f"El área del círculo es: {round(area,2)}cm2 y su perimetro es: {round(perimetro,2)}cm")


# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

seg = int(input("Ingrese la cantidad de segundos para convertir a horas: "))
horas = (seg/60)/60
print(f"Respuesta: {seg} segundos equivalen a {round(horas,2)} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

num = int(input("Ingrese un número entero: "))
print(f"La tabla del {num} es: ")
print(f"{num}*1 = {num*1}")
print(f"{num}*2 = {num*2}")
print(f"{num}*3 = {num*3}")
print(f"{num}*4 = {num*4}")
print(f"{num}*5 = {num*5}")
print(f"{num}*6 = {num*6}")
print(f"{num}*7 = {num*7}")
print(f"{num}*8 = {num*8}")
print(f"{num}*9 = {num*9}")
print(f"{num}*10 = {num*10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese un número entero distinto de 0: "))
num2 = int(input("Ingrese otro número entero distinto de 0: "))
print(f"{num1}+{num2}={num1+num2}")
print(f"{num1}/{num2}={num1/num2}")
print(f"{num1}*{num2}={num1*num2}")
print(f"{num1}-{num2}={num1-num2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso/(altura**2)
print(f"Su indice de masa corporal es de: {round(imc,2)}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.

celcius = float(input("Ingrese la temperatura en grados celcius: "))
fahrenheit = (9/5)*celcius+32
print(f"{celcius} grados celcius es equivalente a {fahrenheit} grados fahrenheit!")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

num1 = float(input("Ingrese un número"))
num2 = float(input("Ingrese otro número"))
num3 = float(input("Ingrese otro número"))
print(f"El promedio de los tres números es de: {round((num1+num2+num3)/3,2)}")
#-------------------------------------------------------------------------
#TP N°1 - Estructuras secuenciales - Programacion I - UTN
# Nombre del alumno: Pérez Lucio Gabriel
