from pprint import pprint

from user import UserName


class UserList(list["UserName"]):
    def search(self, username: str) -> list["UserName"]:
        matching_users : list["UserName"] = []
        for user in self:
            if username in user.username:  # in username ke zade mige age objectet dasht in attrinute okeye boro hal kon
                # Error age in username attribute user nabsahe -> has no attribute.
                matching_users.append(user)

        return matching_users
    
    def append(self, __object: UserName) -> None:
        if not isinstance(__object, UserName):
            raise TypeError("this list only accept User object")
        return super().append(__object)


class UserName(object):
    all_users : list["UserName"] = UserList()  # class attribute
    def __init__(self, username: str ,email: str ,password:str) -> None:
        self.username = username 
        self.email = email # instance attribute
        self.password = password
        UserName.all_users.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.username!r}, {self.email!r}"\
        f", {self.password!r})"
    def __str__(self) -> str:
        return f"{self.username}"


class Seller(UserName): # (name of FatherClass)
    def __init__(self, shaba: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.shaba = shaba
    def order(self, order) -> None:
        print(f"{self.username} you have a {order}!!") # username inheritance from UserName Class


class Buyer(UserName): 
    # def __init__(self, phone: str) -> None:  # Overriding This
    #     self.phone = phone
    def __init__(self, phone: str, **kwargs) -> None:
        super(Buyer, self).__init__(**kwargs)
        self.phonenum = phone

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.username!r}, {self.email!r}"\
        f", {self.password!r}, {self.phonenum!r})"





class SellerBuyer(Seller, Buyer):
    def __init__(self, score, **kwargs) -> None:
        super().__init__(**kwargs)
        self.score = score
    pass







def main2():
    buyer_acc = SellerBuyer(username = "kari98", email = "sa@mali.to", password = "3231", phonenum = "0939", shaba ="6104"\
                            , score= 10)
    print(buyer_acc.email)


def main():
    us1 = UserName("ali007", "abcd@gmail.com", "323121")
    sell = Seller("mash_taaghi", "haji@hmail.com", "yazahra1370")
    print(us1.username, us1.email, us1.password)
    print(sell.username, sell.email, sell.password)
    sell.order("book")
    pprint(UserName.all_users.search("ali"))
    pprint(sell.all_users)


if __name__ == "__main__":
    main2()


# ----------
UserName.all_users # har object - yek onsor to list

# eval("print(1)") # one row
# exec("x = 5\nprint(x)") # some rows

        
        