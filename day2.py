<<<<<<< HEAD
class Fighter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def describe(self):
        print(f"{self.name} has {self.health} HP")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage! HP left: {self.health}")

        def heal_amount(self, heal):
        self.health += heal
        print(f"{self.name} healed {heal} HP! HP now: {self.health}")

    def is_alive(self):
        if self.health <= 0:
            print(f"{self.name}You Are Dead! Train Harder!")
        else:
            print(f"{self.name} You are still Alive Keep Going!")


fighter_1 = Fighter("Abdul", 100)
fighter_2 = Fighter("Enemy", 80)

fighter_1.describe()
fighter_2.describe()
fighter_1.take_damage(25)
fighter_2.take_damage(70)
fighter_1.heal_amount(50)
fighter_2.heal_amount(20)
fighter_1.is_alive()
fighter_2.is_alive()
=======
class Fighter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def describe(self):
        print(f"{self.name} has {self.health} HP")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage! HP left: {self.health}")

        def heal_amount(self, heal):
        self.health += heal
        print(f"{self.name} healed {heal} HP! HP now: {self.health}")

    def is_alive(self):
        if self.health <= 0:
            print(f"{self.name}You Are Dead! Train Harder!")
        else:
            print(f"{self.name} You are still Alive Keep Going!")


fighter_1 = Fighter("Abdul", 100)
fighter_2 = Fighter("Enemy", 80)

fighter_1.describe()
fighter_2.describe()
fighter_1.take_damage(25)
fighter_2.take_damage(70)
fighter_1.heal_amount(50)
fighter_2.heal_amount(20)
fighter_1.is_alive()
fighter_2.is_alive()
>>>>>>> 2bc073d92990917a456f9e8034dd73cce3eae219
