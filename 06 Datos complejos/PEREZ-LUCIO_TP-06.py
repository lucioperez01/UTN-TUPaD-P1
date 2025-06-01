#-------------------------------------------------------------------------------------------

#Tecnicatura Universitaria en Programación                -Universidad Tecnológica Nacional-

#                                 TP-3 ESTRUCTURAS REPETITIVAS   

#Alumno: PEREZ LUCIO GABRIEL
#------------------------------------------------------------------------------------------#
#---------------------------------------  EJERCICIOS  -------------------------------------#                                      
#------------------------------------------------------------------------------------------#

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

#------------------------------------------------------------------------------------------#
# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
    # • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
    # • Luego, pedí un nombre y mostrale el número asociado, si existe.

agenda = {}
for i in range(0,5):
    nombre = input("Ingrese el nombre del contacto a agendar: ")
    numero = input("ingrese el numero de telefono del contacto a agendar: ")
    agenda[nombre] = numero

print("Registro terminado!")
peticion = input("Ingrese el nombre del contacto para saber su número: ")
print(agenda[peticion])

#------------------------------------------------------------------------------------------#
# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresa una frase: ")
#separa las palabras
split_frase = frase.split(" ")
print(f"Palabras únicas: {set(split_frase)}")

#diccionario para contar palabras
conteo_palabras={}

#recorre las palabras y las cuenta
for palabra in split_frase:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print(f"Conteo de palabras: {conteo_palabras}")

#------------------------------------------------------------------------------------------#

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    nota1 = float(input("Ingrese la primera nota del alumno"))
    nota2 = float(input("Ingrese la segunda nota del alumno"))
    nota3 = float(input("Ingrese la tercera nota del alumno"))
    
    #se crea un diccionario donde se almacenan las notas con su clave correspondiente
    alumnos[nombre] = (nota1, nota2, nota3)

alumno = list(alumnos.keys())
notas = list(alumnos.values())

print(alumno, notas)

#bucle que recorre alumno[i], suma las notas y calcula el promedio para cada uno
for i in range(3):
    print(f"Promedio de {alumno[i]} = {round((notas[i][0] + notas[i][1] + notas[i][2]) / 3,2) }")

#------------------------------------------------------------------------------------------#

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Conjuntos de estudiantes que aprobaron cada parcial
parcial1 = {"Ana", "Bruno", "Griselda", "David"}
parcial2 = {"Griselda", "David", "Elena", "Matias"}

# 1. Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2 
print("Aprobaron ambos parciales:", ambos)

# 2. Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
solo_uno = parcial1 ^ parcial2  
print("Aprobaron solo uno de los dos:", solo_uno)

# 3. Estudiantes que aprobaron al menos uno (unión)
al_menos_uno = parcial1 | parcial2 
print("Aprobaron al menos un parcial:", al_menos_uno)

#------------------------------------------------------------------------------------------#

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

productos = {
    'ventilador': 1,
    'estufa': 3,
    'cocina': 4,
    'microondas': 6,
    'heladera': 3
    }

clave = input("Ingrese el nombre producto: ")

#si el valor ingresado no está en el diccionario:
if clave not in productos:
    respuesta = input("El producto no está en el stock, ¿desea añadirlo? si/no")
    if respuesta == "si" or respuesta == "Si":
        valor = int(input("Ingrese la cantidad de existencias de dicho producto: "))
        productos[clave] = valor
        print(f"Producto añadido! {productos}")
    elif respuesta == "no" or respuesta == "No":
        print(f"Este es el Stock actualmente: {productos}")
#si está:
else:
    print(f'Del producto "{clave}" existen {productos[clave]} existencia/s')
    respuesta = input("¿Desea modificar la cantidad de existencias disponibles para este producto? si/no")
    if respuesta == "si" or respuesta == "Si":
        valor = int(input("Ingrese la cantidad: "))
        productos[clave] = valor
        print(f"Producto modificado! {productos}")
    elif respuesta == "no" or respuesta == "No":
        print(f"Este es el Stock actualmente: {productos}")

#------------------------------------------------------------------------------------------#

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("Lunes", "09:00"): "Clase de Programación",
    ("Martes", "15:30"): "Meet",
    ("Miércoles", "14:00"): "Fútbol",
    ("Jueves", "10:00"): "Reunión",
    ("Viernes", "20:00"): "Reunión con amigos"
}

dia = input("Ingrese el dia que desea consultar: ")
hora = input("Ingrese la hora: ")

if (dia, hora) not in agenda:
    print("No se han encontrado actividades pendientes para ese día o esa hora!")
else:
    print(f"El día {dia} a las {hora}, hay {agenda[dia,hora]}")

#------------------------------------------------------------------------------------------#
# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

original = {
    "Argentina": "Buenos Aires",
    "Francia": "Paris",
    "España": "Madrid",
    "Chile": "Santiago de Chile",
    "Ecuador": "Quito",
    "Colombia": "Bogotá"
}
invertido = {}

#se extraen las claves y valores por separado
valores = list(original.values())
claves = list(original.keys())

#bucle que asigna claves y valores al diccionario invertido
for i in range(len(valores)):
    invertido[valores[i]] = claves[i]

print(f"Diccionario original: {original}\nDiccionario invertido: {invertido}")

#------------------------------------------------------------------------------------------#