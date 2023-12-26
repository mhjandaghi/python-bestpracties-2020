from typing import Any


class Shape:
    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.area = 0
        self.perimeter = 0

    def __str__(self) -> str:
        return self.__class__.__name__
    

    def show(self):
        info = ""
        for key, value in self.__dict__.items():
            if value > 0: 
                info += f"{key}: {value:.2f}\n"
        print(info)
    

    def calc_area(self):
        pass

    def calc_perimeter(self):
        pass

# Length - Width       
class Rectangle(Shape):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def calc_area(self):
        self.area = self.length * self.width

    def calc_perimeter(self):
        self.perimeter =  2 * (self.length + self.width) 

# Length
class Square(Shape):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    def __call__(self, length) -> Any:
        self.length = length 

    def calc_area(self):
        self.area = self.length ** 2

    def calc_perimeter(self):
        self.perimeter =  self.length * 4


class Triangle(Shape):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def calc_area(self):
        self.area = (self.height *  self.base) // 2

    def calc_perimeter(self):
        self.perimeter =  self.base + self.lside + self.rside


class Rhombus(Shape):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def calc_area(self):
        self.area = (self.dia1 * self.dia2) // 2

    def calc_perimeter(self):
        self.perimeter =  self.length * 4


class Circle(Shape):
    pi = 3.14
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def calc_area(self):
        self.area = (self.radius ** 2 ) * Circle.pi 

    def calc_perimeter(self):
        self.perimeter =  2 * Circle.pi * self.radius

        
moraba = Square(length = 4)
moraba.calc_area()
moraba.show()