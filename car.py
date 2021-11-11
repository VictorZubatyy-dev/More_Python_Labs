class Car:
    def __init__(self, make, model, year, colour ="blue"):
        self.colour = colour
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print("This" + self.make + "drives.")

    def stop(self):
        print("This" + self.make + "stopped.")