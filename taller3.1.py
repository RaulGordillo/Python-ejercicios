# Taller 3.1 PYTHON
# Autor: Raúl Gordillo Zabaleta
# fecha: 12 de septiembre de 2022

from datetime import date
hoy = date.today()    # Fecha actual
print ("Hoy es el día: ", hoy)
print()

print ("EJERCICIO DE LAS CLASES DE TRIÁNGULOS")
a = int(input("Digite el valor de A: "))
b = int(input("Digite el valor de B: "))
c = int(input("Digite el valor de C: "))
if a == b and b == c:
    print("El TRIÁNGULO ES EQUILÁTERO")
else:
    if a == b or b == c or a == c:
        print("El TRIÁNGULO ES ISOCELES")
    else:
        print("El TRIÁNGULO ES ESCALENO")
print()

animal = input("Digite un animal: ")
animal = animal.upper()
if animal == "PERRO":
    print("Este animal es el mejor amigo del hombre", animal)
elif animal == "GATO":
    print("Este animal persigue a los ratones", animal)
elif animal == "OSO":
    print("Este animal vive en el polo norte", animal)
else:
    print("No es PERRO, no es GATO, ni OSO... es: ", animal)
print()
print ("FIN DEL EJERCICIO")        
