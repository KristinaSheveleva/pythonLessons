from turtle import *
import random
screen= Screen()
screen.setup(width=500, height=500)
y_position=[-70,-40,-10, 20, 50, 80]
user_bet= screen.textinput(title="Bettign window", prompt="Choose a color of a turtle you want to bet on ")
turtle_colors = ["blue", "green", "orange", "red", "yellow", "pink"]
turtle_list=[]


for turtle_index in range(0,6):
    Kevin=Turtle(shape="turtle")
    Kevin.color(turtle_colors[turtle_index])
    Kevin.penup()
    Kevin.goto(x=-230, y=y_position[turtle_index])
    turtle_list.append(Kevin)


if user_bet:
    game_on= True
    
while game_on:
    for turtle in turtle_list:
        if turtle.xcor()>230:
            game_on=False
            if turtle.pencolor()== user_bet:
                print(f"You won! The {turtle.pencolor()} turtle is the winner")
                
            else:
                print(f"You lost! The {turtle.pencolor()} turtle is the winner")
        turtle.forward(random.randint(0,10))
        
        
screen.exitonclick()