class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.height = heigth

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    # Метод, рассчитывающий площадь
    def get_area(self):
        return self.width * self.height

class Square:
    def __init__(self,a):
        self.a = a
    def get_area_square(self):
        return self.a ** 2
#возведение в степень **2 (в квадрат)

class Circle:
    def __init__(self, r):
        self.r = r

    def get_area_circle(self):
        return 3.14 * self.r ** 2