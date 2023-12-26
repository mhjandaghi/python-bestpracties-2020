# ----- Except -----
a = 5
del a
x = 5 / 0 # zero division Error
y = a + 6 # Name Error (not defined)
z = "2" + 5 # Type Error  
m = int(input("m: ")) # Value Error
try:
    x = "5" + 2
    if x > 5:
        raise ValueError("bro ridid!")

    print(x)
except (TypeError, NameError):
    print("Error") 
except ValueError:
    print("Unknown Error") 
finally:
    print("goOd joB".title()) # Dar har sorat ejra mishe...

