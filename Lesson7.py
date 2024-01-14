#1 for numbers in range(1,11):
#     print(numbers)

#2 range_input=int(input("Give me a range of numbers:"))

# for numbers in range(0, range_input+1):
#     if numbers % 2==0:
#         print(numbers)
    
#3 inputnum=int(input("Give me a range number:"))

# total=0

# for number in range(1,inputnum+1):
#     total+=number
# print(total)

#4 given_range=int(input("Give me a range of numbers:"))

# total=0

# for number in range(0, given_range+1):
#     if number % 2 !=0:
#         total+=number
# print(total)

#5 chislo=int(input("Give me a number:"))

# for number in range(1,10):
#     print(f"{chislo} x {number}=", chislo*number)

#6 numb_list=[1,56,4,27,59,100,42,5]
# for numbers in numb_list:
#     print(numbers)

#7 numb_input=input("Give me a number:")
# count=0

# for number in numb_input:
#     count+=1
# print(count)

#8(INTERVIEW QUESTION) word=input("Give me any word:")
# reverse_word=""

# for leters in word:
#     reverse_word=leters+reverse_word

# if reverse_word==word:
#     print("The word is palindrome!")
# else:
#     print("the word is NOT palindrome!")

#9(INTERVIEW QUESTION) word=input("Write any word:")
# reverse=""

# for letters in word:
#     reverse=letters+reverse
# print(reverse)

#10 numbInput=input("Write a number:")
# length=input("Give me a length of a number:")
# sum=0
# for number in numbInput:
#     sum+=int(number)**int(length)

# if sum==int(numbInput):
#     print("This number IS an Armstrong number")
# else:
#     print("This number is NOT an Armstrong number")

#11 numbList=[1,47,89,2,3,246,7190,6,5,23]
# countEven=0
# countOdd=0
# for number in numbList:
#     if number %2==0:
#         countEven+=1
#     elif number %2 !=0:
#         countOdd+=1
# print(countEven)
# print(countOdd)

#12 for num in range (1,101):
#     flag = False
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break
#     if flag:
#         print(num)

#13 number1=0
# number2=1

# for num in range(0,51):
#     if num<1:
#         next_number= num
#     else:
#         next_number=number1+number2
#         number1=number2
#         number2=next_number
#     print(next_number)

#14 number=int(input("Give me a number:"))
# factorial=1
# for num in range(1, number+1):
#     factorial=num*factorial
# print(factorial)
    



#15 text = input("Enter a mix text: ")
# letters = 0
# digits = 0

# for char in text:
#     if char.isalpha():
#         letters += 1
#     elif char.isdigit():
#         digits += 1

# print(f"Letters: {letters}")
# print(f"Digits: {digits}")

#16 for i in range(1, 26):
#     print(i)

#17

#18 month = input("Give me a month names:")
# month_list=month.split(", ")

# for month in month_list:
#     if month == "February":
#         print("February has 28/29 days")
#     elif month == "April" or month== "June" or month== "September" or month== "November":
#             print(month,"has 30 days.")
#     elif month == "January" or month== "March" or month== "May" or month== "July" or month== "August"or month== "October" or month== "December":
#                 print(month,"has 31 days.")
#     else:
#         print("Check the spelling.")