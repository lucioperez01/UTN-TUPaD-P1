#TP N°1 - Estructuras secuenciales - Programacion I - UTN
# Nombre del alumno: Pérez Lucio Gabriel
#-------------------------------------------------------------------------
#EJERCICIOS:

#  1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”:

print("Hola Mundo!")

#-------------------------------------------------------------------------

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}")

#-------------------------------------------------------------------------
# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

#Se le pide al usuario datos y se los guarda en sus respectivas variables ↓
nombre = input("Ingrese su nombre: ") 
apellido = input("Ingrese su apellido: ") 
edad = input("Ingrese su edad: ") 
residencia = input("ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}") #se muestra en consola

#-------------------------------------------------------------------------

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

from math import pi     #importa de la libreria math, solo la constante PI 
radio = float(input("Ingrese el radio de un círculo: "))    #se pide el radio del circulo
perimetro = 2*radio*pi      #se calcula el perimetro
area = pi*(radio**2)        #se calcula el area
print(f"El área del círculo es: {round(area,2)}cm2 y su perimetro es: {round(perimetro,2)}cm") #se imprime en consola

#-------------------------------------------------------------------------

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

#se pide al usuario la cantidad de segundos y se guarda en la variable "seg" dentro de la funcion int() para que se convierta a entero
seg = int(input("Ingrese la cantidad de segundos para convertir a horas: "))
horas = (seg/60)/60         #pasa segundos a horas
print(f"Respuesta: {seg} segundos equivalen a {round(horas,2)} horas.") #se muestra en consola

#-------------------------------------------------------------------------

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

num = int(input("Ingrese un número entero: ")) #pide el numero y lo convierte a entero
#-imprime la tabla ↓
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

#-------------------------------------------------------------------------

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

#pide 2 numeros↓
num1 = int(input("Ingrese un número entero distinto de 0: "))
num2 = int(input("Ingrese otro número entero distinto de 0: "))
#muestra los resultados↓
print(f"{num1}+{num2}={num1+num2}")
print(f"{num1}/{num2}={num1/num2}")
print(f"{num1}*{num2}={num1*num2}")
print(f"{num1}-{num2}={num1-num2}")

#-------------------------------------------------------------------------

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.

#se piden los datos ↓
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso/(altura**2)  #se calcula el imc
print(f"Su indice de masa corporal es de: {round(imc,2)}")  #se muestra en consola

#-------------------------------------------------------------------------

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.

#pide temperatura en celsius↓
celcius = float(input("Ingrese la temperatura en grados celcius: "))
fahrenheit = (9/5)*celcius+32       #calcula en fahrenheit
print(f"{celcius} grados celcius es equivalente a {fahrenheit} grados fahrenheit!") #se muestra en consola

#-------------------------------------------------------------------------

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

#pide 3 numeros al usuario ↓
num1 = float(input("Ingrese un número"))
num2 = float(input("Ingrese otro número"))
num3 = float(input("Ingrese otro número"))
print(f"El promedio de los tres números es de: {round((num1+num2+num3)/3,2)}") #se muestra el promedio

#-------------------------------------------------------------------------
#TP N°1 - Estructuras secuenciales - Programacion I - UTN
# Nombre del alumno: Pérez Lucio Gabriel
