from turtle import Turtle

MOVE_DISTANCE = 20
UP, DOWN, RIGHT, LEFT = 90, 270, 0, 180

class Snake:
    def __init__(self, length):
        self.color = "white"
        self.length = length
        self.starting_position = [(0 - 20 * i, 0) for i in range(self.length)]
        self.segments = self.create_snake()
        self.head = self.segments[0]
        self.DIRECTION = "right"


    def create_snake(self):
        segments = []
        for position in self.starting_position:
            new_segment = Turtle("square")
            new_segment.up()
            new_segment.color(self.color)
            new_segment.goto(position)
            segments.append(new_segment)
        return segments

    def go_up(self):
        if self.DIRECTION != "down":
            self.head.setheading(UP)
            self.DIRECTION = "up"
            
    def go_down(self):
        if self.DIRECTION != "up":
            self.head.setheading(DOWN)
            self.DIRECTION = "down"

    def go_left(self):
        if self.DIRECTION != "right":
            self.head.setheading(LEFT)
            self.DIRECTION = "left"

    def go_right(self):
        if self.DIRECTION != "left":
            self.head.setheading(RIGHT)
            self.DIRECTION = "right"

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(self.color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        self.color = "white"
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.segments = self.create_snake()
        self.head = self.segments[0]        

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def change_color(self):
        self.color = "blue"
        for segment in self.segments:
            segment.color(self.color)