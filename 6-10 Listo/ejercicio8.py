'''
Crea una tupla con elementos e imprimela
'''

tupla = (1,2,3,4,5,6)

print("Impresion completa del elemento ", tupla)

contar = 0
for i in tupla:
    contar+=1
    print("Posicion del elemento", contar, "contiene", i)