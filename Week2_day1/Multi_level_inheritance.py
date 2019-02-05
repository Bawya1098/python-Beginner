class Micro_Computers():
    def __init__(self, size):
        self.size = size

    def display(self):
        print("size is:", self.size)


class Desktop(Micro_Computers):
    def __init__(self, size, cost):
        Micro_Computers.__init__(self, size)
        self.cost = cost

    def display_desktop(self):
        print("cost is: Rs.", self.cost)


class Laptop(Desktop):
    def __init__(self, size, cost, battery):
        Desktop.__init__(self, size, cost)
        self.battery = battery
        print('laptop are')

    def display_laptop(self):
        print("battery is:", self.battery)


l = Laptop('small', 20000, 'battery_supported')
l.display()
l.display_desktop()
l.display_laptop()

print('---------------------------------------------')
d = Desktop('large', 30000)
d.display_desktop()
d.display()

print('---------------------------------------------')
