#Conditionals
#STANDART "IF" STATEMENT

# height=int(input('What is you height?'))
# if height>= 140:
#     print("You can ride!")
# else:
#     print("You can't ride!")

# number=int(input("Give me a number:"))
# if number%2==0:
#     print("The number is even!")
# else:
#     print("The number is odd!")

#NESTED "IF" STATEMENT:

# height=int(input('What is you height?'))
# if height>= 140:
#     print("You can ride!")
#     age=int(input("What's your age?"))
#     if age>=18:
#         print("Please pay $10")
#     else:
#         print("Please pay $5")
# else:
#     print("You can't ride!")

weight=int(input("What is your weight?"))
height=float(input("What is your height?"))
bmi=weight/height**2
if bmi<=18.5:
    print("You are underweight")
elif bmi<=25:
    print("You have a normal weight!")
elif bmi<=30:
    print("You are slightly overweight!")
elif bmi<=35:
    print("You are obese!")
else:
    print("You are clinically obese!")

