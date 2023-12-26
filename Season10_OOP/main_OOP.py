from __future__ import annotations
# ---- Objects ----
# 1- everithing is object in python 
# 2- any object membership of a class
# 3- a variable is refrence to a object
x = 1 # X is a object in bulit_in class (int)

type(x)
x.__class__ # show the name of class
x.__mul__(6) # x * 6

class A:
    pass
A.__bases__ # class object (inhertance)
type.__bases__ # class object

# ---- Create Class ----
class PascalCase:
    pass
# --------
from math import hypot

class Point:
    """
    This class is a point show in table 2D.
    example (be like terminal) .
    >>> ex = Point() 
    >>> ex2 = Point(3, 4)
    >>> ex.reset()
    >>> ex.distance(ex2)
    methods:
        move() -> move for point left and right.
    attributes:
        x
        y
    interface:
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        initilization the new point in object.
        param x: float
        param y: float
        """
        self.x = x
        self.y = y
        # self.move(x, y) # this is better! 
        
    
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
    def reset(self): # self == object (ex : p1)
        # self.x = 0
        # self.y = 0
        self.move(0,0)

    def distance(self, other: "Point") -> float:
        dis = hypot((self.x - other.x), (self.y - other.y))
        return (f"the distance is : {dis}")


p1 = Point() # a object of class point
p2 = Point()

p1.x , p1.y = 2, 5
p2.move(4, 5)
Point.move(p1, 7, 9)
# -----
p1.distance(p2)

p1.color : str = "red" # annonation for object(variable)

# ---- __init__ ---- (مقدار دهی اولیه)
p3 = Point(0, 0) # arguments for (method of __init__)

# __new__ --> cerate
# __init__ --> initilize
# line 23

# ---- Class DocString ----
# line 22
Point.__doc__ # just for Class
# help(Point) # Visit the all class and methods DocStrings

import doctest
# doctest.testmod()

# <mypy> for annonations

# ---- modules and classes ----
# example in pakage_in and test.py
from typing import Any, Optional
point: Optional[Point] = None
def get_point():
    global point
    if not point:
        point = Point()

    return point

if __name__ == "__main__":
    # print(p1)
    pass

# ---- Underscore ----
# - 1 -
for _ in range(2):
    name, _ = [1, 3]
# - 2 -
class User:
    def __init__(self, name, phone = "") -> None:
        self._user_id = id(self) 
        self.name = name
        self.__phone = phone

    def set_phone(self, phone): # work of setter
        if phone.isdigit():
            self.__phone = phone
    def get_phone(self):
        return self.__phone

ali = User("ali", 3231)
print(ali._user_id) # protected name!!!

# - 3 - 
min_ = 1 # dont override the min()
class_ = 12 # dont override the class KeyWord

# - 4 - 
#  __name : private names

dir(ali) # "_User__phone" -> name mangling
print(ali.__phone) # ali._User__phone -> correct

# - 5 - 
# just for special methods
__annotations__
__name__
# -------- getter and setter ----------
ali.set_phone("1234569")
ali.get_phone()

# ---- str - repr ----
str("ali") # for user
repr("karim") # for debugging and programmer
import datetime
today = datetime.datetime.today()
str(today) # 2023-04-22 16:43:59.156990
repr(today) # datetime.datetime(2023, 4, 22, 16, 43, 59, 156990)

# repr > terminal and powershell

# create repr(__str__) in class -> person.py

# ---- attributes in class (instance attribute) ---
person1 = User("ali")
person1.age = 10 # instance attribute
# line1
class UserName:
    all_users : list["UserName"] = []  # class attribute
    def __init__(self, username: str ,email: str ,password:str) -> None:
        self.username = username 
        self.email = email # instance attribute
        self.password = password
        UserName.all_users.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.username!r}, {self.email!r}"\
        f"{self.password!r})"
    
    def __str__(self) -> str:
        return f"{self.username}"
    
    def __len__(self):
        return self.password
    
    def __del__(self):
        print("deleted this object")
        

us1 = UserName("ali", "abcd@gmail.com", "323121")

# -- Hint --
class Test:
    def r(self, ra):
        return ra # without self (because parameter - no attribute)
         
# ---- interhance -----
# with this we dont have Repeat codes
Point.__base__ # fahmidan kelas pedar
Point.__bases__ # fahmidan kelashaye pedar
# example in user.py

# ---- inheriting from bulitins ----
# example in user.py -> class UserList

# ---- Overriding and super() ----
# exxample in user.py

# ----- multiple inhertance -----
# example in mulinher.py

# Diamond MRO -> mulinher.py

# initialization in multiple inhertance

# ---- Polymorphism ----
a = 3 + 2
a = "re" + "ad"
a = 3 + 2j - 2 + 1j
def add(x, y):
    print(x + y)
# example in polymoroh.py

# ---- mixin ----
# example in polymoroph.py

# ---- Duck Typing ----
len("re")
len([1,2,3,4])
def check_len(obj): # LYBL
    # if "__len__" in dir(obj):
    if hasattr(obj, "__len__"):
        len(obj)
    else:
        print("sorry")


def check_len(obj): # EAFP (this better)
    try: 
        len(obj)
    except:
        print("sorry")
# -------
mydict= {
    "a": 1,
    "b": 2,
    "c": 3
}
mydict.get("keyname") # nabashe -> None
if "a" in mydict.keys(): # LYBL
    mydict["a"]
    pass
else:
    "sorry"
    pass

