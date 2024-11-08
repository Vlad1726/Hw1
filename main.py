import random

class Dog:
    def __init__(self, name):
        self.name = name
        self.sleepiness = 0
        self.happiness = 100
        self.hunger = 100
        self.alive = True

    def to_sleep(self):
        print("You choice is sleeping")
        print("Eyes are getting heavier and heavier")
        self.sleepiness -= 25

    def to_eat(self):
        print("You choice is eating")
        print("Sweets are waiting!")
        self.hunger += 25
        self.sleepiness += 25

    def to_play(self):
        print("You choice is playing")
        print("The owner is already waiting")
        self.happiness += 50
        self.hunger -= 25

    def is_alive(self):
        if self.sleepiness >= 100:
            print("You can't live without sleeping")
            self.alive = False
        elif self.hunger <= 0:
            print("Is the sweets really over?")
            self.alive = False
        elif self.happiness >= 500:
            print("You are the happiest dog ever!")
            self.alive = False
        elif self.happiness <= 0:
            print("You are the saddest dog :(")
            self.alive = False

    def end_of_day(self):
        self.happiness -= 10
        print(f"Sleepiness - {self.sleepiness}")
        print(f"Happiness - {self.happiness}")
        print(f"Hunger - {self.hunger}")

    def live(self, day):
        day = f"Day {day} of {self.name}'s life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_sleep()
        elif live_cube == 2:
            self.to_eat()
        elif live_cube == 3:
            self.to_play()
        self.end_of_day()
        self.is_alive()

bob = Dog("Bob")
for day in range(365):
    if not bob.alive:
        break
    bob.live(day)

