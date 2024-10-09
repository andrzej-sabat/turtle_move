import turtle
import random
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle win the race? Enter color: ")

for i, color in enumerate(colors):
    t = Turtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.goto(x=-230 , y= -130 + (i * 50))
    turtles.append(t)


is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:


    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win, {winning_color} turtle wins!")
            else:
                print(f"You loose. You bet on {user_bet} turtle and {winning_color} turtle wins.")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
# def forward():
#     turtle.fd(10)
# def backward():
#     turtle.bk(10)
# def counter_clockwise():
#     turtle.seth(turtle.heading() - 5)
# def clockwise():
#     turtle.seth(turtle.heading() + 5)
# def clear():
#     turtle.penup()
#     turtle.clear()
#     turtle.home()
#     turtle.pendown()
#
# screen.listen()
# screen.onkey(key="w", fun=forward)
# screen.onkey(key="s", fun=backward)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear)






