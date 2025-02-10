from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments = []
    def create_snake(self):
        for i in range(3):
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(i*-20, 0)
            self.segments.append(segment)
    def add_segment(self, position):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for i in range(len(self.segments)-1, 0 , -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(20)
    def right_move(self):
        if (self.segments[0].heading() == 270):
            self.segments[0].left(90)
        else:
            self.segments[0].right(90)
    def left_move(self):
        if (self.segments[0].heading() == 270):
            self.segments[0].right(90)
        else:
            self.segments[0].left(90)
    def up(self):
        if ( self.segments[0].heading() != 270 and self.segments[0].heading() != 90):
            self.segments[0].setheading(90)
    def down(self):
        if ( self.segments[0].heading() != 270 and self.segments[0].heading() != 90):
            self.segments[0].setheading(270)