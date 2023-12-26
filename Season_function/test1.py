# تعداد تکرار رقم دلخواه به صورت رشته
# def nums(x , y):
#     return x.count(y)

# x = (input("enter your number: "))
# print(nums(x, "6"))

########################
# روش دوم تعداد رقم تکراری دلخواه
# def repeat(num, dig):
#     x = 0
#     while num > 0:
#         t = num % 10
#         if t == dig:
#             x += 1
#         num //= 10
    
#     return x

# user_num = int(input("enter your num: "))
# user_dig = int(input("enter your dig: "))
# print(repeat(user_num, user_dig))

########################
# جمغ فاکتوریل ها
# def sum_factoryel(x):
#     sum = 0
#     for i in range(x,0,-1):
#         zarb = 1
#         for j in range(1, i +1):
#             zarb *= j
#         sum += zarb
#     return sum

# user_num = int(input("enter your num: "))
# print(sum_factoryel(user_num))

##############################
# def max_nums(a, b , c):
#     max_num = a
#     if b > a:
#         max_num = b
#         if c > b:
#             max_num = c
#     elif c > a:
#         max_num = c
#     print(max_num)

# max_nums(-12,3,5)

############################
# پوزیشنال و نشانگر تابع و کیوورد
# def func(a,/,b,*,c, **d):
#     print("a =", a)
#     print("b =", b)
#     print("c =", c)
#     print("d =", d)
# func(12,76,c = 9, t= 6, q =545)

##########################
# توابع تبدیلات دما

# def degree_generator(user_deg):
#     far_user = (user_deg * 1.8) + 32
#     kel_user = user_deg + 273
#     return far_user, kel_user

# def far_to_cel(user_far):
#     cel_user = (user_far - 32) / 1.8
#     return cel_user

# print(far_to_cel(95))


# user_degree = int(input("enter your degree: "))
# print(f"your degree is {degree_generator(user_degree)} for far and kelvin")

##############################
# دنباله فیبوناچی

# def fibu(user_many): 
#     a = 0
#     b = 1
#     print(a, end=", ") 
#     for _ in range(1, 10):
#         print(b, end=", ") 
#         c = a + b 
#         a, b = b, c
# بولین زوج بودن
# res_even = (num % 2 == 0)

###########################
# چند ریترن باهم در تابع
# def even_in_list(list1):
#     for i in list1:
#         if i % 2 == 0:
#             return True

#     return False

# print(even_in_list([1,13,3,,9.75])) 

###########################
# استفاده از تابع در تابع دیگر
# def check_even(user_num):
#     return (user_num % 2 == 0)

# def all_even_numbers_list(my_list):
#     for num in my_list:
#         if not(check_even(num)):
#             my_list.remove(num)

#     return my_list

# print(all_even_numbers_list([1,2,3,4,5,6,7,8]))

###########################
# def is_even(num):
#     return num % 2 == 0

# def odd_even_list(my_list):
#     odd_list = []

#     for number in my_list:
#         if not(is_even(number)):
#             odd_list.append(number)
#             my_list.remove(number)
            
#     return my_list, odd_list

# even, odd = odd_even_list([12,2,5,36,45,87,1])
# print(even, odd)

###################
# tarif DocString
# def max3(x,y,z):
#     """this func for maximum 3 numbers
    
#     parametrs:
#         x: a decimal number.
#         y: another decimal number.

#     returns:
#         max(int 3 numbers.)
#      """

####################
# مای پای و اناتیشین(یادداشت)
# def nums(a: int) -> float:
#     return a + 23

# print(nums(10))

###############
# تابع در آرگومان دیگر
# def done_verb():
#     word_list = []

#     user_input = input("enter a word: ")
#     while user_input.lower() != "done":
#         word_list.append(user_input)
#         user_input = input("enter another word: ")

#     return word_list

# def avarge_words(list_of_words):
#     count = 0
#     words = 0
#     for i in list_of_words:
#         count += len(i)
#         words += 1
#     print(f"the avarage is {count / words}")

# avarge_words(done_verb())

###########################
# first_class func
# def min_list(my_list):
    
#     def mininmum(a):
#         print(min(a))

#     def maximum(z):
#         print(max(z))
    
#     if my_list == 1:
#         return mininmum
#     elif my_list == 2:
#         return maximum
    
# user = int(input("actoin: "))
# m = min_list(user)
# m([1,46,417,49,47,26,14,85])

###########################
# name_space (locals and enclosed)

# def a():
#     x = 23
#     print(locals())
#     def b():
#         y = 32
#         print(locals())
#     b()


# a()

########################
# Scope in python
# x = 2
# def a():
#     global x
#     # nonlocal x # enclosing for first function
#     x += 454
#     print(x)

# a()

#########################
# def spilit_char(mystr):
#     return mystr.split()[0]

# def lower_case(mystr):
#     mystr = spilit_char(mystr)
#     return mystr.lower()

# def upper_case(mystr):
#     return lower_case(mystr).upper()

# str1 = "ali mortewza"

# print(upper_case(str1))

#######################
# pass_by_value pass_by_reference

# def func(a):
#     a += 1
#     print(a)

# a = 2 #immutable
# func(a)
# print(a)

# def func2(z):
#     z += [1]
#     print(z)

# li = [1,2,3] #mutable
# func2(li)
# print(li)

########################
# lambda functions(map and filter and reduce and sorted)

