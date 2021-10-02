""" 

Bài 1:
    a. Viết chương trình nhập vào số nguyên dương, nếu không phải số nguyên 
        dương thì nhập lại đến khi đúng.
    b. Tiếp đó nhập vào n số bất kỳ.
    c. Tính tổng n số đó, dưới dạng phép tính tường minh: '1+3+10=14'.
    d. Số lớn nhất - số nhỏ nhất là số nào, ở vị trí nào?

"""

#a.

while True:
    val = int(input('Enter your positive integer: '))
    if val > 0:
        break

#b.
import math
#print the possitive infinity
min_val = math.inf
#print the negative infinity
max_val = -math.inf

min_idx = -1
max_idx = -1
sum_result = 0
t = 1
sum_n = ''

for i in range(val):
    current_val = float(input(f'Tern: {t},Enter number n: ' ))
    sum_result += current_val
    t += 1
    #print a min value , a index value
    if current_val < min_val:
        min_val = current_val
        min_idx = i

    #print a max value , a index value
    if current_val > max_val:
        max_val = current_val
        max_idx = i
        
    if i == 0:
        sum_n = f'{current_val}'
    else:
        sum_n = f'{sum_n} + {current_val}'

sum_n = f'{sum_n} = {sum_result}'

print(sum_n)
print('Min value:', min_val, ',at:', min_idx +1)
print('Max value:', max_val, ',at:', max_idx +1)

