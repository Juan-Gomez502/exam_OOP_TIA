class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "roof roof")
    
    def display_info(self):
        print(f"Animal: {self.name}, Sound: {self.sound}")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "miau")
    
    def display_info(self):
        print(f"Animal: {self.name}, Sound: {self.sound}")

dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")
dog1.display_info()
cat1.display_info()
