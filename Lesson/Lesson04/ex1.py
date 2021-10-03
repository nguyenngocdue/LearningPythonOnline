""" 
Bài 1: Viết chương trình
    - Nhập vào 1 số nguyên dương n
    - Nhập vào n số nguyên dương bất kỳ, lưu vào list a, in ra a
    - In ra các phần tử chẵn của a
    - In ra tổng các phần tử lẻ của a
    - In ra tích các phần tử là số nguyên tố của a
"""
""" 1.1 """

n = int(input(' Enter a possive n: '))
""" 1.2 """
a = []
for item in range(n):
    val = int(input('Enter any possitve n: '))
    a.append(val)

print(f'List a is: {a}')

""" 1.3 + 1.4 """
even = []
total_odd = 0
product_prime_number = 1
for num in a:
    if num % 2 == 0:
        even.append(num)
    else:
        total_odd += num

    """ 1.5 """
    is_prime = True
    for check in range(2, num):
        if num % check == 0: # bằng == 0 nhảy dô set lại is_prime
            is_prime = False
            #print('in: ', is_prime)
            break # khi mà nhận False, stop here >> out ra is_prime == False
    if is_prime == True:  # nó bằng True là số nguyên tố.
        product_prime_number *= num
    #print('num',is_prime)

print(f'Even numbers of list: {even}')
print(f'Total Odd list : {total_odd}')
print(f'{product_prime_number}')



# Way 2 : Dùng cho câu 1.5
# n = int(input(' Enter a possive n: '))
# """ 1.2 """
# a = []
# for item in range(n):
#     val = int(input('Enter any possitve n: '))
#     a.append(val)

# print(f'List a is: {a}')

# product_prime_number = 1

# for i in a:
#     flag = True
#     if i < 2:
#         flag = False
#     elif i == 2:
#         flag = True
#     elif i % 2 == 0:
#         flag = False
#     else:
#         for j in range(3, i, 2):
#             if i % j == 0:
#                 flag = False
#                 break
#     if flag == True:
#         product_prime_number *= i

# print(f'{product_prime_number}')