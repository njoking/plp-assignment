# Base class (optional, for structure)
class Mover:
    def move(self):
        raise NotImplementedError("Subclasses should implement this method")


# Vehicle classes
class Car(Mover):
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane(Mover):
    def move(self):
        print("✈️ The plane is flying in the sky.")

class Boat(Mover):
    def move(self):
        print("🚤 The boat is sailing on the water.")


# Animal classes
class Dog(Mover):
    def move(self):
        print("🐶 The dog is running happily.")

class Fish(Mover):
    def move(self):
        print("🐟 The fish is swimming in the pond.")

class Bird(Mover):
    def move(self):
        print("🕊️ The bird is soaring through the air.")

class Snake(Mover):
    def move(self):
        print("🐍 The snake is slithering on the ground")

class Centipede(Mover):
    def move(self):
        print("🦂 The centipede crawls in the land")

# Polymorphism in action
def describe_movement(movers):
    for mover in movers:
        mover.move()


# Creating objects
car = Car()
plane = Plane()
boat = Boat()
dog = Dog()
fish = Fish()
bird = Bird()
snake = Snake()
centipede = Centipede()

# List of different movers
movers_list = [car, plane, boat, dog, fish, bird, snake, centipede]

# Show how each one moves
describe_movement(movers_list)
