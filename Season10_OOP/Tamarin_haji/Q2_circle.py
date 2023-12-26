from math import pi
class CreateCircle:
    pi_num = pi
    def __init__(self, radius: int) -> None:
        self.rad = radius

    def collecting_environment(self):
        print(f"The environment is: {(self.rad * 2)* CreateCircle.pi_num:.2}")
    def collecting_area(self):
        print(f"The area is: {(self.rad ** 2)* CreateCircle.pi_num:.2}")

c = CreateCircle(10)

c.collecting_area()