def coroutine(func):
    def start(*args, **kwargs):
        my_generic = func()
        next(my_generic)

        return my_generic
    return start


@coroutine
def my_gen():
    print("Start!")
    for i in range(4):
        ali = yield i
        print("OK", ali)


test = my_gen()
print(test.send("alireza"))