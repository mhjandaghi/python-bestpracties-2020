# int - float - methods
x = 23
(x.bit_length())
(x.denominator)
(x.numerator)
f = 16.5
f.is_integer()
f.hex()
########################
# List - Methods
my_list = [1,2,3,4,5,6]
my_list.append("x")
poped_value = my_list.pop("index")
my_list.remove("x")
my_list.index("x", "start", "end")
my_list.clear()  # del mylist[]
my_list.extend([12,45,78])
my_list.sort()
######################
# Set - Tuple - Methods
my_tup = (1,23,45)
my_tup.count("x")
my_set = {1,2,3,4,5}
my_set2 = {4,5,6,7}
my_set.add()
my_set.difference_update(my_set2)
my_set.isdisjoint(my_set2)
######################
# Dict - Methods
my_dict = {"a" : 12,
           "b" : 14,
           "c" : "ahmad"}
my_dict.pop("a")
my_dict.popitem()
my_dict.setdefault("d", 11) # روی دیکشنری اعمال میشه
my_dict.update([["a", 4], ["b", 80]])
my_dict["k"] = my_dict.pop("a") # ترفند تغییر کلید
#####################
# working - with - walrus - operation
(x := "x")
while (s := input("alie?: ").lower()) != "q":
    print("hi")
def func(x):
    print(x ** 2)

# func(x := 5)

list1 = [1,2,3,4]
dict1 = {
    "len": (len_list := len(list1)) ,
    "s": (sum_list := sum(list1) ),
    "avg": sum_list / len_list
}
print(dict1)
######################
# Comprehension
my_list1 = [x for x in (input("sa: ")).split()]
fm = list(map(lambda x : x ** 2, range(10)))

l2 = [x for x in range(10) if x % 2 == 0]
s1 = [1,2,3]
s2 = [5,6,7]
l3 = [(i, j) for i in s1 for j in s2 if i != j]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

my_list = [[row[i] for row in matrix] for i in range(3)]
x = list(zip(*matrix))

gnexer = (x ** 2 for x in range(7))

list2 = [x if x % 2 == 1 else 0 for i in range(10)]

from random import randrange
def func(x = 1):
    x = randrange(50, 150)
    return x


mylist = [x for _ in range(10) if (x := func()) > 100]

names = ["reza", "ali", "sara", "neda", "sahel"]
dict1 = {key : [i for i in names] for key in names}
#########################
# encoding and decoding
# ascii and unicode
bin(ord("c"))
chr("adad")
print("\U00001110") # \u0101
########################
# Bytes - bytearray
x = b"x"
bytes("a", "utf-8")
bytearray("a", "utf-8")
chr(0xa6) # 166
# \x45\x12\xa7
x.decode("utf-8")
name1 = bytearray("rez", "utf-8")
name1[0] = 125
#########################
# String - methods
str12 = "karim x asd"
str12.isascii()
str12.center(10, "^")
str12.isidentifier()
str12.isprintable()
d = {"b" :"*"}
t = str.maketrans(d,"A")
str12.translate(t) # translate(d)
str12.rpartition("s")
str12.removeprefix("k")
str12.rstrip("sda")
######################

