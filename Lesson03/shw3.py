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
    n = int(input('Enter a possitve integer : '))
    if n > 0:
        break

n_input = n
surplus = []
while n_input > 0:
    a = int(float(n_input % 2))
    #print(f'surplus: {a}')
    surplus.append(a)

    n_input = (n_input-a)/2 
    #print(f'n_input: {n_input}')

#print(f'{surplus}')
string = ''
for i in surplus[::-1]:
    string = string + str(i)
print('The binary for %d is %s' %(n, string))


reverse_binary = string[::-1]
print(f'The reverse binaty value {string} is {reverse_binary}')


val_reverse_binary = 0
i = 0
while True:
    if n == 0:
        break
    surplus = n % 2
    n = n // 2
    print('nnnn', n)
    
    val_reverse_binary += surplus *(2**(i-1))
    i -= 1
print('The decimal of %s is %d'%(reverse_binary,val_reverse_binary))



azaz