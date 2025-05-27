#-------------------------------------------------------------------------------------------

#Tecnicatura Universitaria en Programación                -Universidad Tecnológica Nacional-

#                                 TP-3 ESTRUCTURAS REPETITIVAS   

#Alumno: PEREZ LUCIO GABRIEL
#------------------------------------------------------------------------------------------#
#---------------------------------------  EJERCICIOS  -------------------------------------#                                      
#------------------------------------------------------------------------------------------#

# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

# Definicion de funciones
def recursive_factorial(num):
    if num == 0:
        return 1
    else:
        return num*recursive_factorial(num-1)           #calcula el factorial

def recursive_count(num):
    if num == 1:
        return 1
    else:
        print(f"{num}!: {recursive_factorial(num)}")        #imprime el resultado de la funcion factorial que se le pasa como 
        return recursive_count(num-1)+ 1           #<---  #argumento el valor "n" dentro de la funcion "recursive_count"

# Programa principal
num = int(input("Ingrese un número: "))
print(f"Número ingresado: {recursive_count(num)}")

#------------------------------------------------------------------------------------------#

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def rec_fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return rec_fibonacci(pos-1) + rec_fibonacci(pos-2)      #calcula la posicion del fibonacci

contador = 0
def recursive_count(num, actual=0):
    if actual == num:
        return
    else:
        print(rec_fibonacci(actual), end=', ')  #calcula fibonacci de "actual" sin dejar salto de linea    
        recursive_count(num, actual + 1)        #cuenta desde 0 a num


num = int(input("Ingrese la posicion desde la que quiere calcular fibonacci: "))
recursive_count(num)
print(rec_fibonacci(num))

#------------------------------------------------------------------------------------------#

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛(𝑚−1)
# . Prueba esta función en un
# algoritmo general.

def potencia_recursiva(n,m):
    if n == 0:
        return 0
    elif m == 1:
        return n
    else:
        return n * potencia_recursiva(n,m-1)


num = int(input("Ingresa la base de la potencia: "))
exponente = int(input("Ingresa el exponente de la potencia: "))
print(potencia_recursiva(num,exponente))

#------------------------------------------------------------------------------------------#

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

lista = []  #se crea una lista vacía

#divide recursivamente y guarda los restos de cada division
def recurr_div(decimal,lista):     
    if decimal < 1:
        return 1
    else:
        resto = decimal % 2
        lista.append(resto)
        recurr_div(decimal//2, lista)
        return lista                        

#imprime la lista de atrás para adelante ↓
def print_list(list):                       
    if len(list) == 0:
        return
    else:
        print(list[-1], end="")
        return print_list(list[:-1])
    
recurr_div(10,lista) #se pasa el número y la lista vacía
print_list(lista)    #se le pasa la lista ya con los restos e imprime al reves.

#------------------------------------------------------------------------------------------#

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(cadena):
    len_cadena = len(cadena)
    if len_cadena <= 1:     #si la cadena tiene menos de 1 o 1 letra
        return True        
    elif cadena[0] != cadena[-1]:   #si la ultima y la primera letra son diferentes, es False.
        return False
    else:
        return es_palindromo(cadena[1:-1])  #llamar a la funcion con cadena[desde primera a ultima] como arg

palabra = input("Ingrese una palabra: ")
print(es_palindromo(palabra))

#------------------------------------------------------------------------------------------#

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

#-------------resolución:
#Hipotesis: Si a cualquier número lo dividimos sucesivamente entre 10, conseguiremos que los enteros
#vayan pasando a decimal: por ej: 135/10= 13,5, eso entre 10: 1.35 y eso entre 10 = 0.135 (ya cuando tenemos 0,... 
# habremos extraido todos los enteros a la parte decimal). 

# Si consigo extraer siempre el primer decimal en cada division,
#habré conseguido extraer todos los digitos para cuando llegue a 0 (0,135) la parte entera:

from math import floor

def suma_digitos(n):
    entero = floor(n)                                           #convierte a entero                  
    primer_decimal = int(( n - floor(n)) * 10)                  #extrae el primer decimal
    if entero == 0:                                             #Si la parte entera es 0, retornar
        return primer_decimal
    else:                                                       #Sino, extraer el siguiente entero, y sumarlo
        return suma_digitos(n/10) + primer_decimal              #al decimal que tenemos (anteriormente un entero)


print(suma_digitos(305))

#------------------------------------------------------------------------------------------#
# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 0:
        return n
    else: 
        return contar_bloques(n-1) + n


n_bloques_nivel_bajo = int(input("Ingrese el N° de bloques que tiene el nivel más bajo de la piramide: "))
print(f"Para construir la piramide con {n_bloques_nivel_bajo} bloques en el nivel bajo, se necesitan: {contar_bloques(n_bloques_nivel_bajo)} bloques.")

#------------------------------------------------------------------------------------------#

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4 
# contar_digito(123456, 7) → 0 

#-------------resolución:
#Ideas:
#   • dividir sucesivamente por 10 y restarlo a ese numero entero redondeado (floor) * 10, nos da el primer decimal. 
#   Ej: (15.5 - floor(15.5))*10 = 5
#   • comparar ese decimal con el digito proporcionado por parametro. Ej: si digito = 5, y es igual a param = 5. Contador + 1
#   • contar las veces que coinciden sumandolo a un contador. 

from math import floor

def contar_digito(numero,digito,contador=0):
    primer_decimal = int(( numero - floor(numero)) * 10 )
    print(f"primero decimal: {primer_decimal}")
    if numero < 1 and primer_decimal != digito:
        return contador
    elif primer_decimal == digito:
        contador = contador +1
        return contar_digito(numero/10,digito,contador)
    else:
        return contar_digito(numero/10,digito,contador)

print(contar_digito(125,5))

