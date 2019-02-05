class Computer:
    def __init__(self, generation):
        self.generation = generation

    def display(self):
        print("generation:", self.generation)


class Analog_Computer(Computer):
    def __init__(self, generation, data):
        Computer.__init__(self, generation)
        self.data = data

    def display_name(self):
        print('Processing_data=', self.data)


class Digital_Computer(Computer):
    def __init__(self, generation, operational_method):
        Computer.__init__(self, generation)
        # Analog_computer.__init__(self, generation, data)
        self.operational_method = operational_method

    def print(self):
        print("operational_method:", self.operational_method)


class Hybrid_Computer(Digital_Computer, Analog_Computer):
    def __init__(self, generation, data, operational_method):
        Analog_Computer.__init__(self, generation, data)
        Digital_Computer.__init__(self, generation, operational_method)

        print("hybrid_computers are:")


c = Hybrid_Computer('Third', 'analog and digital', 'discrete')
c.display()
c.display_name()
c.print()
print("-----------------------------------")

print("digital computers are:")
d = Digital_Computer('second', 'Discrete')
d.display()
d.print()
print("------------------------------------")

print("analog computer are:")
a = Analog_Computer('first', 'analog')
a.display()
a.display_name()
print("------------------------------------")
