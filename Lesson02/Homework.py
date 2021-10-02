"""
Bài 1: viết chương trình:
    + Nhập vào 1 số.
    + In ra giá trị tuyệt đối số đó.
"""

# n = float(input('Enter value n: '))
# if n < 0:
#     print(f'Absolute value n is: {-n}')
# print(f'Absolute value n is: {n}')


"""
Bài 2: Viết chương trình:
    - Nhập vào 1 ký tự.
    - Nếu:
        + Kí tự đó là kí tự thường thì in ra chính nó,
            nếu ký tự hoa thì đổi về kí tự thường.
        + Kí tự đặt biệt thì in ra kí tự đặc biệt.
        + Nếu là số thì in ra số đối.
 """
val = input('Enter character n: ')

if ('a' <= val <= 'z'):
    print(f'Lowercase character: {val}')
elif ('A' <= val <= 'Z'):
    v = chr((ord(val) + 32))
    print(f'{val} is changed to lowercase character: {v}')
#if val.isdigit() == True: 
elif '0' <= val <= '9': # it has a problem with [val > 9 and val <0]
    print(f'Digit character: {-float(val)}')


"""
Bài 3: Viết chương trình:
    aX + b = 0
    - Nhập vào a, b là hệ số phương trình bậc 1.
    - In ra kết quả phương trình đó. 
"""

a = float(input('Enter value a: '))
b = float(input('Enter value b: '))

if a == 0:
    if b == 0:
        print('The equation has no value')
    elif b != 0:
        print('The equation has infinitely many values')
else:
    print(f'The equation has value X: X = -b/a = {-b}/{a} = {-b/a}')



"""
Bài 4: Viết phương trình:
    aX^2 + bX + c = 0
    - Nhập vào a, b, c là hệ số phương trình bậc 2 một ẩn.
    - In ra kết quả phương trình đó.
"""

a = float(input('Enter value a: '))
b = float(input('Enter value b: '))
c = float(input('Enter value c: '))

if a == 0:
    if b == 0:
        if c == 0:
            print(f'The equation has infinitely many values')
        elif c != 0:
            print(f'The equation has not a value')
    else:
        print(f'The equation has value X: X = -c/a = {-c/b}')
else:
    denta = b*b - 4*a*c
    if denta > 0:
        import math
        print(f'The equation has two values: X1 = (-b - sqrt(denta))/2a = {(-b - math.sqrt(denta))/(2*a)},\
                                             X2 = (-b + sqrt(denta)/2a) = {(-b + math.sqrt(denta))/(2*a)}')
    elif denta == 0:
        print(f'The equation has value X: X = -c/a = {-b/2*a}')
    else:
        print(f'The equation has not a value')


