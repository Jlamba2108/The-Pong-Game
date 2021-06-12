from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
player_name1 = screen.textinput(title=" ", prompt="Enter Player 1 Name :")
player_name2 = screen.textinput(title=" ", prompt="Enter Player 2 Name :")
screen.title(f"Pong Game")
# Instructions
instruction1 = Turtle()
instruction1.color("white")
instruction1.penup()
instruction1.hideturtle()
instruction1.goto(-200, -270)
instruction1.write(f"Player 1: {player_name1}\nPress 'Q' to move up or \n'A' to move down ", align="center",
                   font=("Courier", 15, "bold"))

instruction2 = Turtle()
instruction2.color("white")
instruction2.penup()
instruction2.hideturtle()
instruction2.goto(200, -270)
instruction2.write(f"Player 2: {player_name2}\nPress 'K' to move up or \n'M' to move down ", align="center",
                   font=("Courier", 15, "bold"))

# Divide screen
div_screen = Turtle()
div_screen.shape("square")
div_screen.shapesize(stretch_wid=26, stretch_len=0.15)
div_screen.color("white")
div_screen.penup()
div_screen.goto(0, -10)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "k")
screen.onkey(r_paddle.go_down, "m")
screen.onkey(l_paddle.go_up, "q")
screen.onkey(l_paddle.go_down, "a")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 279 or ball.ycor() < -279:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        game_is_on = False

# End game
game_finish = Screen()
game_finish.clear()
game_finish.bgcolor("black")
game_finish.setup(width=800, height=600)

# Display Winner
display_winner = Turtle()
display_winner.color("white")
display_winner.penup()
display_winner.hideturtle()
display_winner.goto(0, 0)
if scoreboard.r_score == 10:
    display_winner.write(f"Game Over! \nWinner is Player 2:\n{player_name2}", align="center",
                         font=("Courier", 30, "bold"))
if scoreboard.l_score == 10:
    display_winner.write(f"Game Over! \nWinner is Player 1:\n{player_name1}", align="center",
                         font=("Courier", 30, "bold"))

screen.exitonclick()