import turtle
import math

bob = turtle.Turtle()


# def square (t):
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)
#
#
# square(bob)

# 关键字实参（keyword arguments）
def polygon (t, n=4, length=70):
    """

    :rtype: object
    """
    angle = 360 / n
    polyline(t, n, length, angle)


# polygon(bob, n=6, length=100)



def circle (t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)


# circle(bob,10)  #画一个半径 为10 的圆


# 与其把接口弄乱，不如根据周长（circumference）选择一个合适的n值：

def circle2 (t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)


# 现在线段的数量，是约为周长三分之一的整型数， 所以每条线段的长度（大概）是3，小到足以使圆看上去逼真， 又大到效率足够高，对任意大小的圆都能接受。

# circle2(bob, 100)  # 画两个圆 哈哈


def arc (t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)


def polyline (t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


#重写 画圆方法
def circle3(t, r):
    """
    :param t: turtle 对像
    :param r: 半径
    :return:
    """
    arc(t, r, 360)


circle3(bob,120)

turtle.mainloop()
