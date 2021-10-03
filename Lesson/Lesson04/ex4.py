while True:
    n = int(input('Enter N number: '))
    break
lst_a = []
for i in range(n):
    lst_a.append(int(input('Enter possitive N number : ')))
print(lst_a)

flag = True
start = 1
dem = 0
in_count = 0
out_count = 0
for i in lst_a:
    if i in lst_a[::]:
        in_count += 1
    else:
        out_count += 1
# if flag == False:
#     dem +=1
print('IN:',in_count, 'OUT:',out_count )


