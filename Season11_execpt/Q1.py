result = None
def check_input():
    global result
    user_input = input("enter your input: ")
    try:
        result = int(user_input)
        return result
    except ValueError:
        try:
            result = float(user_input)
            return result
        except ValueError:
            print("You have enter a number!")
    return check_input()


check_input()
print(f"result: {result}")