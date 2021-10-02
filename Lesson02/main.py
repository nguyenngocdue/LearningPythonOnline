a = float(input(' a value = '))
b = float(input(' b value = '))
print(a>b, type(a>b))
print(a<b, type(a<b))
print(a==b, type(a==b))

""" Toán tử Logic
and: trả về True nếu một trong 2 là True, ngược lại trả về False (kiểm tra từ trái qua phải, sai là kết thúc luôn)
or: trả về False nếu một trong 2 là False, ngược lại trả về True
not: trả ngược lại giá trị.
 """
x = float(input(' x value = '))
y = float(input(' y value = '))
print(x>y or (x<=y))
print(False and (x!= y))

x = float(input(' x value = '))
c = str(input(' c value = '))
print(x>0, x<0, x!=10)
print(c>'a', c<'z')


c = input("Nhập c:")
print('c là chữ thường', 'a' <= c <= 'z')
print('c là chữ hoa', 'A' <= c <= 'Z')
print('c là chữ cái', 'a' <= c <= 'z' or 'A' <= c <= 'Z')
print('c ko là chữ cái', not ('a' <= c <= 'z' or 'A' <= c <= 'Z'))


c = input("Nhập c: ")
print('c là chữ thường', 'a' <= c <= 'z')
print('c là chữ hoa', 'A' <= c <= 'Z')
print('c là chữ cái', 'a' <= c <= 'z' or 'A' <= c <= 'Z')
print('c không là chữ cái', not('a' <= c <= 'z' or 'A' <= c <= 'Z'))

inp = input('Enter value: ')
if ('a' <= inp <= 'z'):
    print('inp')
print('End')

inp = input('Enter inp value: ')
if ('a' <= inp <= 'a'):
    print(chr(ord(inp - 32 )))
print(inp)

n = float(input('Enter n value: '))
if n < 0:
    print('Giá trị tuyệt đối là:'-n)
print(f'Giá trị tuyệt đối là: {n}')        

n = int(input('Enter n value: '))
if (n % 2 == 0):
    print(f'{n} is even')
else:
    print(f'{n} is odd')

''' Truthy - Falsy'''
x = [1,2,3]
if x:
    print('value 1: True')
else:
    print('value 2: False')

x = float(input('Enter x value: '))
y = float(input('Enter y value'))
if x > y:
    print(f'{x} > {y}')
elif x == y:
    print(f'{x} = {y}')
else:
    print(f'{x} < {y}')