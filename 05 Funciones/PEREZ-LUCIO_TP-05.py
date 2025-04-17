#-------------------------------------------------------------------------------------------

#Tecnicatura Universitaria en Programación                -Universidad Tecnológica Nacional-

#                                 TP-3 ESTRUCTURAS REPETITIVAS   

#Alumno: PEREZ LUCIO GABRIEL
#------------------------------------------------------------------------------------------#
#---------------------------------------  EJERCICIOS  -------------------------------------#                                      
#------------------------------------------------------------------------------------------#

# #1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

#Definicion de funciones
def imprimir_hola_mundo():  #funcion para imprimir hola mundo
    print("Hola Mundo!")

#Programa principal
imprimir_hola_mundo()       #llamada a la funcion

#------------------------------------------------------------------------------------------#

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), 
# deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

#Definicion de funciones 
def saludar_usuario(nombre):        #funcion que imprime saludo
    print(f"Hola {nombre}!")

#Programa principal
saludar_usuario(input("Ingrese su nombre: "))       #llamada a la funcion
#------------------------------------------------------------------------------------------#

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#Definicion de funciones
def solicitar_datos_usuario(mensaje):       #funcion que solicita informacion al usuario, reutilizable
    variable = input(mensaje)
    return variable
def informacion_personal(nombre, apellido, edad, residencia):   #funcion que imprime un mensaje con la informacion solicitada
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Programa principal
#llamada a las funciones ↓
nombre = solicitar_datos_usuario("Ingrese su nombre: ")
apellido = solicitar_datos_usuario("Ingrese su apellido: ")
edad = solicitar_datos_usuario("Ingrese su edad: ")
residencia = solicitar_datos_usuario("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#------------------------------------------------------------------------------------------#

# 4. Crear dos funciones: calcular_area_circulo(radio) 
# que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) 
# que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

#import ↓
from math import pi

#definicion de funciones
def calcular_area_circulo(radio):                       #funcion para calcular area
    area = pi * radio**2
    return round(area,2)

def calcular_perimetro_circulo(radio):                  #funcion para calcular perimetro
    perimetro = 2*pi*radio
    return round(perimetro,2)

def validar_numero_entero(num):                         #funcion para validar el dato ingresado
    while num < 0:
        num = int(input("Error, ingrese un número entero."))
    return num

#programa principal
radio = int(solicitar_datos_usuario("Ingrese el radio de un círculo: "))        #solicitar_datos_usuario: funcion definida en ejercicios anteriores
radio= validar_numero_entero(radio)                                             #llamada a funcion para validar numero
print("El area del circulo es:",calcular_area_circulo(radio))                   #mensaje + llamada a funcion
print("El perimetro del circulo es:",calcular_perimetro_circulo(radio))         #mensaje + llamada a funcion

#-------------------------------------------------------------------------------------------#

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#definicion de funciones
def segundos_a_horas(segundos):
    result = (segundos/60)/60
    return result

#programa principal
segundos = int(solicitar_datos_usuario("ingrese un valor expresado en segundos: "))     #solicitar datos, convertirlos a int, almacenarlos en "segundos"
validar_numero_entero(segundos)                 #validar que "segundos" sea un entero positivo con funcion definida en anteriores ejercicios
print(f"{segundos} segundos equivalen a ",round(segundos_a_horas(segundos),2),"hora/s") #imprimir el valor redondeado en 2 decimales de segundos_a_horas con "segundos" como argumento.

#-------------------------------------------------------------------------------------------#

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

#definicion de funciones
def tabla_multiplicar(numero):                  
    for i in range(1,11):                       #bucle para iterar las multiplicaciones 
        tabla = numero*i                        #numero por i
        print(f"{numero} x {i} = {tabla}")      #imprime cada vuelta en pantalla

#programa principal
tabla_multiplicar(validar_numero_entero(int(solicitar_datos_usuario("ingrese un número: "))))  #se solicita un numero, se valida que sea entero y se pasa a tabla_multiplicar

#-------------------------------------------------------------------------------------------#

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

#definicion de funciones
def operaciones_basicas(a, b):                      #funcion para operaciones basicas
    suma = a + b
    resta = a - b
    mult = a * b
    div = a / b
    return (suma, resta, mult, div)                 #retorna una tupla con los resultados

def validar_no_cero(num):                           #para validar que el numero ingresado no sea 0 y no dividir por 0
    while num == 0:                                 #mientras numero sea 0
        num = int(input("ERROR: Ingrese un número válido"))     #preguntarle de nuevo el numero
    return num

#programa principal
num1 = validar_no_cero(validar_numero_entero(int(solicitar_datos_usuario("Ingrese un número"))))    #se solicitan los datos, se validan y guardan en num1            
num2 = validar_no_cero(validar_numero_entero(int(solicitar_datos_usuario("Ingrese un número"))))    
operaciones = operaciones_basicas(num1, num2)
print(f"{num1} + {num2} = {operaciones[0]}")                    #se muestran los resultados llamando a la tupla
print(f"{num1} - {num2} = {operaciones[1]}")
print(f"{num1} x {num2} = {operaciones[2]}")
print(f"{num1} / {num2} = {operaciones[3]}")
#-------------------------------------------------------------------------------------------#

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos 
# y llamar a la función para mostrar el resultado con dos decimales.

#definiciones de funciones
def calcular_imc(peso, altura):             #funcion que calcula el IMC
    result = peso / (altura**2)
    return result

#programa principal
peso = validar_no_cero(validar_numero_entero(int(solicitar_datos_usuario("Ingrese su peso: ")))) #se pide al usuario, se valida, y se guarda en peso
altura = validar_no_cero(validar_numero_entero(float(solicitar_datos_usuario("Ingrese su altura: ")))) #lo mismo que arriba. Se utilizan funciones de anteriores ejercicios
print("El resultado es:",round(calcular_imc(peso, altura),2))           #se muestra

#-------------------------------------------------------------------------------------------#

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

#definicion de funciones
def celcius_a_fahrenheit(celcius):
    result = (celcius * 1.8) + 32
    return result

#programa principal 
print("Resultado en Fahrenheit:",round(celcius_a_fahrenheit(int(solicitar_datos_usuario("ingrese un valor expresado en grados celcius: "))),2))

#-------------------------------------------------------------------------------------------#

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

#Definicion de funciones
def calcular_promedio(a, b, c):             #funcion para calcular promedio
    result = (a + b + c)/3                  #suma y divide por la cantidad
    return result   

#prograna principal
num1 = validar_no_cero(int(solicitar_datos_usuario("Ingrese un número ")))  #se pide al usuario un numero, se convierte a int y se valida que no sea 0
num2 = validar_no_cero(int(solicitar_datos_usuario("Ingrese un número ")))
num3 = validar_no_cero(int(solicitar_datos_usuario("Ingrese un número ")))
resultado = calcular_promedio(num1, num2, num3)
print("El promedio de los números ingresados es:",round(calcular_promedio(num1,num2,num3),2))

#-------------------------------------------------------------------------------------------#
#Alumno: PEREZ LUCIO GABRIEL