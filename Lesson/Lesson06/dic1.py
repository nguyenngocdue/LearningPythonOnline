
# while True:
#     n = int(input('Enter n value: '))
#     if n > 0:
#         break
# out = {x: 'le'if x%2 else 'chan' for x in range(n)}
# print(out)
# n = 0
# out = {chr(x):1 for x in range(ord('a'),ord('z')+1)}
# print(out)

# Tìm hiểu về Hash table
# Tìm hiểu cách lấy dữ liệu của dictionary
# inmuitable data type
# định nghĩa con trỏ.
# 
#  
# out_lst1 = ''
# s = str(input("Enter your string: "))
# for i in s:
#     if 'A' <= i <= 'Z':
#         out_lst1 += i.lower()
#     elif 'a' <= i <= 'z':
#         out_lst1 += i
# print('Out list 1: ', out_lst1)


# count = {}
# for i in out_lst1:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1

# print(count)

dic = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}
for i in zip(dic.values(),dic.keys()):
    print(i)


