""" 
Bài tập Tuple
    1. Viết chương trình đảo ngược một Tuple
    2. Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu Tuple.
    3. Viết chương trình tìm ra tuple có phần tử thứ 2 nhỏ nhất từ một list chứa các tuple.
    4. Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực.
"""
# ----------------------------------------------------------------
from collections import Counter

tup = (1, 2, 3, 4, 5)
reverse_tup = tup[::-1]

new_lst02 = ['a', 1, 2, 1, 2, 3, 'a', (4, 5, 6), 'b']
for idx, val in enumerate(new_lst02):
    if type(val) == tuple:
        count = Counter(new_lst02[:idx])
        print('The count of elements occur of list',count)

new_lst03  = [1, 2,(1), (4, 5, 3), (6, 7, 10), (3, 4, 5)]

#Look at second index maximum value from tuple
extract_tup = [i for i in new_lst03 if type(i) == tuple and len(i) > 1]
max_tup = extract_tup[0]
for i in extract_tup:
     if i[2] > max_tup[2]:
         max_tup = i
         print('Maximum tuple at second index', max_tup)

new_lst04 = [1, 2, 3, (4, 5, 6), ('a', 7, 8, 10), 'z', (6, 7, 9, 'c')]
# Extract tuples
extract_tup = [i for i in new_lst04 if type(i) == tuple]

#remove string from tuples
res = [tuple([val for val in i if type(val) != str]) for i in extract_tup]
print("The list after string removal is: ", res)

#Totall tuples
totall_res = [sum(tup) for tup in res]
print('Totall value each tuples:', totall_res)
print('Totall value from all tuples:', sum(totall_res))

# Maximum value from tuples
max_tuples = [max(tup) for tup in res]
print('Maximum value from tuples:', max_tuples)