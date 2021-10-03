"""  
Bài 2 : Viết chương trình
    a. Nhập vào 1 ký tự, nếu gặp Enter thì chuyển sang bước tiếp theo.
    b. In ra tổng các số trong chuỗi ký tự đã nhập.
    c. Đưa các chữ cái hoa về chữ thường, chỉ in ra các chữ cái có trong chuỗi,
        bỏ qua số và các ký tự đặc biệt, giữa nguyên tính thứ tự.
"""
sum = 0
char_seq = ''
while True:
    n = input('Enter a character: ')

    if n == "":
        break
    
    if len(n) > 1:
        continue
    
    if "0" <= n <= "9":
        sum += int(n)

    if 'A' <= n <= 'Z':
        n = chr(ord(n) + 32)
    
    if 'a' <= n <= 'z':
        char_seq = f'{char_seq}{n}'
print(f'Sum digit is {sum}')
print(f'Char sequence: {char_seq}')