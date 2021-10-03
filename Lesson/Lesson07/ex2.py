""" 
Bài tập Set:
    1. Viết chương trình đếm số lượng ký tự phân biệt từ một chuỗi nhập vào từ bàn phím sử dụng Set.
    2. Khởi tạo 2 List có n phần tử ký tự 'a' --> 'z'. Tìm phần tử chung giữ 2 list đó với:
    a. n = 10
    b. n = 100
    c. n = 1.000.000
    3. Đếm số key:val trùng lặp trong 2 dictionary
"""
import random, string


s =  set(input('Enter your string s: '))
print(f'Your string is {s}')
print(f'The number of discriminating charecters of list S: {len(s)} ')


lsta = ['a', 'b', 'c', 'd', 'e', 'f', 'g',]
lstb = ['b', ]

# Create a charecter list from a to z
letters = string.ascii_lowercase
length = int(input('Enter your length: L = '))
lst_a = [random.choice(letters) for val in range(length)]
lst_b = [random.choice(letters) for val in range(length)]

# Convert list to set
set_a = set(lst_a)
set_b = set(lst_b)

#Intersection of set
intersec_ab = set_a & set_b #lst_a.intersection(lst_b)
print('List a: ', lst_a)
print('List b: ', lst_b)
print(f'Intersection between list a and list b: {intersec_ab}')

#Create two dictionary
dic1 = {1:'a', 5:'b', 2:'c', 6:12}
dic2 = {4: 100, 2:'a', 1:'a', 2:'c', 6:'d', 5:'b'}
import collections
print('Dictionary 1: ',dic1)
print('Dictionary 2: ',dic2)
count = 0
for k1,v1 in zip(dic1.keys(),dic1.values()):
    for k2,v2 in zip(dic2.keys(),dic2.values()):
        if k1 == k2 and v1 == v2:
            count += 1
print('The number of kyey:val values duplicate in 2 dictionary: ',count)

