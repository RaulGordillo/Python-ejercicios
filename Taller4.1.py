#Taller 4.1 PYTHON
# Autor: Raúl Gordillo Zabaleta
# fecha: 26 de septiembre de 2022

from datetime import date
hoy = date.today()    # Fecha actual
print ("Hoy es el día: ", hoy)
print()

print("TALLER 6 CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print()
num1=int(input("Digite el primer número: "))
num2=("***Ciclo controlado por contador")
print("Ciclo para el primer número")
i = 1
while i <= num1:
    print (i)
    i +=1
print("Fin del ciclo")

print ()
print("****Ciclo controlado por evento")
i = 1
numero1= 5
numero2 = int(input("Digite un número de 1 a 10: " ))
while numero2 != numero1:
    i+=1
    numero2 = int(input("Digite un número de 1 a 10: " ))
print("Acertaste en el intento número: ", i)
print("Fin del ciclo")

print()
print("****Ciclo abortado con la secuencia break")
amistad = input("Digite nombre de una amistad: ")
amistad = amistad.upper()
for character in amistad:
    if character == "A":
        break
    print (character)
print("Fin del ciclo")
print()
print("FINAL DEL PROGRAMA")


