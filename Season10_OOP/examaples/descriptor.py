class NameField:
    # def __init__(self, name= None) -> None:
    #     self.name = name
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        # owner = class NameField
        # instance = object of NameField
        # return self.name
        return instance.__dict__[self.name]
    

    def __set__(self, instance, value):
        if 15 > len(value) > 0:
            # self.name = value
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f"Invalid Error {value!r}")
        

    def __delete__(self, instance):
        print("deleting..")
        del instance.__dict__[self.name]
        
class Parent:
    childname = NameField()
    mothername = NameField()
    fathername = NameField()



    def __init__(self, childname, mothername, fathername) -> None:
        self.childname = childname
        self.mothername = mothername
        self.fathername = fathername



p = Parent("reza", "mahdi", "neda")
print(p.childname)
print(p.mothername)
print(p.fathername)
