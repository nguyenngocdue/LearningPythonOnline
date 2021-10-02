""" 
Bài 2: Viết phương trình:
    - Nhập 1 số nguyên dương N
    - Phân tích N ra làm các chữ số
    - Đưa ra số đảo ngược của N
    - Số N có thuộc dạng đối xứng không? (121, 1221, 24342...)
"""

""" 1.1 """
n = int(input('Enter possive N: '))

# # way 1
# result = []
# for i in range(len(str(n))):
#     result.append(int(str(n)[i]))
# print(f'Slipt N: {result}')

# Way 2
slpit_N = [int(str(n)[i]) for i in range(len(str(n)))]
print(f'Slipt number N: {slpit_N}')

""" 2.2 """
# Way1:
# you can also use:  slipt_N[::-1] => for

# Way 2:
# result = []
# devidi_N = [] 
# for i in range(1,len(str(n))+1):
#     result.append((str(n)[-i]))
# print(f'Slipt N and Reverse list : {result}')

#Way 3:
#result = [str(i) for i in slpit_N[::-1]]

#Way 4:
result = [str(n)[-i] for i in range(1,len(str(n))+1)]
re = []
val = ''
for i in result:
    val += i
    a = re.append(val)
print(f'Reverse N: {int(val)}')


""" 2.3 """
#121 1221 123321 12344321
result = [int(str(n)[i]) for i in range(len(str(n)))]
flag = True
for i in range(int(len(result)*0.5) ):
    if result[i] != result[-1-i]:
        print(f'{n} is not an opposite number')
        flag = False
        #print('Check in-flag: ', flag)
        break

#print('Check out-flag: ', flag)
if flag == True: 
    print(f'{n} is an opposite number')

