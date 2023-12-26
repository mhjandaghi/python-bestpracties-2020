from datetime import datetime as dt, timedelta as td
from time import sleep
class Product:
    def __init__(self, product_name, price, discount) -> None:
        self.product_name = product_name
        self.price = price
        self.discount = discount

    def __str__(self) -> str:
        return f"{self.product_name}"
class Comment:
    website = "sabz.ir"
    def __init__(self, product, name, discreption, like= 0, disslike= 0) -> None:
        self.product = product
        self.name = name
        self.discreption = discreption
        self.date = dt.now()
        self.like = like
        self.disslike = disslike
        
    def show(self):
        print(f"product: {self.product}\nname: {self.name}\n"
               f"descripton: {self.discreption}\n"
               f"date: {self.date}\n"
               f"like: {self.like}\n"
               f"disslike: {self.disslike}")
        
    @classmethod
    def info(cls):
        print(cls.website)

    @classmethod
    def censorship(cls, product, name, discreption, like= 0, disslike= 0):
        print("tje comment was censored!!!")
        sc = discreption.replace("khar", "****")
        return cls(product, name, sc, like, disslike)

    @staticmethod
    def elapswd_time(time):
        print(dt.now() - time)

# def elapswd_time(time):
#         sleep(3)
#         print(dt.now().second - time)
        

py_course = Product("py_expert", 0, 0)
com1 = Comment(py_course, "ali", "khar")
com1.show()
Comment.info() # com1.info()
com2 = Comment.censorship(py_course, "ali", "khar")
com2.show()
Comment.elapswd_time(com2.date - td(days= 2))