""" 
Baì 3: Viết chương trình
    - Nhập vào một số nguyên dương, yêu cầu nhập đến bao giờ đúng số nguyên dương
        thì chuyển sang bước khác.
    - Đổi số đó sang hệ nhị phân và in ra kết quả.
        (gợi ý: dùng string interpolation)
    - Đảo ngược số đó ở hệ nhị phân, in ra kết quả.
        (gợi ý: dùng ép kiểu và string interpolation)
    - Đổi số đã được đảo ngược ra hệ thập phân, in ra kết quả.

"""
while True:
    n = int(input('Enter a positive integer:' ))
    if n > 0:
        break
n_copy = n
binary = ''
reverse_binary = ''
val_reverse_binary = 0

i = 0
while True:
    if n == 0:
        break
    surplus = n % 2
    binary = f'{surplus}{binary}'
    reverse_binary = f'{reverse_binary}{surplus}'
    i += 1
    n = n // 2
n = n_copy
while True:
    if n == 0:
        break
    surplus = n % 2
    n = n // 2
    val_reverse_binary += surplus *(2**(i-1))
    i -= 1
    
print('The binary for %d is %s' %(n_copy, binary))
print(f'The reverse binaty value:  {reverse_binary}, value: {val_reverse_binary}')

