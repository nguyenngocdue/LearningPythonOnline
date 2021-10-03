n = int(input(' Enter a possive N: '))

n_item = n

binary = ''
i = 0
while True:
    if n == 0:
        binary = f'{0}{binary}'
        break
    s = n % 2
    binary = f'{s}{binary}' #string interpolation
    i += 1 
    n = n // 2 #n = (n-surp)/2
    #print(binary)
    
print(f'The binary of a possive N: {binary}')


lst = list()
for num in binary:
    lst.append(int(num))
print('List of N: ', lst) 

re = lst[::-1]
reverse_binary = ''
for i in re:
    reverse_binary += str(i)
print('Reverse of binary: ', int(reverse_binary))

n = n_item

i = 1
val_reverse_binary = 0
while True:
    if n == 0:
        break
    surplus = n % 2
    n = n // 2
    val_reverse_binary += surplus *(2**(len(reverse_binary)-i))
    i += 1
lst_decimal = [int(i) for i in str(val_reverse_binary)]
print('Decimal of reverse of binary: ', lst_decimal)
