class Person:
    def __init__(self, std, pre, mid, fin):
        self.__std = std
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin

    def Grade(self):
        return (self.__pre + self.__mid + self.__fin) / 3

    def display(self):
        print(f"Student: {self.__std}\n")
        print(f"Prelim Grade: {self.__pre}")
        print(f"Midterm Grade: {self.__mid}")
        print(f"Final Grade: {self.__fin}\n")
        print(f"Average Grade: {round(self.Grade(), 2)}\n\n")

class Student1(Person):
    pass

class Student2(Person):
    pass

class Student3(Person):
    pass

std1 = Student1("Student 1", 90, 92, 94)
std1.display()

std2 = Student2("Student 2", 95, 89, 97)
std2.display()

std3 = Student3("Student 3", 98, 97, 98)
std3.display()

# Encapsulation Test
std2.std = "JUSTIN"
std2.pre = 50
std2.mid = 40
std2.fin = 30
std2.display()