class Product:
    def __init__(self, item_name, price, weight, brand):
        self.item_name = item_name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    
    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.price = self.price + (self.price * tax)
        return self
    
    def return_item(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        if reason_for_return == "like new":
            self.status = "for sale"
        if reason_for_return == "opened":
            self.status = "used"
            self.price = self.price - (self.price * 0.20)
        return self

    def display_info(self):
        print("Item Name: " + str(self.item_name))
        print("Price: " + str(self.price))
        print("Weight: " + str(self.weight))
        print("Brand: " + str(self.brand))
        print("Status: " + str(self.status))
        return self

product_one = Product("Peas", 3.99, 0.16, "Green Giant")
product_one.display_info() .return_item("opened") .display_info()

product_two = Product("Forks", 7.99, 0.75, "Select Kitchen")
product_two.display_info() .return_item("like new") .display_info()

product_three = Product("Diapers", 33.99, 4.25, "Huggies")
product_three.display_info() .return_item("defective") .display_info()

product_four = Product("Crayons", 4.99, 0.25, "Crayola")
product_four.display_info() .add_tax(0.12) .display_info()

product_five = Product("Crayons", 4.99, 0.25, "Crayola")
product_five.display_info() .sell() .display_info()