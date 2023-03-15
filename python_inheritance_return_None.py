#######如果不给子类加return，则一直return None###########
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        aa=str("The seating capacity of a {} is {} passengers".format(self.name,capacity))
        return aa

# Implement your code below:
class Bus(Vehicle):
    def seating_capacity(self,capacity=80):
        return super().seating_capacity(capacity) #####This is the key!!!


b=Bus("aa","20","mm")
a=b.seating_capacity()
