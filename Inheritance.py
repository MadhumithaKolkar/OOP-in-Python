class Vehicle:
    def __init__(self):
        self.category = "vehicle"
    def general_usage(self):
        print("General usage : Transport")

class Locomotive:
    def __init__(self):
        self.category = "Locomotive"
    def purpose(self):
        print("Move around")

class Car(Vehicle,Locomotive):
    def __init__(self):
        super().__init__()
        self.wheels_count = 4
        self.has_roof = True
        print("I am a car")

    def specific_usage(self):
        print("Specific usage: Drive and go for family trips")

class MotorCycle(Vehicle):
    def __init__(self):
        self.wheels_count = 2
        self.has_roof = False
        print("I am a motorcycle")

    def specific_usage(self):
        print("Specific usage: Drive to work")

c1 = Car()
c1.general_usage()
c1.specific_usage()
c1.purpose()
print(c1.category)

m1 = MotorCycle()
m1.general_usage()
m1.specific_usage()

print(c1.wheels_count)
print("Does the vehicle have a roof ?",c1.has_roof)
print("Does the motorcycle have a roof ? ",m1.has_roof)
print(isinstance(c1,Car))
print(issubclass(Car,Vehicle))