try: # EAFP
    mydict["c"]
except:
    "Sorry"
    pass

class Duck:
    def move(self):
        print("im swimming")
class Person:
    def move(self):
        print("im Walking")
class Plane:
    def move(self):
        print("im Flying")

def func(obj):
    obj.move()

d = Duck()
p = Person()
a = Plane()

# ---- call ----
def f(): # Callable
    return
p = 1 # Not_Callable

class A:
    def __init__(self, x) -> None:
        print("init")
        self.x = x

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print('call')
        self.z = 3


a = A(5) 
a # not Callable (Just Callable)
a(3) # Now Callable
callable(A) # Class or Object
# Example in shape.py (Square)

# ---- Types of Methods ----
# example in comment.py

# ---- Property ----
# Example in Color.py

# ---- aggregation - composition ----
class Question:
    def __init__(self, q, a: list) -> None:
        self.q = q
        self.a = a

class ExamPaper: # Composition
    def __init__(self) -> None:
        self.question = Question("what?", ["nothing", "good", "all"])

e = ExamPaper()
print(e.question.a) 

# ---------
class Student:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

    def __str__(self) -> str:
        return f"{self.name}: {self.id}"
    
class Uni:
    def __init__(self, students: list) -> None:
        self.students = students

s = [Student("ali", 2222), Student("bahar", 1234)]
uni1 = Uni(s)

# ---- Meta Class ----
class HumanMeta(type): # Meta Class
    pass
class Father(metaclass = HumanMeta):
    pass
# chon hame instance "type" hastand.

# ---- Abstract Class ----
from abc import ABC, abstractmethod, ABCMeta
class Vehicle(ABC): # Ravash Aval

    @abstractmethod
    def move(self):
        """
        this method for move a vehicle
        """
        print("default")

    @abstractmethod
    def repair(self):
        """
        this method for repair object
        """

    # @staticmethod
    # @abstractmethod
    # def func():
    #     pass

    def class_name(self):
        print(self.__class__)

class LandV(Vehicle): # abc
    @abstractmethod 
    def brake(self):
        """
        this for eject
        """
class AirV(Vehicle): # abc
    @abstractmethod
    def eject(self):
        """
        this for eject only airplane and ...
        """

# concrete class:
class Car(LandV): # bayad move o repair tarif she
    def move(self):
        super().move()
        print("driving!")

    def repair(self):
        print("thats it repair..!")

    def brake(self):
        super().brake()
        print("braking")


class AirPlane(AirV):
    def move(self):
        super().move()
        print("Flying!")

    def repair(self):
        print("thats it repair..!")
    
    def eject(self):
        super().eject()
        print("ejecting")

a = Vehicle() # Type Error



# class Animal(metaclass = ABCMeta):
#     pass

# ---- Operator Overloading ----
# example in user.py

# ---- __slots__ ----
class ParentClass:
    __slots__ = ('a', 'b')
    def __init__(self,a ,b) -> None:
        self.a = a
        self.b = b
        
class MyClass(ParentClass):
    __slots__ = ('c',)
    def __init__(self,a ,b) -> None:
        super().__init__(a,b)

obj = MyClass(1,2)
obj.c = 3
obj.__dict__["d"] = 4
obj.__dict__ # list of Attributes

# ---- iterable - iterator ----
lst = [1,2,3]
"__next__" in dir(lst) # False
"__iter__" in dir(lst)
it_lst = iter(lst) # iterator shoadn
next(it_lst)

class NewObj:
    def __init__(self) -> None:
        self.items = [1,2,3,4]
        self.count = 0

    def __iter__(self):
        for i in self.items:
            yield i
    
    def __next__(self):
        self.count += 1
        return self.count

n = NewObj()
n1 = iter(n)

class PowTwo:
    def __init__(self, max_pow) -> None:
        self.n = 0
        self.max_pow = max_pow

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <= self.max_pow:
            result = self.n ** 2
            self.n += 1
            return result
        else:
            raise StopIteration
        
a = PowTwo(10)

# ---- Class Decorator ----
from functools import wraps, update_wrapper

def my_decorator(cls):
    @wraps(cls)
    def wrapper_func(*args, **kwargs):
        print("*" * 22)
        cls(*args, **kwargs)
        print("-" * 22)

    return wrapper_func

@my_decorator
class Test:
    pass

NewTest = my_decorator(Test) # ravash do decorator 
o1 = NewTest()
obj = Test() # ghabl , baad setare barooon

class MyDec:
    def __init__(self, func) -> None:
        update_wrapper(self, func)
        self.func = func
    
    def __call__(self) -> Any:
        # kaaraye ghabl ejra
        a = self.func()
        return a
        # SELF.FUNC()

@MyDec
def x():
    print("ali")

# ---- descriptor ----
# example in descriptor.py

# ---- context manager ----
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("The File Was Open")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_eval, exc_tb):
        print("The File Was Closed")
        self.file.close()


with FileManager("text.txt", "w") as fm:
    fm.write("hello!!!")

# ---- Data Class ----
from dataclasses import dataclass, InitVar
from typing import ClassVar
@dataclass(frozen=False)
class Person:
    name: str
    family: str
    age: ClassVar[int] = 22
    gender: InitVar[str]

    def __post_init__(self, gender):
        if self.age < 0:
            self.age = 0
        if gender == "man":
            self.name += "*"



p = Person("ali", "hasani", age= 20, gender= "man")

# ***** THE END *****