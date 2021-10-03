def CreateCellCaro(n):
    # n: enter length and width of Caro: nxn
    # Create Empty list
    lstCaro = [[] for i in range(n)]
    t = 0
    checksign = [0,1,2]
    for i in lstCaro:
        for j in range(n):
            value = int(input(f"Enter value row {t+1}, column {j+1}: "))
            while value not in checksign:
                value = int(input(f"One more time,Enter value row {t+1}, column {j+1}: "))
            lstCaro[t].append(value)
        t  += 1
    return lstCaro

def checkWin(lst,persign):
    # a: nxn
    a = lst
    for x in range(len(a)):
        for y in range(len(a)):
            #check row
            count = 0
            i, j = x, y
            while (j < len(a) and a[i][j] == persign):
                count += 1
                j += 1 # kiem tra phia truoc

                # nếu 4 số 1 liên tiếp, 2 đầu là 0 thì thắng
                # j - 5 < 0 sẽ bị đảo list 
                try:
                    if count == 4 and a[i][j] == a[i][j-5] == 0:
                        return True
                except:
                    pass
                if count >= 5:
                    return True

            j = y
            while (j -1 >= 0 and a[i][j-1] == persign):
                count += 1
                j -= 1 # kiểm tra vị trí sau lưng
                if count >= 5:
                    return True


            #check column
            count = 0
            i, j = x, y
            while (i < len(a) and a[i][j] == persign):
                count += 1
                i += 1
                # nếu 4 số 1 liên tiếp, 2 đầu là 0 thì thắng
                try:
                    if count == 4 and a[i][j] == a[i-5][j] == 0:
                        return True
                except:
                    pass
                if count >= 5:
                    return True
            i = x
            # check column i-1, j phía bên trên
            while (i-1 >= 0 and a[i-1][j] == persign):
                count += 1
                i -= 1
                if count >= 5:
                    return True
            # check column i+1, j phía bên dưới
            i, j = x, y
            count = 0
            while (i < (len(a)-1) and a[i+1][j] == persign):
                count += 1
                i += 1
                if count >= 5:
                    return True
                try:
                    if count == 4 and a[i+1][j] == a[i-4][j] == 0:
                        return True
                except:
                    pass

            #check cheo phai
            count = 0
            i, j = x, y
            while (i < len(a) and j < len(a) and a[i][j]) == persign: #phia tren
                count += 1
                i -= 1
                j += 1
                # nếu 4 số 1 liên tiếp, 2 đầu là 0 thì thắng
                try:
                    if count == 4 and a[i][j] == a[i+1][j-1] == 0:
                        return True
                except:
                    pass
                if count >= 5:
                    return True
            if count >= 5:
                return True

            i, j = x, y
            while(i + 1 < len(a) and j - 1 >= 0 and a[i+1][j-1]) == persign: # phia duoi
                count += 1
                i += 1
                j -= 1
                try:
                    if count == 4 and a[i+1][j-1] == a[i-4][j+4] == 0:
                        return True
                except:
                    pass
                if count >= 5:
                    return True

            # check cheo trai
            count = 0
            i, j = x, y
            while (i-1 >= 0 and j-1 >= 0 and a[i][j]) == persign: #phia tren
                count += 1
                i -= 1
                j -= 1
                # nếu 4 số 1 liên tiếp, 2 đầu là 0 thì thắng
                try:
                    if count == 4 and a[i][j] == a[i+5][j+5] == 0:
                        return True
                except:
                    pass
                if count >= 5:
                    return True

            i, j = x, y
            while (i <(len(a)-1) and j < (len(a)-1) and a[i+1][j+1]) == persign: #phia duoi
                count += 1
                i += 1
                j += 1
                #print(i,j)
                try:
                    if count == 4 and a[i+1][j+1] == a[i-4][j-4] == 0:
                        return True
                except:
                    pass
                if count >= 5:
                    return True

# a = [[0,1,0,0,1,0,1],
#      [1,1,2,1,0,1,0],
#      [0,1,1,2,1,0,0],
#      [1,0,1,0,2,1,0],
#      [1,1,0,2,0,2,1],
#      [0,1,2,2,2,2,0],
#      [0,0,0,2,2,0,1]]

n = int(input("Enter the number of item: "))
while n < 5:
    n = int(input("Enter the number of item: "))


a = CreateCellCaro(n)

if checkWin(a,1) == True:
    print("The player with the symbol 1: Win")
elif checkWin(a,2) == True:
    print("The player with the symbol 2: Win")
else:
    print("Keep playing")