class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    
    def display_all(self):
        print("Price: " + str(self.price))
        print("Speed: " + str(self.speed))
        print("Fuel: " + str(self.fuel))
        print("Mileage: " + str(self.mileage))
        print("Tax: " + str(self.tax))
        return self

car_one = Car(2000,"35mph", "Full", "15mpg")
car_one.display_all()

car_two = Car(2000,"5mph", "Not Full", "105mpg")
car_two.display_all()

car_three = Car(2000,"15mph", "Kind of Full", "95mpg")
car_three.display_all()

car_four =  Car(2000,"25mph", "Full", "25mpg")
car_four.display_all()

car_five = Car(2000,"45mph", "Empty", "25mpg")
car_five.display_all()

car_six = Car(20000000,"35mph", "Empty", "15mpg")
car_six.display_all()


