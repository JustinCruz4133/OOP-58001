class DistanceConversion:
    def __init__(self, distance):
        self.__distance = distance

    def MtoCm(self):
        return self.__distance * 100

    def MtoKm(self):
        return self.__distance / 1000

    def MtoI(self):
        return self.__distance * 39.37

    def display(self):
        print(f"\n{self.__distance} Meters")
        print(f"is equivalent to:\n")
        print(f"Centimeter: {self.MtoCm()}")
        print(f"Kilometer: {self.MtoKm()}")
        print(f"Inch: {round(self.MtoI(), 2)}")

InputDistance = int(input("Enter Distance in Meters: "))

user = DistanceConversion(InputDistance)
user.display()