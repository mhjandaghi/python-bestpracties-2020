class OptionsMixin:
    def eat(self):
        pass
    def sleep(self):
        pass
    def cry(self):
        pass
    def die(self):
        pass


class Animal:
    def __init__(self, name= "", color= "") -> None:
        self.name = name
        self.color = color

    def info(self):
        print(f"my animal is {self.name} and color is"+
              f" {self.color}")

    def sound(self):
        print("sound of animal")


class Cat(Animal, OptionsMixin):
    def __init__(self, name= "", color= "") -> None:
        super().__init__(name, color)

    def info(self):
        print(f"my cat is {self.name} and color is"+
              f" {self.color}")

    def sound(self):
        print("Meowww ...")


class Cow(Animal, OptionsMixin):
    def __init__(self, name= "", color= "") -> None:
        super().__init__(name, color)

    def info(self):
        print(f"my Cow is {self.name} and color is"+
              f" {self.color}")

    def sound(self):
        print("moo ...")


my_cat= Cat("jessy", "black")
my_cow = Cow("gabi", "white")

an = Animal()
an.info()
# for animal in [my_cat, my_cow]:
#     animal.sound()
#     animal.info()

# ----------------

class Shape: # Abstract Class
    def __init__(self, kind, name) -> None:
        self.kind = kind 
        self.name = name

    def area(self):
        raise NotImplementedError("You must calc area")
    
class Square(Shape):
    def __init__(self, kind, name, side) -> None:
        super().__init__(kind, name)
        self.side = side

    def area(self):
        print(self.side ** 2)

class Circle(Shape):
    pi = 3.14
    def __init__(self, name, radius) -> None:
        super().__init__("Circle", name)
        self.radius = radius

    def area(self):
        print(self.radius ** 2 * self.pi)