class Car:
    def __init__(self, color, model) -> None:
        self.color = color
        self.model = model
        
    def lights_on(self):
        return f"Lights On Men"
    
class Home:
    def __init__(self, color: str, num_of_room: int, area: int) -> None:
        self.colorhome = color
        self.rooms = num_of_room
        self.area = area
    
    def house_details(self):
        return f"{self.colorhome} and {self.rooms}"

house1 = Home("red", 4, 100)
print(house1.house_details())
