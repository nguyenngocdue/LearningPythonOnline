""" 
Task
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20 , print Weird
If  is even and greater than 20, print Not Weird
Input Format
A single line containing a positive integer, .
Constraints: 0 <= n <=100
"""
######################################################################

# n = int(input().strip())
# check = {True: "Not Weird", False: "Weird"}
# print(check[n%2==0 and (n in range(2,6) or n > 20)])

# n = int(input())
# while n <0 or n > 100:
#     n = int(input())
#     break

""" In the Python 2 solution, there is an explicit test first: if n % 2 == 1.
The Python 3 solution shows a short version of the same test.
n % 2 returns 1 (True) or 0 (False), so the == 1 can be omitted. """

# if n % 2:
#     print('Weird')
# elif 2 <= n <= 5: 
#     print('Not Weird')
# elif 6 <= n <= 20:
#     print('Weird')
# else:
#     print('Not Weird')

""" Also, the Python 3 solutions rely on the fact that if the first test is True (the value is odd),
any value that gets beyond that stanza will be even. No more modulo divisions are necessary. 
2-->5 : Not weird (even)
6-->20 : Weird (even)
> 20 : Not weird (even)
"""

n = int(input().strip())
if (n % 2 or 6 <= n <= 20): # or: true + false --> true
    print("Weird")
else:
    print("Not weird")