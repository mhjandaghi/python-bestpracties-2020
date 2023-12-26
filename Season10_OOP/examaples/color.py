class Color:
    def __init__(self, rgb, name) -> None:
        self.rgb = rgb
        self.name = name

    def _set_name(self, name):
        if name:
            self._name = name
        else:
            raise ValueError(f"Invalid Error {name!r}")

    def _get_name(self):
        return self._name 

    def _del_name(self):
        print("Delting")
        del self._name


    name = property(fget=_get_name,fset=_set_name, fdel=_del_name, doc="docmoc") # Doc (default): fget
    # name = property()
    # name = name.setter(_set_name)
    # name = name.getter(_get_name)
    # name = name.deleter(_del_name)
# -----------
c1 = Color(0xa632a8, "violet") # Setter        
c1.rgb = 0xd9cb4e
print(c1.name) # Getter
del c1.name # Delete

# ---------------

class Color:
    def __init__(self, rgb, name) -> None:
        self.rgb = rgb
        self.name = name

    @property
    def name(self):
        """
        this atter for my object
        """
        return self._name

    @name.setter
    def name(self, name):
        if name:
            self._name = name
        else:
            raise ValueError(f"Invalid Error {name!r}")
 
    @name.deleter
    def _del_name(self):
        print("Delting")
        del self._name

# --------------------------------

class NewList(list):
    @property
    def avg(self):
        return sum(self) / len(self)

l = NewList((1,2,3))
print(l.avg)