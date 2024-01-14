#IFIFIF statements
pizza_size=input("What size of pizza would you like?")
add_pepperoni=input("Would you like pepperoni?")
cheese=input("Would you like any cheese?")
bill=0

if pizza_size=="S":
    bill+=15
elif pizza_size=="M":
    bill+=20
elif pizza_size=="L":
    bill+=25

if add_pepperoni=="Y" and pizza_size=="S":
    bill+=2
else:
    bill+=3

if cheese=="Y":
    bill+=1
print(f"Your final bill is {bill}")