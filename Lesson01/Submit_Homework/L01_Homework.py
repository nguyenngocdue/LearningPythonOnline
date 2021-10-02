"""
1. Viết chương trình
a. In ra dòng chữ "What is your name?"
b. Cho phép người dùng nhập vào tên của họ
c. In ra dòng chữ "Hello <ten-da-nhap>" với <ten-da-nhap> là iput của user

2. Viết chương trình
a. Nhập vào 2 số nguyên a, b, in ra 2 số đó
b. Tính và in ra kết quả:
    i. a +b
    ii. a - b
    iii. a * b
    iv. a/b
c. Lặp lại câu b với format như sau: 2 + 3 = 5 (với ví dụ phép công, a = 2, b = 5 ) theo 2 cách
    i. Không sử dụng nhứng chuỗi
    ii. Nhúng chuỗi
3. Đọc đề trên Google Driver
"""


# câu 1.a:
print ("What is your name?")

# Câu 1.b:
name = input("Enter your name: ")
print(name)

# Câu 1.c:
name_lognin = input("Enter your login name: ")
print("Hello "+ str(name_lognin))

#Câu 2.a
a = int(input("Enter a integer: "))
b = int(input("Enter b integer: "))
print(a,b)

#Câu 2.ai-->2.iv
ab_total = a + b
ab_subtract = a - b
ab_mutiply = a * b
ab_divide = a / b
print(ab_total)
print(ab_subtract)
print(ab_mutiply)
print(ab_divide)

#Câu 2.c
a = 2
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(f'{a + b}')
print(f'{a - b}')
print(int('{}'.format(a)) * int('{}'.format(b)))
print(int('{}'.format(a)) / int('{}'.format(b)))  

##########################################################################
#Câu 3:
a_length_Land = float(input("Enter a length of land: "))
b_width_Land = float(input("Enter b width of land: "))
c_length_Yard = float(input("Enter c length of Yard: "))
d_width_Yard = float(input("Enter d width of Yard: "))

print('length of land is a =: {}'.format(a_length_Land))
print('width of land is b =: {}'.format(b_width_Land))
print('length of yard is c =: {}'.format(c_length_Yard))
print('width of land is d =: {}'.format(d_width_Yard))

area_land = a_length_Land * b_width_Land
area_yard = c_length_Yard * d_width_Yard
are_house = area_land - area_yard

print(f'Area of land is: {a_length_Land} * {b_width_Land} = {area_land} m2')
print(f'Area of yard is: {c_length_Yard} * {d_width_Yard} = {area_yard} m2')
print(f'Area of hourse is: {area_land} - {area_yard} = {are_house} m2')