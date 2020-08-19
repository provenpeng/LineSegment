import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.data = [float(x), float(y)]

    @property
    def x(self):
        return self.data[0]

    @property
    def y(self):
        return self.data[1]

    def __str__(self):
        return "point(%.2f, %.2f)" % (self.x, self.y)

    def distance(self, pt):
        """
        两点距离
        :param pt:
        :return:
        """
        xDiff = self.x - pt.x
        yDiff = self.y - pt.y
        return math.sqrt(xDiff ** 2 + yDiff ** 2)

    def slope(self, pt):
        """
        两点形成的直线的斜率
        :param pt:
        :return:
        """
        x = self.x - pt.x
        y = self.y - pt.y
        return (y / x) if x != 0 else None


class LineSegment:
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2

    def __str__(self):
        return f"LineSegment({self.point_1}, {self.point_2})"

    @property
    def length(self):
        """
        直线长度
        :return:
        """
        le = self.point_1.distance(self.point_2)
        if le == 0:
            le = int(le)
        return le

    @property
    def slope(self):
        """
        直线斜率
        :return:
        """
        s = self.point_1.slope(self.point_2)
        if s == 0:
            s = int(s)
        return s

    def is_perpendicular(self, other):
        """
        是否与另一个线段垂直
        :param other:
        :return:
        """
        if None not in (self.slope, other.slope):
            return self.slope * other.slope == -1
        elif self.slope is None:
            return other.slope == 0.0
        elif self.slope == 0.0:
            return other.slope is None

    def is_parallel(self, other):
        """
        是否与另一个线段平行
        :param other:
        :return:
        """
        return self.slope == other.slope


if __name__ == '__main__':
    # line1 = LineSegment(Point(0, 0), Point(1, 1))
    # line2 = LineSegment(Point(1, -1), Point(-1, 1))
    # line1 = LineSegment(Point(0, 0), Point(0, 1))
    # line2 = LineSegment(Point(0, 0), Point(2, 0))
    line1 = LineSegment(Point(0, 0), Point(0, 2))
    line2 = LineSegment(Point(0, 0), Point(0, 10))
    print(f"{line1}的长度为{line1.length}")
    print(f"{line1}的斜率为{line1.slope}")
    print(f"{line2}的长度为{line2.length}")
    print(f"{line2}的斜率为{line2.slope}")
    print(f"{line1}与{line2}平行：{line1.is_parallel(line2)}")
    print(f"{line1}与{line2}垂直：{line1.is_perpendicular(line2)}")
