from turtle import *
screen= Screen()
Kevin=Turtle()
Kevin.screen.canvheight
Kevin.screen.setup(width=500, height=500)
y_position=[-70,-40,-10, 20, 50, 80]
for turtle_index in range(0,6):
    Kevin=Turtle(shape="turtle")
    Kevin.color("red")
    Kevin.penup()
    Kevin.goto(x=-230, y=y_position[turtle_index])

turtle_colors = ["blue", "green", "orange", "purple", "yellow", "pink"]

screen.textinput(title="Bettign window", prompt="Place your bet and choose a color ")


#create a list of different colors
#eacH turtle has to be a different color
#find a function that lets you choose the color of the turtle
# make a menu that asks for a bet and color



# def pattern(gap):
#     for _ in range(int(360/gap)):
#         Kevin.color(random_color())
#         Kevin.circle(50)
#         Kevin.speed("fastest")
#         Kevin.setheading(Kevin.heading()+gap)


# def random_color():
#     red = random.randint(0,255)
#     green =random.randint(0,255)
#     blue = random.randint(0,255)
#     color= (red, green, blue)
#     return color

# pattern(10)

def move_forward():
    Kevin.forward(10)

def move_backward():
    Kevin.backward(10)

def move_left():
    new_heading=Kevin.heading()+10
    Kevin.setheading(new_heading)

def move_right():
    new_heading=Kevin.heading()-10
    Kevin.setheading(new_heading)

def clear():
    Kevin.clear()
    Kevin.penup()
    Kevin.home()
    Kevin.pendown()

Kevin.screen.listen()
Kevin.screen.onkey(key="w", fun=move_forward)
Kevin.screen.onkey(key="s", fun=move_backward)
Kevin.screen.onkey(key="a", fun=move_left)
Kevin.screen.onkey(key="d", fun=move_right)
Kevin.screen.onkey(key="c", fun=clear)

Kevin.screen.bye(exitonclick())