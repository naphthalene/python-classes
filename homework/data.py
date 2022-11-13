#import numpy as np
import math
#Definitions
origin = (0,0)
point_a = (0,0)
point_b = (3,4)
segment_ab = (point_a,point_b)
scale = 4


def move_square(square, move_to):
    """
    Return a new square with new location
    """
    x = square [0][0]
    y = square [0][1]
    scale = square[1]


    return (move_to, scale)

#((x1,y1),scale)
square_a = (point_a,scale)
new_square = move_square(square_a,point_b)

# ----------------------------------
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

point_c = Point(17, -19)

# ----------------------------------
class Segment:
    """
    TODO: implement a line class
    """
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    @property
    def length(self) -> float:
        return math.sqrt((self.a.x - self.b.x)**2 + (self.a.y - self.b.y)**2)

# ----------------------------------
class Square:
    def __init__(self,point: Point, scale: float):
        self.point = point
        self.scale = scale

    @property
    def area(self) -> float:
        """
        Return the area of this square
        self.point and self.scale are available
        """
        return self.scale**2

square_a = Square(Point(3,7),4)

# ----------------------------------
class Triangle:
    def __init__(self,a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c
        self.ab = Segment(a,b)
        self.ac = Segment(a,c)
        self.bc = Segment(b,c)

    @property
    def area(self) -> float:
        """
        TODO: return the area of this triangle
        self.point and self.scale are available
        """
        s = (self.ab.length + self.bc.length + self.ac.length)/2
        return  math.sqrt(s*(s-self.ab.length)*
                         (s-self.ac.length)*
                         (s-self.bc.length))

        

triangle1 = Triangle((5,4),(2-3),(5,-10))
