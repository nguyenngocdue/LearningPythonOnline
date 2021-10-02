""" 
Bài 1: Viết phương trình
    - Nhập vào 1 chuỗi kí tự, lưu ở biến s.
    - In ra chuỗi kí tự đó theo cú pháp: Your input string is: '..'.
    - In ra giá trị mã ASCII của chuỗi kí tự đó trên cùng 1 dòng.
    - Đổi các chữ về in thường, loại bỏ các kí tự không phải số và không phải chữ, in ra chuỗi kí tự đã xử lý.
    - Xóa bỏ tất cả các khoảng trắng.
    - In hoa chữ cái đầu chuỗi hoặc sau khoảng trắng như viết tên người.
 """
#---------------------------------------------------------------- 
s = str(input('Enter your string: '))
print(f'Your input string is: {s}')
s_Ascii = ''
for i in s:
    s_Ascii += str(ord(i)) + " "
print(s_Ascii)
#---------------------------------------------------------------- 
""" Đổi các chữ về in thường, loại bỏ các kí tự không phải số và không phải chữ, in ra chuỗi kí tự đã xử lý. """

out_lst1 = ''
for i in s:
    if 'A' <= i <= 'Z':
        #out_lst1 += chr(ord(i) + 32)
        out_lst1 += i.lower()
    elif '0' <= i <= '9':
        out_lst1 += i
    elif 'a' <= i <= 'z':
        out_lst1 += i
print('Out list 1: ', out_lst1)

#----------------------------------------------------------------
""" Xóa bỏ khoảng trắng: """
out_lst2 = ''
for i in s:
    if i != " ":
        out_lst2 += i
print('Out list 2: ',out_lst2)
print('Dùng hàm replace để delete khoảng trắng:', s.replace(" ",""))

#----------------------------------------------------------------
""" In hoa chữ cái đầu chuỗi hoặc sau khoảng trắng như viết tên người."""
name = []
for i in s.split():
    name.append(i[0].upper() + i[1:])
print('My name is: ', ' '.join(name))

#Conprehension
name = ' '.join(word[0].upper() + word[1:] for word in s.split())
print('My name is: ', name)