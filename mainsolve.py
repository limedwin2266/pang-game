from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pang")
screen.tracer(0) #close the animation, but need to update again
ball = Ball()
scoreboard = Scoreboard()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))


screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"W")
screen.onkeypress(l_paddle.go_down,"S")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collusion
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounce
        ball.bounce_y()
    
    #Detect collusion with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle) <50 and ball.xcor()< -320:
        ball.bounce_x()

    #Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    #Detect when left paddle misses
    if ball.xcor() <-380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()