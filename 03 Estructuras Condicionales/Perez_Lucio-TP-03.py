#-------------------------------------------------------------------------------------------

#Tecnicatura Universitaria en Programación                -Universidad Tecnologica Nacional-

#                                 TP-3 ESTRUCTURAS CONDICIONALES   

#Alumno: PEREZ LUCIO GABRIEL
#-------------------------------------------------------------------------------------------
#                                         EJERCICIOS
#-------------------------------------------------------------------------------------------

# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

age = int(input("Ingrese su edad: "))
if age > 18:
    print("Es mayor de edad!")

#-------------------------------------------------------------------------------------------

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado!")
else:
    print("Desaprobado.")
    
#-------------------------------------------------------------------------------------------
# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese un numero par: "))
if num % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print(f"El número {num} no es par. Por favor, ingrese un número par.")
    
#-------------------------------------------------------------------------------------------
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:

edad = int(input("Ingrese su edad: "))
if 0 < edad < 12:
    print("Usted es un niño/a.")
elif 18 > edad >= 12:
    print("Usted es un Adolescente.")
elif 30 > edad >= 18:
    print("Usted es un Adulto/a joven.")
else:
    print("Usted es un adulto/a.")
    
#-------------------------------------------------------------------------------------------
# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
print(len(contraseña))
caracteres = len(contraseña)
if 8 <= caracteres <= 14:
    print("Has ingresado una contraseña correcta!")
else:
    print(f"su contraseña tiene {caracteres} caracteres.") 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
    
#-------------------------------------------------------------------------------------------
# Escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
from statistics import mode, median, mean
#definiendo variables ↓ 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
#print↓
print(f"La moda es: {moda}")
print(f"La mediana es: {mediana}")
print(f"La media es: {media}")
#condicionales↓
if moda < mediana < media:
    print("Es de sesgo positivo o a la derecha.")
elif media < mediana < moda:
    print("Es de sesgo negativo o a la izquierda.")
elif media == mediana and mediana == moda:
    print("Es sin sesgo.")

#-------------------------------------------------------------------------------------------
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

string = input("Ingrese una frase o palabra: ")
lastLetter = string[-1]
if lastLetter == "a" or lastLetter == "e" or lastLetter == "i" or lastLetter == "o" or lastLetter == "u":
    print(string + "!")
else:
    print(string)

#-------------------------------------------------------------------------------------------
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro

name = input("Ingrese su nombre: ")
print("Como quiere escribir su nombre?: ")
print("Presione 1 para escribir su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("Presione 2 para escribir su nombre en minúsculas. Por ejemplo: pedro")
print("Presione 3 para escribir su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
choice = int(input("Ingrese 1, 2 o 3: "))

if choice == 1:
    print(name.upper())
elif choice == 2:
    print(name.lower())
elif choice == 3:
    print(name.title())
else:
    print("Opcion ingresada no correspondiente.")
    
#-------------------------------------------------------------------------------------------
# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla

magnitudTerremoto = float(input("Ingrese la magnitud de un terremoto: "))
if 0 < magnitudTerremoto < 3:
    print("Es imperceptible.")
elif 4 > magnitudTerremoto >= 3:
    print("Es ligeramente perceptible.")
elif 4 <= magnitudTerremoto < 5:
    print("Moderado. No suele causar daños.")
elif 6 > magnitudTerremoto >= 5:
    print("Es fuerte. Puede causar daño a estructuras débiles.")
elif 6 <= magnitudTerremoto < 7:
    print("Muy Fuerte. Puede causar daños significativos.")
elif magnitudTerremoto >= 7:
    print("Puede causar graves daños a gran")


#-------------------------------------------------------------------------------------------
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

userDay = int(input("Ingrese el dia actual: ")) #pregunta el dia
mes = int(input("Ingrese el mes actual: ")) #pregunta el mes
hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ") #pregunta el hemisferio

    #si el mes == 12 and el dia es >= 21 o el mes es > 0 y <= que 21. O el mes es <= 3 y el dia es <=20, se ejecuta ↓
if (mes == 12 and userDay >= 21) or (0 < mes <= 3 and userDay <= 20): 
    if hemisferio == "n" or hemisferio == "N":
        print("Es invierno!")
    else:
        print("Es verano!")
    #si el mes es 3 y el dia es <= a 31 y >= 21 o mes es <= 5 o mes es 6 y el dia es <= 20, se ejecuta ↓
elif (mes == 3 and 31 >= userDay >= 21) or (0 < mes <= 5) or (0 < mes == 6 and userDay <= 20):
    if hemisferio == "n" or hemisferio == "N":
        print("Es primavera!")
    else:
        print("Es otoño!")
    #si el mes es 6 y el dia es >= 20 o el mes es <= 8 o si el mes es == 9 y el dia es <= 20, se ejecuta ↓
elif (mes == 6 and userDay >= 20) or (0 < mes <= 8) or (mes == 9 and userDay <= 20):
    if hemisferio == "n" or hemisferio == "N":
        print("Es verano!")
    else:
        print("Es invierno!")
else: #si nada de esto se cumple, se ejecuta ↓ 
    if hemisferio == "n" or hemisferio == "N":
        print("Es otoño!")
    else:
        print("Es primavera!")

#-------------------------------------------------------------------------------------------
#Alumno: PEREZ LUCIO GABRIEL
