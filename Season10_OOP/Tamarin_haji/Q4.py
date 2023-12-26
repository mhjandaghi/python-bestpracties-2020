from os import system 
system("cls")

class Time:
    def __init__(self, h= 0, m= 0, s= 0) -> None:
        if 0 < h < 24:
            self.houres = h
        if 0 < m < 59:
            self.minutes = m
        if 0 < s < 59:
            self.seconds = s
        self.day = 0

    def __str__(self) -> str:
        return (f"day: {self.day}\n{self.houres:02}:{self.minutes:02}:{self.seconds:02}")

    def __add__(self, other):
        # if self.houres + other.houres > 24:
        #     self.day += 1
        #     self.houres = (self.houres + other.houres) - 24
        # if self.minutes + other.minutes > 60:
        #     self.houres += 1
        #     self.minutes = (self.minutes + other.minutes) - 60
        # if self.seconds + other.seconds > 60:
        #     self.minutes += 1
        #     self.seconds = (self.seconds + other.seconds) - 60
        s = self.seconds + other.seconds
        m = self.minutes + other.minutes + s // 60
        h = self.houres + other.houres + m // 60
        return Time(h%24, m%60, s%60)
    
    def __eq__(self, other):
        return (self.houres * 3600 + self.minutes * 60 + self.seconds) == (other.houres * 3600 + other.minutes * 60 + other.seconds)
    
j = Time(12,4,3)
x = Time(9,57,12)
z = x + j
print(j)
print(z)
