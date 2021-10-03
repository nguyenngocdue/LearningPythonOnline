while True:
    n = int(input(' Enter amount n :'))
    break
a = []
for i in range(n):
    a.append(input('Enter value n: '))
print(f'List a is {a}')

b = []
for i in a:
    b.append(i)
print(f"List b is: {b}")

c = []
for i in a[::-1]:
    c.append(i)
print(f"List c is: {c}")

get =  int(input(' Enter a number to get value: '))
print(a[get])

