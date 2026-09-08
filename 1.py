class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def display_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")

car1=Vehicle("Toyota", 2010)
car2=Vehicle("Fiat", 2018)
car1.display_info()
car2.display_info()