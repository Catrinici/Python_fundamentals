# 1.Given
# -How would you change the value 10 in x to 15?  Once you're done x should then be[[5, 2, 3], [15, 8, 9]].

# -How would you change the last_name of the first student from 'Jordan' to "Bryant"?

# -For the sports_directory, how would you change 'Messi' to 'Andres'?

# -For z, how would you change the value 20 to 30?

# x = [[5,2,3],[10,8,9]]
# x[1][0] = 15
# print(x)
# students = [
#     {'first_name': 'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# sports_directory = {
#     'basketball':['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer':['Messi', 'Ronaldo', 'Rooney']
# }
# z=[{'x':10, 'y':20}]

# students[0]['last_name'] = "Briant"
# print(students)
# sports_directory['soccer'][0] = "Andrei"
# print(sports_directory)
# z[0]['y'] = 30
# print(z)

# 2.Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list:
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]
# def iterateDictionary(students):
#     for person in students:
#         for key,val in person.items():
#             print('{} - {}' .format(key,val))

# iterateDictionary(students)

# 3.Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output
# def iterateDictionary2(students):
#     for person in students:
#         print(person.get('first_name'))
# iterateDictionary2(students)

