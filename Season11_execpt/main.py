# ---- Exception ----
# Syntax error mesl (if :)
# Run-time Error (exception)
# Zero division Error ->
a = (5 / 0)
# Name Error ->
x = 0
del x
z = (x  + 6)
# Type Error ->
p = "x" + 6

# ---- Try Execpt else finally ----
try:
    x = int(input("x: "))
    print(x)
except ValueError:
    print("try again...!")
except (TypeError, NameError) as e:
    print("Error Type - hint")
except Exception: # except:
    print("Other Error")

# ----

def div(x, y, n):
    try:
        s = x + y
        res = s / n
    except TypeError as te:
        print(te.__class__.__name__)
    except ZeroDivisionError as ze:
        print(ze.__class__.__name__)
        try:
            s = s + "a"
        except:
            print("Type Error")
    else:
        return res     
    finally:
        print("Test Passed") 
        
try:    
    div(2,3,0)
except:
    print("Error Global!!!")

# ---- raise ----
def divis(x, y, n):
    if n == 0: # Sadeh
        raise ZeroDivisionError("eshteb nazan")
    
    try: # Pichideh
        s = x + y
        d = s / n
    except ZeroDivisionError as zde:
        raise RuntimeError("oops") from zde

# ---- Create Exception ----
class DigitError(Exception):
    def __init__(self, s, message= "Error Founded") -> None:
        self.message = message
        self.s = s
        super().__init__(self.message)
        
 

def func(string):
    if not string.isdigit():
        raise DigitError
    
    nums = []
    for num in string: 
        nums.append(int(num))

    print(nums)

func("09h9")

# ---- Warnings - assert ----
import warnings 
def f(x: int,y: int):
    if not (isinstance(x, int) and isinstance(y, int)): 
        warnings.warn("x and cant be strings!", UserWarning)
    print(x + y)

f(4, "s")
print("ok")

def f(x: int,y: int):
    assert (isinstance(x, int) and isinstance(y, int))
    print(x + y)

