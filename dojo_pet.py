# Create a Ninja class with the ninja attributes listed above.
class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        pet.play
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method



class Pet:
    def __init__(self,name,type,tricks,health,energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
    def eat(self):
       self.energy += 5
       self.health += 10
    def play(self):
        self.health += 5
    def noise(self,animal_sound):
        animal_sound =input(f'what type of sound does your {Pet} make?')
        print(animal_sound)
    
        