# a = lambda x: x ** 2
# # print(a(2))
# my_list = [12, 45, 7, 9, 11, 20, 1]
# list(map(function, list)) # calc on your list
# list(filter(lambda x: x % 2 == 0, my_list)) #True - false
# ------------
# from functools import reduce  #reduce bayad do ta argument begire 
# reduce(lambda x,y: x **y, my_list)   out put be sorat int
# ------------
# print(sorted(my_list, key= lambda x: x % 3))  # a fuction for sort objects
# def extraxt_first_name(full_name):
#     return full_name.split()[0]

# print(list(map(extraxt_first_name, ["mahdi jandaghi"])))
# print(list(filter(lambda x: len(x) == 3, ["asd", "asdfrewq"])))
# ------------
# for i in map(lambda x: "a" * x, [2,4,6]):
#     print(i)

################################
# iterators  (تکرار کننده ها)

# my_list = [12,124,7,5]
# my_list = my_list.__iter__()  # iter(my_list)
# print(next(my_list)) # عنصر بعد ار اخری چاپ میشه )(یعنی اول چاپ میشه)    print(my_list.__next__())
# while True:
#     try:
#         print(print(my_list.__next__()))
#     except StopIteration:
#         break

# from itertools import count  # count is infinite iterator 
# count yek lazy hast
# print(next(count(10))) # dakhel parantez number start wared mikunim. defualt 0 hast

###############################
# Decorators (for functions) 

# def dec(func):
#     def inner():
#         print("*" * 20)
#         func() # f = func()
#         print("*" * 20)
        # return f
#     return inner

# def f():
#     print("mahdi")

# test = dec(f)

# def editor(func):
#     def inner(*x, **y):
#         if y == 0:
#             print("warning!!!")   
#         return func(*x, **y)

#     return inner

# @editor    # helper decorator
# def f1(num1, num2):
#     print(num1 / num2)

# f1(5,0)

from functools import wraps

def decoration_func(main_func):
    @wraps(main_func)
    def decration_main(*args, **kwargs):
        # do before the main func
        func = main_func(*args, **kwargs) # decroation_func(*x, **y)
        # do after the main func
        return func
    return decration_main


# @decoration_func
# def func1():
#     print("something")

# print(func1.__doc__)
# print(func1.__name__)

###############################
# Generators

def func(x): 
    yield x ** 2
    print("hi")
    yield 12 * x
    print("im mahdi")

# x = func(6)
# print(next(x))


def power():
    for i in range(8):
        yield i ** 2
 
# result = power()
# for i in result:
#     print(i)


def list_range(start, end, step= 1): 
    while start < end:
        yield start
        start += step



# print(max(gen1(gen2([121,12,54,95,36,14]))))
# my_gen = list_range(1,23)
# my_gen.close()
# my_gen.throw(ValueError("Error!!!!"))
# my_gen.send()

##############################
# Coroutine

# def coroutine(func):
#     def start(*args, **kwargs):
#         my_generic = func()
#         next(my_generic)

#         return my_generic
#     return start


# @coroutine
# def my_gen():
#     print("Start!")
#     for i in range(4):
#         ali = yield i
#         print("OK", ali)


# test = my_gen()
# print(test.send("alireza"))
# print(next(test))  # variable ali baz None mishe.
# print(test.send("karim"))
###################################
# func_attributes صفات

# def ave(li):
#     return sum(li) / len(li)


# setattr(ave, "karim", 123)
# ave.school_name = "ahmadi"
# getattr(ave, "karim")
# delattr(ave, "karim")
# if hasattr(ave, "karim"):
#     pass

#################################
# resurcive functions  بازگشتی

def rec_fact(x):
    if x == 0 or x == 1:  # بخش شرط شکستن
        return 1
    return x * rec_fact(x - 1) # بخش فرا خوانی و بازگشت
            
# print(rec_fact(5))

# exercises for  resurcive functions



def calc_over_six(num):
    if num <= 0:
        return 1
    elif num % 10 < 5:
        return calc_over_six(num // 10)
    else:
        return num % 10 * calc_over_six(num // 10)
    
# print(calc_over_six(6723))

def calc_fibu_res(n):
    if n == 0 or n == 1:
        return n
    return calc_fibu_res(n - 1) + calc_fibu_res(n - 2)
    

# print(calc_fibu_res(4))

def factoryal(num):
    if num == 0 or num == 1:
        return 1
    return num * factoryal(num -1)   

##############################
# gen_dec_depth_recursive

from time import sleep
def dec(func):
    def main(*args,**kwargs):
        print("-" * 10)
        value = func(*args,**kwargs)
        print("*" * 10)
        return value
    return main


@dec
def reverse_nums(x):
    if x <= 0:
        return
    print(x)
    sleep(1)
    return reverse_nums(x - 1)


def g_rev(n):
    if n <= 0:
        return
    sleep(0.6)
    yield n
    for i in g_rev(n-1):
        yield i

gn = g_rev(10)

# print(list(gn))
import sys
num = 1000
sys.getrecursionlimit()
sys.setrecursionlimit(num)

###############################
# memorization
def dec_fib(func):
    memoiz = {}
    def inner(n):
        if n not in memoiz:
            memoiz[n] = func(n)
        return memoiz[n]
            
    return inner




@dec_fib
def fib_rec(n):
    if n == 0 or n == 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


# print(fib_rec(300))

#############################

