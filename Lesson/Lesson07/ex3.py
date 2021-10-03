""" 
Bài tập 1: 
    Nhập n phần tử số nguyên vào List a. (n nhập từ bàn phím)
    Tạo ra list b là các số nguyên dương và âm.
    Viết chương trình tính tổng lacing các phần tử của list a và b với nhau.
"""
while True:
    numberof_a = int(input('How many items do you want to enter into list a?'))
    break
a = []
for i in range(numberof_a):
    a.append(int(input('Enter N number : ')))

while True:
    numberof_b = int(input('How many items do you want to enter into list b?'))
    break
b = []
for i in range(numberof_b):
    b.append(int(input('Enter N number : ')))
print('List a: ', a)
print('List b: ', b)

result = []
for i in a:
    sum = 0
    for j in b:
        product = i*j
        sum += product
    result.append(sum)  
print(result)

