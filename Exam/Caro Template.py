# def CreateCellCaro(n):
#     # n: enter length and width of Caro: nxn
#     # Create Empty list
#     lstCaro = [[] for i in range(n)]
#     t = 0
#     checksign = [0,1,2]
#     for i in lstCaro:
#         for j in range(n):
#             value = int(input(f"Enter value row {t+1}, column {j+1}: "))
#             while value not in checksign:
#                 value = int(input(f"One more time,Enter value row {t+1}, column {j+1}: "))
#             lstCaro[t].append(value)
#         t  += 1
#     return lstCaro

# n = int(input("Enter the number of item: "))
# while n < 0:
#     n = int(input("Enter the number of item: "))
# a = CreateCellCaro(n)
# print(a)

a = [[1,0,0,0,0,0],
     [0,0,1,1,1,0],
     [1,0,1,1,0,0],
     [1,0,1,0,0,0],
     [0,0,0,0,1,0],
     [0,0,0,1,1,0]]

# play_continue = False
# for x in range(6):
#     check = 0
#     play_continue = True
#     for y in range(6):
#         #check row
#         count = 0
#         i, j = x, y
#         if count < 5:
#             while (j < len(a[0]) and a[i][j] == 1):
#                 count += 1
#                 j += 1 # kiem tra phia truoc
#                 if count >= 5:
#                     break
#                 # nếu 4 số 1 liên tiếp, 2 đầu là 0 thì thắng
#                 # j - 5 < 0 sẽ bị đảo list 
#                 try:
#                     if (j - 5 >= 0 and count == 4 and a[i][j] == a[i][j-5] == 0):
#                         count += 2 # out = 6 => thì bên ngoài sẽ đúng luôn
#                         break
#                 except: "None"   
#         j = y
#         if count < 5:
#             while (j -1 >= 0 and a[i][j-1] == 1):
#                 count += 1
#                 j -= 1 # kiểm tra vị trí sau lưng
#                 if count >= 5:
#                     break
#         if count >= 5:
#             check +=count
#             print("Win")
#             break
#         #check column
#         count = 0
#         i, j = x, y
#         if count < 5:
#             while (i < len(a[0]) and a[i][j] == 1):
#                 count += 1
#                 i += 1
#                 # nếu 4 số 1 liên tiếp, 2 đầu là 0 thì thắng
#                 try:
#                     if (i - 5 >= 0 and count == 4 and a[i][j] == a[i-5][j] == 0):
#                         count += 2 #= 6 => thì bên ngoài sẽ đúng luôn
#                         break
#                 except: "None"
#                 if count >= 5:
#                     break
#         i = x
#         if count < 5:
#             while (i-1 >= 0 and a[i-1][j] == 1):
#                 count += 1
#                 i -= 1
#                 if count >= 5:
#                     break
#         if count >= 5:
#             check +=count
#             print("Win")
#             break

#         #check cheo phai
#         count = 0
#         i, j = x, y
#         while (i < len(a[0]) and j < len(a[0]) and a[i][j]) == 1: #phia tren
#             count += 1
#             i -= 1
#             j += 1
#             # nếu 4 số 1 liên tiếp, 2 đầu là 0 thì thắng
#             try:
#                 if (j - 1 >= 0 and i - 1 >= 0 and count == 4 and a[i][j] == a[i+1][j-1] == 0):
#                     count += 2
#                     break
#             except: "None"
#             if count >= 5:
#                 break
#         i, j = x, y

#         while(0 <= i - 1 and i + 1 < len(a) and j - 1 >= 0 and a[i+1][j-1]) == 1: # phia duoi
#             count += 1
#             i += 1
#             j -= 1
#             #print("i = ", i, "j =" , j, "count",count -1)
#             if count >= 5:
#                 break
#         if count >= 5:
#             check +=count
#             print("Win")
#             break
#         # check cheo trai
#         count = 0
#         i, j = x, y
#         while (i <len(a[0]) and j < len(a[0]) and a[i][j]) == 1: #phia duoi
#             count += 1
#             i += 1
#             j += 1
#             # nếu 4 số 1 liên tiếp, 2 đầu là 0 thì thắng
#             try:
#                 if (i - 1 >= 0 and j -1 >= 0 and count == 4 and a[i][j] == a[i-1][j-1] == 0):
#                     count += 2
#                     break
#             except: "None"
#             if count >= 5:
#                 break
#         i, j = x, y
#         while (i-1 >= 0 and j-1 >= 0 and a[i-1][j-1]) == 1: #phia tren
#             count += 1
#             i -= 1
#             j -= 1
#             if count >= 5:
#                 break
#         if count >= 5:
#             check +=count
#             print("Win")
#             break
#     if check >= 5:
#         break
# if play_continue:
#     print("Keep playing", play_continue)

re = []
for i in a:
    re.append(i + [])
print(re)