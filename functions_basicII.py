# 1.Countdown - Create a function that accepts a number as an input.  Return a new list that counts down by one, from the number(as lists 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5, 4, 3, 2, 1, 0].
# def countDown(num):
#     new=[]
#     while num >= 0:
#         new.append(num)
#         num -= 1
#     return new
# print(countDown(5))

# 2.Print and Return - Your function will receive a list with two numbers. Print the first value, and return the second.
# def printReturn(list):
#     print(list[0])
#     return(list[1])
# print(printReturn([2,4]))
  
# 3.First Plus Length - Given a list, return the sum of the first value in the list, plus the list's length.
# def returnSum(list):
#     return(list[0]+len(list))
# print(returnSum([5,2,3,4,5]))

# 4.Values Greater than Second - Write a function that accepts a list, and returns a new list with the list values that are greater than its 2nd value.  Print how many values this is.  If the list is only one element long, have the function return False
# def greater(arr):
#   sub_arr = []
#   if len(arr) == 0:
#     return False
#   for x in arr:
#     if arr[x] > arr[1]:
#       sub_arr.append(arr[x])
#   print(sub_arr)
#   print(len(sub_arr))

# 5.This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size, and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4, 7) should return [7, 7, 7, 7].
# def lengthAndValue(num1, num2):
#     new_arr = []
#     for x in range(0, num1):
#         new_arr.append(num2)
#     return new_arr
# print(lengthAndValue(4,7))
