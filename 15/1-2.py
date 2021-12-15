# Задание 1
# Создать базовый класс Фигура с методом для подсчета
# площади. Создать производные классы: прямоугольник,
# круг, прямоугольный треугольник, трапеция со своими
# методами для подсчета площади.
import math
class Shape:
    @staticmethod
    def square():
        return "square of the base shape"


class Rect(Shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def square(self):
        return self.a*self.b

    def __str__(self):
        return f"фигура: прямоугольник, длина: {self.a}, ширина: {self.b}, площадь: {self.square()}"

    def __int__(self):
        return int(self.square())
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def square(self):
        return 3.14*self.r*self.r

    def __str__(self):
        return f"фигура: круг, радиус: {self.r}, площадь: {self.square()}"
    def __int__(self):
        return int(self.square())
class RightTriangle(Shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return f"фигура: прямоугольный треугольник, сторона А: {self.a} сторона В: {self.b} площадь: {self.square()}"
    def __int__(self):
        return int(self.square())
    def square(self):
        return self.a*self.b/2

class Trapezoid(Shape):
    def __init__(self,d1,d2,alpha,a,b,h):
        self.d1=d1
        self.d2=d2
        self.alpha=alpha
        self.a=a
        self.b=b
        self.h=h
    def __str__(self):
        return f"фигура: трапеция, диагональ1: {self.d1}, диагональ2: {self.d2}, угол между диагоналями: {self.alpha} " \
               f"основание 1: {self.a}, основание 2:{self.b}, высота: {self.h}, площадь: {round(self.square(),3)} "
    def square(self):
        return 0.5 * self.d1 * self.d2*math.sin(math.radians(self.alpha))

    def square2(self):
        return (self.a+self.b)/2*self.h

    def __int__(self):
        return int(self.square())

f=Shape()
print(f.square())
r=Rect(2,5)
print(r)
print(int(r))
c=Circle(5)
print(c)
print(int(c))
rt=RightTriangle(5,6)
print(rt)
print(int(rt))
tr=Trapezoid(4,4,30,5,6,7)
print(tr)
print(int(tr))
print(tr.square2())
