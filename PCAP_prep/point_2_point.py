import math  # math.hypot(x, y)


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


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
