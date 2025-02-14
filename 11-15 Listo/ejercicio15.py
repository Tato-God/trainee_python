'''
Ordena una lista de números de menor a mayor
'''
array_num = [30,21,2,29,1,25,20,11,13,4,14,8,16,5,18,21,22,26,28,6,20,10,19,7,3,12,15,24,9,17,27,23]


print('lista desordenada')
print(array_num)


print('Misma lista orden ascendente')
array_num.sort()
print(array_num)


print('Nueva lista orden ascendente')
# aqui la lista se ordena pero te lo entrega como una nueva lista.
order_asc = sorted(array_num)
print(order_asc)


print('Misma lista orden descendente')
array_num.sort(reverse=True)
print(array_num)




