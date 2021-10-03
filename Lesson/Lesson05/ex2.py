""" 
Baì 2: Viết phương trình:
    - Nhập vào 1 chuỗi kí tự không dấu, không có kí tự đặc biệt, lưu ở biến S
    - Đếm số lần xuất hiện của các kí tự trong chuỗi đó.
    - Nhập vào 1 kí tự, tìm kiếm tất cả vị trí kí tự đó trong chuỗi, Nếu không tìm thấy in ra -1
    - Tìm kiếm vị trí đầu tiên xuất hiện kí tự đó từ bên trái sang bên phải, phải sang trái, nếu không thấy in ra -1 
 """

#----------------------------------------------------------------
""" Đếm số lần xuất hiện của các kí tự trong chuỗi đó. """

s = str(input("Enter your string: "))
# cách này em giải theo dictionary:
count = {}
for i in s:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)

# Cách này code theo thuật toán. Cho hai list để ghi giá trị vào.

# dic = []
# count = []
# for ele in s:
#     if ele not in dic:
#         dic.append(ele)
#         count.append(1) 
#     else:
#         ops = dic.index(ele)
#         count[ops] += 1
# # print('dic', dic)
# # print('count',count)

# # # Print ra kiểu dạng list:
# # # out = [str(c)+d for c,d in zip(count,dic)]
# # # print(out)

# #print ra kiểu dạng chuỗi:
# for i in range(len(dic)):
#     print(dic[i], '\t', count[i])



# # #----------------------------------------------------------------
# """ Nhập vào 1 kí tự, tìm kiếm tất cả vị trí kí tự đó trong chuỗi, Nếu không tìm thấy in ra -1 """

# # char = str(input('Enter a character : '))
# # look_index_char = ''
# # for index, ele in enumerate(s):
# #     if char not in s:
# #         print(-1)
# #         break
# #     elif ele == char:
# #         look_index_char +=  str(index + 1) + " "
# # print(f'Place of character {char}: ',look_index_char)

# # #----------------------------------------------------------------
# """ Tìm kiếm vị trí đầu tiên xuất hiện kí tự đó từ bên trái sang bên phải và ngược lại, nếu không thấy in ra -1  """

# search_index_char = str(input('Enter a character to search : '))
# index_char = [idx for idx in range(len(s)) if s[idx] == search_index_char]
# if index_char:
#     print(f'Character {search_index_char} from s list: ', index_char)
#     print(f'Character {search_index_char} from the left: ', index_char[0])
#     print(f'Character {search_index_char} from the right: ', index_char[-1])
# else:
#     print(-1)