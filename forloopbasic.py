#1.Basic - Print all the numbers/integers from 0 to 150.
#  for i in range(0,150):
#     print(i)

# 2.Multiples of Five - Print all the multiples of 5 from 5 to 1, 000, 000.
# for i in range(5,1000000):
#     if i%5 ==0:
#         print(i)

# 3.Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
# for i in range(1,100):
#     if i%5:
#         print("Coding")
#     elif i%10==0:
#             print("Coding Dojo")

# 4.Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
# sum = 0
# for i in range(0,500000):
#     if i%2 !=0:
#         sum+=i
#         print(sum)

# 5.Countdown by Fours - Print positive numbers starting at 2018, counting down by fours(exclude 0).
# count = 2018
# while count > 0:
#     print(count)
#     count-=4


def a():
    print(1)
    x = b()
    print(x)
    return 10


def b():
    print(3)
    return 5


y = a()
print(y)
