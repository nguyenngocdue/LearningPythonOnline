""" 
- Kiểu dữ liệu hỗn hợp chưa nhiều kiểu giá trị
- Chuỗi giá trị có tính thự tự, có thể được truy cập nẫu nhiên theo chỉ số.

+ list rỗng
+ các phần tử cùng 1 kiểu dữ liệu
+ các phẩn tử khác kiểu dữ liệu
+ có thể lòng 1 list khác vào list ban đầu.

2. Access elements:
    - lits: có tính thứ tự có thể truy cập ngẫu nhiên, thông qua chỉ số.
    - Chỉ số băt đầu từ 0
--> có giá trị trong khoảng 0 => số phần tử của list -1
--> nếu một list có lồng vào 1 list khác chỉ choi là một phần tử
--> đọc và ghi giá trị bằng chỉ số
"""
lst = [1,2,3,"a", ["b","c",]]
print(lst)
print (lst[4])
print(lst[4][1])

"""  
b. Truy cập phẩn tử bằng chỉ số âm

Element  :        e1   e2  e3  e4  e5
Pos Index:        0    1    2   3   4
Neg Index:       -5    -4   -3   -2   -1

Khoảng giá trị đi từ -len(l) (phần tử đầu tiên) -1
tác dụng truy cập bằng chỉ số âm: để get phần tử cuối cùng.
"""

"""  
c. Slicing (Truy cập chỉ số đoạn cắt)

Element  :        e1   e2  e3  e4  e5
Pos Index:        0    1    2   3   4
Neg Index:       -5    -4   -3   -2   -1

Slicing:
- l[start:stop]
- l[start: top : step]


"""

a = [1,2,3,4,5,6]
print(a[:3])
print(a[::-1])
print(a[-2::])





