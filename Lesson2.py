#number="23"
#print(int(number[0])+int(number[1]))

#num_char = str(len(input("What is your name")))
#print("Your name is " + num_char +" characters")

#name=input("What is your name?")
#age=int(input("How old are you?"))
#human=bool(input("Are you a human?"))
#print("Your name is "+name+" your age is "+str(age)+" you are a human "+str(human))

#weight=int(input("What is tou weight?"))
#height=float(input("What is your height?"))
#bmi=weight/height**2
#print(bmi)
#print(int(bmi))

age=int(input("What is your age?"))
years=90-age
months=years*12
weeks=years*52
days=years*365
print(f"You have {days}, {weeks} weeks, and {months} months left")