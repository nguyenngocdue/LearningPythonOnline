""" Kỹ thuật đặc lính canh:
    - Nhập vào mảng 1 chiều các số nguyên. Tìm phần tử lớn nhất.
"""
def searchMax(lst):
    lst_num = [val for val in lst if type(val) == int]

    # gán cho value đầu là lớn nhất >> đem đi so sánh các value tiếp.
    check = int(lst_num[0])
    for i in lst_num:
        if int(i) >= check:
            check = i
    return check

""" Kỹ thuật đặt cờ hiệu:
    - Kiểm tra mảng có toàn là phần tử chẳng hay không
"""
def checkEven(lst):
    check = True # flag at here.
    for i in lst:
        if i % 2:
            check = False
            break
    return check 

""" Kỹ thuật đếm"""

"""Đếm số lần xuất hiện + index + phần tử xuất hiện trong một mảng của 1 phần tử."""
def count_index_Item(lst, item):
    count = 0
    idx = []
    for index, val in enumerate(lst):
        if val == item:
            count += 1
            idx.append(index)
    return count, idx

""" Lấy giá trị index mà phần tử đó xuất hiện trong List"""
def getIndex (lst, item):
    index = [idx for idx in range(len(lst)) if lst[idx] == item]
    return item,index

""" Đếm số cấu kiện xuất hiện trong List """
# Cách 1:
def countItem(lst):
    item = []
    count_item = []
    for val in lst:
        if val not in item:
            item.append(val)
            count_item.append(1)
        else:
            index_item = item.index(val)
            count_item[index_item] += 1
    return item, count_item
# Cách 2:
def countItemDic(lst):
    count = {}
    for i in lst:
        if i in count:
            count[i] += 1 # save at value
            #print(count)
        else:
            count[i] = 1
    return count
# Kiểm tra số lần xuất hiện phần tử đó trong List
def countItem_InList(lst,obj):
    return lst.count(obj)





if __name__ == '__main__':
    lst = [0,1,2,'a','b','c',"a","b"]
    out = countItem_InList(lst,"a")
    print(out)




""" 
+ OOP
+ C#, C# Form.
+ Duyệt mảng, ................
+ Kỹ thuật lập trình >> 
+ Học C++ để học cách giải thuật

1 - 


"""