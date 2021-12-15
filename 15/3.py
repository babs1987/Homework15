class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("info about abstract fugure")
        return "nihuya"

    def save(self):
        f = open("figure", "w", encoding="utf8")
        f.write(self.show())
        f.close()

    def open(self):
        f = open("figure", "r", encoding="utf8")
        return f.read()
        # f.close()


class Square(Shape):
    def __init__(self, x, y, a):
        super().__init__(x, y)
        self.a = a

    def show(self):
        print(f"Квадрат координаты ({self.x},{self.y}) длина стороны -{self.a} ")
        return f"Квадрат координаты ({self.x},{self.y}) длина стороны -{self.a} "


class Rectangle(Square):
    def __init__(self, x, y, a, b):
        super().__init__(x, y, a)
        self.b = b

    def show(self):
        print(f"прямоугольник, координаты {self.x},{self.y} длина стороны A :{self.a}, длина стороны B: {self.b} ")
        return f"прямоугольник, координаты {self.x},{self.y} длина стороны A :{self.a}, длина стороны B: {self.b}  "


class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def show(self):
        print(f"фигура: круг координаты центра ({self.x},{self.y}) , радиус: {self.r} ")
        return f"фигура: круг координаты центра ({self.x},{self.y}) , радиус: {self.r} "


class Ellipse(Rectangle):
    def show(self):
        print(
            f"фигура: эллипс координаты левого верхнего угла описанного прямоугольника ({self.x},{self.y}) , "
            f" длина стороны A :{self.a}, длина стороны B: {self.b}  ")
        return f"фигура: эллипс координаты левого верхнего угла описанного прямоугольника ({self.x},{self.y}) ," \
               f" длина стороны A :{self.a}, длина стороны B: {self.b}  "


s = Square(5, 6, 5)
r = Rectangle(5, 5, 6, 7)
c = Circle(5, 6, 8)
e= Ellipse(5,6,4,5)
e.save()

print(e.open())
