# Taller 3 PYTHON
# Autor: Raúl Gordillo Zabaleta
# fecha: 12 de septiembre de 2022

from datetime import date
hoy = date.today()    # Fecha actual
print ("Hoy es el día: ", hoy)
print()

a = int(input("Digite el valor de A: "))
b = int(input("Digite el valor de B: "))
if a >= b:
    print ("A es mayor o igual que B")
else:
    print ("A es menor que B")

print ()

curso1="Requerimientos"
curso2="Algoritmos"
print("El curso1 es: ", curso1)
print("El curso2 es: ", curso2)
if curso1 == "Requerimientos" and curso2 == "Algoritmos":
    print ("Usted estudia Programación de Software")
else:
    print ("Usted estudia otro programa diferente a Programación de Software")
print()
print ("***** Final del Análisis del Programa de Formación SENA *****")
print()

frase = input("Digite una oración ")
print("La frase en mayúscula es: ", frase.upper())
longitud = len (frase)
print("La longitud de la frase es: ", len(frase), "caracteres")
if longitud > 10:
    print ("La frase contiene más de 10 caracteres")
else:
    print ("La frase contiene menos de 10 caracteres")
print ()
print ("FINAL DEL PROGRAMA")