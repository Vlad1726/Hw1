class Dog:
    def __init__(self, name):
        self.sleepiness = 0
        self.happines = 50
        self.hunger = 0
        self.alive = True

    def to_sleep(self):
        print("Eyes are getting heavier and heavier")
        self.sleepiness = 0

    def to_eat(self):
        print("Sweets are waiting!")
        self.hunger -= 10

    def to_play(self):
        print("The owner is already waiting")
        self.happines += 25
        self.hunger += 10

    def is_alive(self):
        if self.sleepiness => 100:
            print("You can't live without sleeping")
            self.alive = False
        elif self.hunger <= 0
            print("Is the sweets really over?")
            self.alive = False
        elif self.hunger => 100
            print("Too much sweets! You overeat")
            self.alive = False
        elif self.happines => 250
            print("You are the happiest dog ever!")
                break
        elif self.happines <= 0
            print("You are the saddest dog :(")
            self.alive = False

        def end_of_day(self):
            self.happines -= 10
            print(f"Sleepiness - {self.sleepiness}")
            print(f"Happines - {self.happines}")
            print(f"Hunger - {self.hunger}")


        def live(self, day):
            day = f"Day {day} of {self.name} life"
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
    if bob.alive == False:
        break
    bob.live(day)