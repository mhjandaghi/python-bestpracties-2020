# 't' > text(default) ,,, "b" > binary
# 'r'('rt') > reading (default in open /// not found > error
# "w" > writing /// not found > create same name file
# 'a' > writing end the text /// not found > create same name file
# 'x' > writing /// should it create file . else > error
# ex > "xb" --- "ab" --- "wb"
# "r+" ("rt+") > read and write /// not found > Error /// end of text append your write
# "w+" ("w+t") > write and read /// delete before text.
# "a+" ("a+t") > write and read to end of text /// not found > create same name file
# "x+" ('xt+') > write and read /// delete before text. /// find file > Error
# "ex" -> 'r+b' --- 'xb+' --- 'ab+'
open("pedar12.txt", "wt")  # line3
open("pedar12.txt", "a")
# open("test1.txt", "x")
open("pedar.txt", "a+")
# open("daddy.txt", "x+")  # line-11
open("../code.txt", "x")

# ------- read-write methods -------
f = open("test1.txt", "r+", encoding="utf8")
s = "*"
if f.writable():
    f.write(s)
if f.readable():
    f.read(5)

li = ["a", "b", "c"]
f.writelines(li)
f.readline(4)
my_list = f.readlines()  # buffer_bytes
for line in f:
    # print(line)
    pass

while True:
    a = f.readline()
    print(a, end="")
    if a == "":
        break
print("End")

# ------ buffer ------
import os

file = open("pedar12.txt", "wb", encoding="utf8", buffering= 0) # no buffer
file.write(b"mahdiiii")
file.flush()
os.fsync(file) # args -> File-name
input("x: ")
# -- part 2 --
file1 = open("pedar12.txt", "w", encoding="utf8", buffering= 1)  # line buffer and buffering = -1 (default chars = 8192)
file1.write("reza\n")
file1.write("kami")
file1.close()
file2 = open("pedar12.txt", "wb", encoding="utf8", buffering= 25)  # adad delkhah baraye tedad cahracters
file2.close()

# ------ pointer ------
file3 = open("pedar12.txt", "rb")
file3.tell()
file3.read()
file3.seek(0, 0) # arg2 -> 0:start --- 1:default harja k hast --- 2: az akhar

# ------ Context_manager(with - as) ------
with open("pedar.txt") as f1, open("pedar12.txt", "w") as f2:
    pass

f5 = open("pedar12.txt", "w")
l1 = ["a", "b", "c"]
f5.writelines("\n".join(l1))
# ------ Std - file ------
from sys import stdin, stdout, stderr
# stdin -> keyboard (input)
f = stdin.readline() # input - behavior
print(f)
# stdout -> screen (print)
stdout.write("hi")
# stderr -> screen (execptions) 
stderr.write("Error")

# ------ File - methods ------
f = open("test1.txt", "w", encoding= "utf8", buffering= -1, errors= "strict", newline="", closefd=True)
f.truncate(1)
f.seekable() # True or False
import os
os.remove("pedar.txt")
# ------ Json-File -------
import json
jn = "[1,2,3]"
py = json.loads(jn)

jn = "true"
py = json.loads(jn)

jn = "{'a': 23, 'b': [1,2,3]}"
py = json.loads(jn)

jn = "null"
py = json.loads(jn)
# -----
with open("json1.json", "r") as js:
    s = json.load(js)
    print(js)
# ------ dumps -> python to json srting
d = [12,4,5,9]
js_str = json.dumps(d) # array (class str)

d = None
js_str = json.dumps(d) # null (class str)

d = True
js_str = json.dumps(d) # true (class str)

# ------ dump -> python to json file
x = {"a": 1, "b": 9}

with open("json1.json", "w") as jsf:
    json.dump(x, jsf) # array
    json.dump(None, jsf) # null

# ------ Csv -------
import csv
with open("test.csv") as cf:
    data = csv.reader(cf) # iterator (list)
    data1 = csv.DictReader(cf) #iterator (dict0)

with open("myc.csv", "w", newline="") as sf:
    writer = csv.writer(sf)
    writer.writerow(["a", "b", "c"]) # a row
    writer.writerows([[1,2,3], [4,5,6]]) # rows

# ---- END ----

