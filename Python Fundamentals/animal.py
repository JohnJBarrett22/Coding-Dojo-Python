class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print(str(self.name) + "\nHealth: " + str(self.health))
        return self

animal_one = Animal("Goliath", 100)
animal_one.walk().walk().walk().run().run().display_health()


class Dog(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 150
    
    def pet(self):
        self.health += 5
        return self

dog_one = Dog("Kitty", 100)
dog_one.walk().walk().walk().run().run().pet().display_health()


class Dragon(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 170
    
    def fly(self):
        self.health -= 10
        return self
    
    def display_health_drag(self):
         super().display_health()
         print("I am a dragon")
         return self        

dragon_one = Dragon("Hopper", 100)
dragon_one.fly().fly().fly().display_health_drag()


class Pig(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 250
    
    def oink(self):
        self.health += 10
        return self
    
    def display_health_pig(self):
         super().display_health()
         print("I am a piglet")
         return self        

pig_one = Pig("Hammerton", 100)
pig_one.oink().oink().oink().display_health_pig()