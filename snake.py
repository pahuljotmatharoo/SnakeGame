from turtle import Turtle
import random

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(4):
            snake_part = Turtle()
            snake_part.shape("square")
            snake_part.color("blue")
            snake_part.penup()
            snake_part.goto(x=(20 * i), y=0)
            self.snake_body.append(snake_part)

    def move(self, distance):
        self.head.forward(distance)
        for i in range(len(self.snake_body) - 1, 0, -1):
            position = self.snake_body[i - 1].pos()
            self.snake_body[i].goto(position)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend_snake(self):
        snake_part = Turtle()
        snake_part.shape("square")
        snake_part.setposition(-400, -400)
        snake_part.penup()
        self.snake_body.append(snake_part)
        snake_part.color("blue")


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.color("white")
        x_cord = random.randrange(-280, 280, 20)
        y_cord = random.randrange(-280, 280, 20)
        self.goto(x_cord, y_cord)

    def refresh(self):
        new_x = random.randrange(-280, 280, 20)
        new_y = random.randrange(-280, 280, 20)
        self.goto(new_x, new_y)