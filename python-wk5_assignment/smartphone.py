# Base class
class Smartphone:
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self.__battery = battery_capacity  # Encapsulated attribute

    def charge(self, amount):
        if amount + self.__battery > 100:
            self.__battery = 100
        else:
            self.__battery += amount
        print(f"{self.model} charged. Battery at {self.__battery}%")

    def use(self, amount):
        if amount > self.__battery:
            print(f"{self.model} battery heading to critical level. please charge!")
        else:
            self.__battery -= amount
            print(f"{self.model} used. Battery at {self.__battery}%")

    def get_battery(self):
        return self.__battery

    def show_info(self):
        print(f"📱 {self.brand} {self.model} - Battery: {self.__battery}%")


class SmartphoneWithFastCharging(Smartphone):
    def charge(self, amount):
       
        fast_amount = amount * 2
        super().charge(fast_amount)  


# Usage
phone1 = Smartphone("Samsung", "Galaxy S21", 70)
phone2 = SmartphoneWithFastCharging("OnePlus", "9 Pro", 40)

# Normal phone
phone1.show_info()
phone1.use(30)
phone1.charge(20)

print()

# Fast-charging phone
phone2.show_info()
phone2.use(10)
phone2.charge(20)  

print()


try:
    print(phone1.__battery)
except AttributeError:
    print("🔒 Battery cannot be accesed directly. Try Using getter method.")
