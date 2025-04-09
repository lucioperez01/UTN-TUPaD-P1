#-------------------------------------------------------------------------------------------

#Tecnicatura Universitaria en Programación                -Universidad Tecnológica Nacional-

#                                 TP-3 ESTRUCTURAS REPETITIVAS   

#Alumno: PEREZ LUCIO GABRIEL
#------------------------------------------------------------------------------------------#
#---------------------------------------  EJERCICIOS  -------------------------------------#                                      
#------------------------------------------------------------------------------------------#

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

#-------------------------------------------------------------------------------------------

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = input("Ingrese un número: ")
numLen = len(num) #calcula el tamaño del string
cont = 0
for i in range(numLen): # for i hasta el tamaño del string:
    num[i]
    cont +=1 #contador +1

print(f"El número tiene {cont} dígito/s.") #se imprime el resultado

#-------------------------------------------------------------------------------------------

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número: "))+1  #primer número + 1 para que no tome el for el primer número 
num2 = int(input("Ingrese un número: "))    #segundo número 
i=0
x=0
variable = 0 #acumulador
for i in range(num1,num2): #for desde el primer número hasta el segundo (no se incluye)
    print("-------------------------------")
    x+=1 #contador de vueltas del bucle
    print(f"vuelta n° {x}")
    print(f"Suma: {variable} + {i}")
    variable = variable + i  #acumlulador
    print("acumulado: ",variable)
print(f"El resultado es {variable}") #se imprime el resultado 


#-------------------------------------------------------------------------------------------

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

num = int(input("Ingrese un número: "))     #ingresa un número
acumulador = num    #lo suma suma a acumulador
print(f"Acumulado = {acumulador} ")     #se muestra
while num != 0:     #mientras el numero ingresado no sea 0, se sigue
    num = int(input("Ingrese otro numero"))
    acumulador += num #suma al acumulador el numero ingresado
    print(f"Acumulado = {acumulador}")
print(f"El monto total acumulado es {acumulador}!") #se muestra el resultado

#-------------------------------------------------------------------------------------------

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

from random import randint
randNum = randint(0,9)      #genera un número aleatorio entre 0 y 9
intentos = 0            #contador de intentos
while num != randNum:           #mientras numero ingresado no sea igual a numero aleatorio...
    intentos += 1           #en cada vuelta se suma 1 al contador de intentos
    num = int(input("Adivine el número del 1 al 9: "))      
    print(f"intento {intentos}")
if num == randNum:
    print(f"Adivinaste! Fueron necesarios {intentos} intentos!")    #se muestra en pantalla los intentos y el aviso de que ganó


#-------------------------------------------------------------------------------------------

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

MIN = 0         #constante de valor mínimo
MAX = 100           #constante de valor máximo
PASO = -2       #constante de paso del bucle
for i in range(MAX,MIN,PASO):           #for desde MAX(100) hasta MIN(0), con PASO(-2)
    print(i)            #se muestra i


#-------------------------------------------------------------------------------------------

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

NUM1 = 0                #constante de numero minimo para el for
num2 = float("-inf")    #num2 se inicializa en -inf para que caiga en el while
variable = 0       
while num2 < 0:         #[VALIDACION] mientras que num2 sea < 0 ↓
    num2 = int(input("Ingrese un número entero positivo: ")) #se le pide un número

for i in range(NUM1,num2):      #FOR desde NUM1(0) hasta el número ingresado
    print(f"Suma: {variable} + {i}")        #se muestra lo que se va a sumar
    variable = variable + i                 #se acumula
    print("acumulado: ",variable)           #se muestra el acumulado
    print("-------------------------------")
print(f"El resultado es {variable}")        #se muestra el resultado al final

#-------------------------------------------------------------------------------------------

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#declaracion de variables ↓
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(1,101):          #for del 1 al 101 (sin incluir)
    num = int(input("Ingrese un número entero: ")) #se pide un numero

    if num > 0:         #si es mayor a 0
        positivos += 1
    elif num < 0:       #si es meno a 0
        negativos += 1
    if num % 2 == 0:        #si es par
        pares += 1
    else:               #esle es impar
        impares += 1
        #se muestran los resultados ↓
print(f"ingresaste {positivos} números positivos.")
print(f"ingresaste {negativos} números negativos.")
print(f"ingresaste {pares} números pares.")
print(f"ingresaste {impares} números impares.")

#-------------------------------------------------------------------------------------------

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

MIN = 1             #constante para el numero minimo
MAX = 100           #constante para el número máximo
sum = 0                     
for i in range(MIN,MAX+1):#<---- for desde min a max, acomodando el número maximo (MAX+1) 
    num = int(input("Ingrese un número: "))
    sum += num                #sumando num a sum 
print(f"El promedio de los números ingresados fue de {sum/(MAX)}")   #mostrando el result

#-------------------------------------------------------------------------------------------

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = input("Ingrese un número: ")
numLen = len(num)               #para conocer la longitud del string               
for i in range(numLen-1,-1,-1):             #for desde numLen-1 hasta -1 con paso -1
    print(num[i], end='')

#-------------------------------------------------------------------------------------------
#Alumno: PEREZ LUCIO GABRIEL