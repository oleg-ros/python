'''
the constructor accepts three arguments - all of them are objects of the Point class;
the points are stored inside the object as a private list;
the class provides a parameterless method called perimeter(), which calculates the perimeter of the triangle described by the three points; the perimeter is a sum of all legs' lengths (we mention it for the record, although we are sure that you know it perfectly yourself.)
'''


import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        hypot_x = x - self.__x
        hypot_y = y - self.__y
        return math.hypot(hypot_x, hypot_y)

    def distance_from_point(self, point):
        hypot_x = point.getx() - self.__x
        hypot_y = point.gety() - self.__y
        return math.hypot(hypot_x, hypot_y)


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        dist1 = self.__vertices[0].distance_from_point(self.__vertices[1])
        dist2 = self.__vertices[1].distance_from_point(self.__vertices[2])
        dist3 = self.__vertices[2].distance_from_point(self.__vertices[0])
        return dist1 + dist2 + dist3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
