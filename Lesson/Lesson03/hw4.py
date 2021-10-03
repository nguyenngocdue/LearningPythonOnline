"""
Bài 4: Mật mã Caesar
    Caesar là một vị hoàng đế La Mã, ông ta cũng là một tướng lĩnh tài ba. Để đảm
    bảo bí mật quân sự, ông ta tạo ra một bộ mã hóa như sau:
    - Một kí tự được dịch đi một khoảng cách d là một số nguyên (0 < d < 26)
    - Nếu việc dịch đó làm ký tự ra ngoài khoảng cho phép, quay vòng về 'a', 'A'
        rồi lại tiếp tục dịch. Ví dụ: d = 2, a -> c, m -> k, z -> b
    * Viết chương trình:
        Cho người dùng lựa chọn chế độ:
            - 0. thoát chương trình.
            - 1. mã hóa
            - 2. giãi mã
    Với chế độ 1,2
            - Nhập vào khoảng cách d.
            - Nhập vào một chuỗi s.
            - Đưa ra kết quả tương ứng.
        (Lưu ý: Phân biệt chữ hoa - thường)
"""
while True:
    print ('------------------------------------------------')
    c = input('0. Exit     1.Encrypt     2.Decrypt\nYour choice: ')

    if c == '0':
        break
    if (c != '1') and (c != '2'):
        print ('Invalid input')
        continue

    while True:
        d = int(input('Enter distance d (0 < d < 26): '))
        if 0 <= d <= 26:
            break
        print('Invalid input, try again!')
    
    while True:
        s = input('Enter a sequence without digit and special char:')

        is_valid = True
        for current_char in s:
            is_valid_current_char = 'a' <= current_char <= 'z' or 'A' <= current_char <= 'Z'
            
            if not is_valid_current_char:
                is_valid =  False
                print(f'Input {s}: {current_char} invalid')
                break
        if is_valid:
            break
        
    if c == '1':
        result = ''
        for current_char in s:
            if 'a' <= current_char <= 'z':
                curverted_pos = ord(current_char) + d
                if converted_pos > ord('z'):
                    converted_pos -= 26
                result = f'{result}{chr(converted_pos)}'
            if 'A' <= current_char <= 'Z':
                converted_pos = ord(current_char) + d
                if converted_pos > ord('Z'):
                    converted_pos -= 26
                result = f'{result}{chr(converted_pos)}'
        print(f'Encrypt {s} with {d}:', result)

    else:
        result = ''
        for current_char in s:
            if 'a' <= current_char <= 'z':
                converted_pos = ord(current_char) - d
                if converted_pos < ord('a'):
                    converted_pos += 26
                result = f'{result}{chr(converted_pos)}'
            if 'A' <= current_char <= 'Z':
                converted_pos = ord(current_char) - d
                if converted_pos < ord('A'):
                    converted_pos += 26
                result = f'{result}{chr(converted_pos)}'
        print(f'Decrypt {s} with {d}', result)






