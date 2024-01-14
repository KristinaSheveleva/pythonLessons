# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
  
# # TODO: Add more code here 👇
# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   if month== 2 and is_leap(year):
#     return 29
#   else:
#     return month_days[month-1]   

# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year, month)
# print(days)



# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# dictionary={
#     0: 10, 
#     1: 20
# }


# Write a Python script to check whether a given key already exists in a dictionary.

    # key=int(input())

    # if key in dictionary:
    #     print("It already exists")
    # else:
    #     print("It does not exist in the dictionary")

# Write a Python script to print a dictionary 
# where the keys are numbers between 1 and 15 (both included) 
# and the values are the square of the keys.

dict1={}

for key in range(1,16):
    # dict1[key]=key**2
    dict1.update({key:key**2})

print(dict1)
