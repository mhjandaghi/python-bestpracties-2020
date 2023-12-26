from pprint import pprint
class SuperClass1:
    def __init__(self, p1) -> None:
        self.pname1 = p1

class SuperClass2:
    def __init__(self, p2) -> None:
        self.pname2 = p2

class SubClass(SuperClass1, SuperClass2): # ravash_sadeh
    def __init__(self, p1, p2, p3) -> None:
        SuperClass1.__init__(self, p1)
        SuperClass2.__init__(self, p2)
        self.p3 = p3


obj = SubClass(1, 2, 3)

# -------- MRO --------
class BaseClass:
    num_base_calls = 0

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def call_me(self):
        print("call me now base!")
        self.num_base_calls += 1

class LeftSubClass(BaseClass):
    num_left_calls = 0

    def __init__(self, c, **kwargs) -> None:
        super().__init__(**kwargs)
        self.c = c

    def call_me(self):
        # BaseClass.call_me(self)
        super().call_me()
        print("call me now left!")
        self.num_left_calls += 1

class RightSubClass(BaseClass):
    num_right_calls = 0

    def __init__(self, d, e, f, *args, **kwargs) -> None:
        super().__init__(**kwargs)
        self.d = d
        self.e = e
        self.f = f

    def call_me(self):
        # BaseClass.call_me(self)
        super().call_me()
        print("call me now right!")
        self.num_right_calls += 1


class MainSubClass(LeftSubClass, RightSubClass):
    num_main_calls = 0

    def __init__(self, g, **kwargs) -> None: # *args also useful
    
        super().__init__(**kwargs)
        self.g = g


    def call_me(self):
        # LeftSubClass.call_me(self)
        # RightSubClass.call_me(self)
        super().call_me()
        print("call me now sub!")
        self.num_main_calls += 1
        

s = MainSubClass(a =1,b =2,c= 3,d= 4,e= 5,f= 6,g= 7)
print(s.num_base_calls, s.num_left_calls, s.num_right_calls,\
       s.num_main_calls)
pprint([s.a, s.b, s.c, s.d, s.e, s.f, s.g])
# pprint(MainSubClass.__mro__)