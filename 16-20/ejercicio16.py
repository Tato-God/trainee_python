'''
Calcula 2 elevado a la 4 potencia sin utilizar el operador **
'''

#utilizando operador **

def operation_oper(b,c):
    return b**c


# no recursivo
def operation(b, c):
    result = 1
    i = 0
    while i < c:
        i+=1
        result*=b
        
    return result

# operacion recursiva
def operation_rec(b,c):    
    if c == 0:
        return 1
    else:
        return b * operation_rec(b,c-1)


def operation_pow(b,c):
    return pow(b,c)


cant_max = 4
base = 2


print('Solo con operador')
print(operation_oper(base, cant_max))


print('No recursivo')
print(operation(base, cant_max))


print('Recursivo')
print(operation_rec(base, cant_max))


print('con libreria math()')
print(operation_pow(base, cant_max))


