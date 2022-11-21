#
# Program Name: Vehicle Data Collector
#
# Author: Ayden Pitstick
#
# SDEV220
#
# 11/17/2022
#
# Description: Takes the vehicle type, year, make, model, doors and roof data from a user and displays it in a easily readable list
# 
# Variables: 
# 
# vehicleType - recives user input for the vehicle type
# year - recives user input for the vehicle year
# make - recives user input for the make of the vehicle
# model - recives user input for the model of the vehicle
# doors - recives user input for the number of doors the vehicle has
# roof - recives user input for the type of roof the vehicle has
# vehicleData - takes the Automobile class and allows it's attributes to be made human readable
# 

vehicleType = input("Enter vehicle type or type Exit to exit: ")

while vehicleType!= ("Exit"):
    year = input("Enter vehicle model year: ")
    make = input("Enter the make of the vehicle: ")
    model = input("Enter the model of the vehicle: ")
    doors = input("Enter the number of doors the vehicle has: ")
    roof = input("Enter the type of roof the vehicle has: ")
    break

class Vehicle:
     def __init__(self, vehicleType):
        self.vehicleType = vehicleType

class Automobile(Vehicle):
    def __init__ (self, vehicleType, year, make, model, doors, roof):
       super().__init__(vehicleType)
       self.year = year
       self.make = make
       self.model = model
       self.doors = doors
       self.roof = roof
    def VehicleData(self):
        print("Vehicle Type: " + vehicleData.vehicleType)
        print("Year: " + vehicleData.year)
        print("Make: " + vehicleData.make)
        print("Model: " + vehicleData.model)
        print("Number of Doors: " + vehicleData.doors)
        print("Roof Type: " + vehicleData.roof)

vehicleData = Automobile(vehicleType, year, make, model, doors, roof)

vehicleData.VehicleData()


    