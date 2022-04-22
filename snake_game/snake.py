from turtle import Turtle 

move_distance = 20

starting_position = [(0,0),(-20,0),(-40,0)]

up = 90
down = 270
left = 180
right = 0

class Snake:

    def __init__(self):
        self.segments_list = []
        self.create_snake()
        self.head = self.segments_list[0]
    
    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.segments_list[-1].position())

    def add_segment(self,position):
        segment = Turtle(shape='square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segments_list.append(segment)
        
    
     
    def move(self) :
        for seg_num in range(len(self.segments_list) -1, 0, -1,):
                new_x = self.segments_list[seg_num - 1].xcor()
                new_y = self.segments_list[seg_num - 1].ycor()
                self.segments_list[seg_num].goto(new_x,new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def reset(self):
        for seg in self.segments_list:
            seg.goto(1000,1000)
        self.segments_list.clear()
        self.create_snake()
        self.head = self.segments_list[0]