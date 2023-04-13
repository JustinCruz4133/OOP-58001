class Circle:
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi

    def Area(self):
        return self.pi * self.radius ** 2

    def Perimeter(self):
        return 2 * self.pi * self.radius

    def Display(self):
        print("\nA Circle with a radius of", self.radius, "centimeters")
        print("Will have a/an:")
        print("Area:", round(self.Area(), 2), "centimeters")
        print("Perimeter:", round(self.Perimeter(), 2), "centimeters")


r = int(input("Enter the Radius of the Circle (in Centimeters): "))

user = Circle(r, 3.141592653589793)
user.Display()
