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
    if "0" <= n <= "9":
        sum += int(n)    
    
    if len(n) > 1:
        outText = ''
        for j in n:
            if ('A' <= j) and (j <= 'Z'):
                n = chr(ord(j) + 32)
                outText += n
            if ('a' <= j) and (j <= 'z'):
                outText += j

print(f'Sum digit : {sum}')
print(f'Char sequence: {outText}')
