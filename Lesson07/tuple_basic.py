# Packing
# Unpacking



# my_tuple = 1, 2, 3 # Packing tuple
# print(my_tuple, type(my_tuple))

# print(*my_tuple)
# print(type(*my_tuple))
#----------------------------------------------------------------
"""
- Lấy ra 2 phần tử đầu tiên của my_tuple lưu vào biến a, b, còn lại  lưu  vào biến c ở dạng mảng

- Lấy ra 2 phần tử cuối cùng của my_tuple lưu vào biến a, b, còn lại  lưu  vào biến c ở dạng mảng

- Lấy 1 phần tử đầu, 1 phần tử cuối của my_tuple lưu vào a, b. Còn lại lưu vào c dưới dạng mảng
"""

my_tuple = 1, 2, 3, 4, 5, 'a', 'b' # Packing tuple
a, b, *c = my_tuple
print(a, b, c) #UnPacking Tuple

a, b, c, d = 1, 2, 3, 4 #Unpacking --> nó không liên quan đến gì về biến, nó ứng dụng trên VT = Packing : VP = Unpacking
print(a, b, c, d)

""" 
Về nhà đọc thêm:
    - Dictionary và dấu ** --? làm ơn nhớ đọc giúp!
"""