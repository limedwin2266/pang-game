from turtle import Turtle, Screen
from paddle import Paddle
#Create a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pang")

#Create a paddle
paddle = Paddle()
paddle.paddle_shape()

screen.listen()
screen.onkey(paddle.up,"Up")
screen.onkey(paddle.down,"Down")








screen.exitonclick()