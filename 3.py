#create two parent classes Hero and Villain, each with attributes name and private attribute power. 
#add a method in each parent class to access the private attribute .
#create at least one child class for each parent class that inherits from it. in each child class creat a method that uses the parent attributes.
#use input() to allow the user to enter the name and power for the both characters and display their information on screen and call the child class method.  
class Hero:
    def __init__(self, name, power):
        self.name = name
        self.__power = power

    def get_power(self):
        return self.__power

class Villain:
    def __init__(self, name, power):
        self.name = name
        self.__power = power

    def get_power(self):
        return self.__power

class SuperHero(Hero):
    def __init__(self, name, power):
        super().__init__(name, power)

    def display_info(self):
        print(f"Hero: {self.name}, Power: {self.get_power()}")
        
class SuperVillain(Villain):
    def __init__(self, name, power):
        super().__init__(name, power)

    def display_info(self):
        print(f"Villain: {self.name}, Power: {self.get_power()}")

hero_name = input("Enter the hero's name: ")
hero_power = input("Enter the hero's power: ")
villain_name = input("Enter the villain's name: ")
villain_power = input("Enter the villain's power: ")

hero = SuperHero(hero_name, hero_power)
villain = SuperVillain(villain_name, villain_power)

hero.display_info()
villain.display_info()