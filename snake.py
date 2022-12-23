import turtle as t

UP= 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    pos= 0

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]


    def create_snake(self):
        for i in range(3):
            self.add_segment(i)


    def add_segment(self, position):
        segment = t.Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(self.pos - 20, 0)
        self.pos -= 20
        self.snake.append(segment)

    def extend_snake(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for segment_number in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment_number - 1].xcor()
            new_y = self.snake[segment_number - 1].ycor()
            self.snake[segment_number].goto(new_x, new_y)

        self.head.forward(20)

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

