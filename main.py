from turtle import Screen, Turtle
import time
from snake import Snake, Food

food = Food()
screen = Screen()
screen.setup(width=604, height=604)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
pen = Turtle()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

score = 0
speed = 0.065
game_over = False
while not game_over:
    screen.update()
    time.sleep(speed)
    snake.move(20)
    pen.color("white")
    pen.penup()
    pen.setposition(-250, -250)
    pen.write(f"Current score: {score}", font=("Arial", 16, "normal"), align="left")
    pen.color("black")

    if snake.head.distance(food) < 14:
        score += 1
        food.refresh()
        pen.clear()
        snake.extend_snake()

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        screen.clear()
        game_over = True

    # body collision
    for part in snake.snake_body:
        if snake.head.position() == part.position():
            pass
        elif snake.head.distance(part) < 15:
            screen.clear()
            game_over = True

screen.bgcolor("black")
pen.setposition(0, 0)
pen.color("yellow")
if score < 2:
    pen.write(f"Game over! You suck! \nFinal score: {score}", font=("Times New Roman", 40, "normal"), align="center")
elif 2 < score < 10:
    pen.write(f"Game over! Nice try! \nFinal score: {score}", font=("Times New Roman", 40, "normal"), align="center")
else:
    pen.write(f"Game over! Good Job! \nFinal score: {score}", font=("Times New Roman", 40, "normal"), align="center")

screen.exitonclick()
