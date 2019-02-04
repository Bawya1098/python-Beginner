class Circle:
    radius = 5

    def area(self, radius):
        self.area = 3.14 * radius * radius
        print(self.area)

    def perimeter(self, radius):
        self.perimeter = 2 * 3.14 * radius
        print(self.perimeter)


c = Circle()
c.area(Circle.radius)
c.perimeter(Circle.radius)
