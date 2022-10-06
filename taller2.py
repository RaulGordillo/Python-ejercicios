# Taller 2 PYTHON
# Autor: Raúl Gordillo Zabaleta
# fecha: 12 de septiembre de 2022

from datetime import date
hoy = date.today()    # Fecha actual
print ("Hoy es el día: ", hoy)

a = int (input("Digite el primer número: "))
b = int (input("Digite el segundo número: "))
c = int (input("Digite el tercer número: "))
x = [a, b, c]
print ("El valor máximo es: ", max(x))
print ("El valor mínimo es: ", min(x))
print ("La suma de los tres valores es: ", sum(x))
print()

z = float(input("Digite un número con decimales: "))
redondo = round(z)
print ("El valor de", z, " redondeado es:", redondo)
print() 

frase = input("Digite una oración: ")
print ("La frase en mayúscula es: ", frase.upper())
print ("La frase en minúscula es: ", frase.lower())
print ("La frase con mayúscula inicial es: ", frase.capitalize())
print ("La frase con palabras con mayúscula inicial es: ", frase.title())
print ("La longitud de la frase es: ", len(frase), "caracteres")
print()
print("FIN DEL EJERCICIO")