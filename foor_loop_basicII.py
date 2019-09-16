# 1.Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to[-1, "big", "big", -5].
# def makeItBig(list):
#     newlist=[]
#     for i in list:
#         if i > 0:
#             i = "big"
#         newlist.append(i)
#     return(newlist)
    

# print(makeItBig([-1,3,5,-5]))

# 2.Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1, 1, 1, 1]) changes array to[-1, 1, 1, 3] and returns it.  (Note that zero is not considered to be a positive number).
# import random
# def replaceLastVal(list):
#     x = random.randint(1, 10)
#     list.pop()
#     list.append(x)
#     return(list)
# print(replaceLastVal([3,4,5,6,7]))

# 3.SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1, 2, 3, 4]) should return 10
# def sumTotal(list):
#     sum = 0
#     for i in list:
#         sum += i
#     print("The total Sum is", sum)
# sumTotal([1, 2, 3, 4])
    
# 4.Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1, 2, 3, 4]) should return 2.5
# def averageFun(list):
#     sum = 0
#     x = len(list)
#     for i in list:
#         sum += i
#     return("Average is: ", sum/x)
    
# print(averageFun([1, 2, 3, 4]))

# 5.Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1, 2, 3, 4]) should return 4
# def length(list):
#     return(len(list))
# print(length([1, 2, 3, 4]))

# 6.Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1, 2, 3, 4]) should return 1
# minimum([-1, -2, -3]) should return -3.
# def minimum(list):
#     if len(list) == 0:
#         return False
#     min = list[0]
#     for i in list:
#         if i < min:
#             min = i
#     return(min)
# print(minimum([6, 2, 3, 4]))
    
# 7.Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1, 2, 3, 4]) should return 4
# maximum([-1, -2, -3]) should return -1.
# def maximum(list):
#     if len(list) == 0:
#         return False
#     max = list[0]
#     for i in list:
#         if i > max:
#             max = i
#     return(max)

# print(maximum([1, 2, 3, 4]))
# print(maximum([-2,-3,-1]))
# print(maximum([]))

# 8.UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
# def UltimateAnalyze(list):
#     if len(list) == 0:
#          return False
#     x = len(list)
#     min = list[0]
#     max = list[0]
#     sum = 0
#     obj = {}
#     for i in list:
#         if i < min:
#             min = i         
#         if i > max:
#             max = i     
#         sum += i
#     avg = sum/x
#     min = obj.setdefault('min',min)
#     max = obj.setdefault('max',max)
#     sum = obj.setdefault('sum', sum)
#     avg = obj.setdefault('avg', avg)
#     x = obj.setdefault('length', x)
#     return(obj)
# print(UltimateAnalyze([8, 2, 3, 4]))

# 9.ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1, 2, 3, 4]) should return [4, 3, 2, 1]. This challenge is known to appear during basic technical interviews.
# def reverse(lst):
#     i = 0            # first item
#     j = len(lst)-1   # last item
#     while i < j:
#         lst[i], lst[j] = lst[j], lst[i]
#         i += 1
#         j -= 1
#     return lst


# print(reverse([8, 2, 3, 4,7]))

