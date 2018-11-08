class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print("This bike has a price of",self.price,", a maximum speed of",self.max_speed, "and a total of", self.miles, "miles on it.")
        return self

    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    
    def reverse(self):
        print("Reversing")
        if self.miles >= 5:
            self.miles -= 5
        return self
  
new_bike1 = Bike(199,"25mph")
new_bike1.ride().ride().ride().reverse().displayInfo()

new_bike2 = Bike(399, "32mph")
new_bike2.ride() .ride().reverse().reverse().displayInfo()

new_bike3 = Bike(89, "14mph")
new_bike3.reverse().reverse().reverse().displayInfo()

