import re
data = open('regex_sum_1492257.txt')
suma = 0
for linea in data:
    linea = linea.rstrip()    
    x = re.findall('([0-9]+)', linea)
    for valor in x:
        suma = suma + int(valor)
print(suma)


