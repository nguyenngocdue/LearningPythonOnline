# """ Bài 01: Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiền của một chuỗi thành $. """

# s = str(input('Enter your string: '))
# out = [s.replace(s[0],"$")]
# print('replace',out)

# #----------------------------------------------------------------

# """ Bài 02: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím."""

# m = int(input('Enter your place m to remove: '))
# while m < 0:
#     m = int(input('Enter your place m to remove: '))
#     break
# lst = [i for i in s]
# v = lst.pop(m)
# print(f'Place need to remove: "{m}", Value: "{v}" >>>',''.join(lst))

# #----------------------------------------------------------------
# """ Bài 03: Viết chương thình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi"""
# #s = str(input('Enter your string: '))
# ix = ''
# for index, ele in  enumerate(s):
#     if index % 2:
#         ix += ele
# print(ix)
# #----------------------------------------------------------------
# """ Bài 04: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào, nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng. """

# s = str(input('Enter your string: '))
# if len(s) < 2:
#     print('Empty string', ' ')
# if len(s) >= 2:
#     ix = s[:2] + s[len(s)-2:]
# print(ix)

#----------------------------------------------------------------
""" Bài 05: Viết chương trình tìm ra kí tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bàn phìm."""


#----------------------------------------------------------------
""" Bài 06: Viết chương trình đảo ngược ký tự thường sang ký tự hoa và ký tự hoa sang ký tự thường trong một chuỗi."""