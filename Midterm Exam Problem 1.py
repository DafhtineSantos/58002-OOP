class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:

            self.radius = radius
        elif diameter is not None:

            self.radius = diameter / 2
        else:

            raise ValueError("Either radius or diameter must be provided")

    def area(self):
        return 3.14 * self.radius ** 2

    def peri(self):
        return 2 * 3.14 * self.radius


r = float(input("Enter the radius of the circle: "))

c = Circle(radius=r)

print("The area of the circle is:", c.area())
print("The perimeter of the circle is:", c.peri())