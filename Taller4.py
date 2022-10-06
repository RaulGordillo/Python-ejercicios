# Taller 4.1 PYTHON
# Autor: Raúl Gordillo Zabaleta
# fecha: 26 de septiembre de 2022

from datetime import date
hoy = date.today()    # Fecha actual
print ("Hoy es el día: ", hoy)
print()

print("TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA FOR")
print()

num1=int(input("Digite el primer número: "))
num2=int(input("Digite el segundo número (mayor): "))
print("Ciclo para el primer número")
for i in range(num1):
    print (i)
print("Fin del ciclo")

print ()
print("Ciclo desde el primer número hasta el segundo número")
for i in range(num1,num2):
    print(i)
print("Fin del ciclo")

print()
empresa = input("Digite el nombre de una empresa: ")
empresa = empresa.lower()
for character in empresa:
    print (character)
print("Fin del ciclo")

print()
print("FINAL DEL PROGRAMA")

         
