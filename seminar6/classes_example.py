import random


class Warrior:
    nr_warriors = 0

    def __init__(self, name, weapon, health):
        Warrior.nr_warriors += 1
        self.__name = name
        self.__weapon = weapon
        self.__health = health

    def get_name(self):
        return self.__name

    def get_weapon(self):
        return self.__weapon

    def get_health(self):
        return self.__health

    def set_health(self, new_health):
        self.__health = new_health

    def attack(self, warrior):
        attack_points = random.randint(0, 10)
        warrior.set_health(warrior.get_health() - attack_points)
        if warrior.is_alive():
            print(f"{warrior.get_name()} got hurt, down to {warrior.get_health()}")
            return
        print(f"{warrior.get_name()} died!")

    def is_alive(self):
        return self.get_health() > 0

    def __add__(self, other):
        return Warrior(f"{self.get_name()}-{other.get_name()}", "sword", 1000)

    def __str__(self):
        return f"Warrior(name={self.get_name()}, weapon={self.get_weapon()} health={self.get_health()})"

    def __repr__(self):
        return str(self)


class Army:
    def __init__(self, name, nr_soldiers):
        self.__name = name
        self.__soldiers = [
            Warrior(f"f{name}-{index}", "sword", 100) for index in range(nr_soldiers)
        ]


if __name__ == "__main__":
    import time

    bob = Warrior("Conan", "sword", 100)
    bob2 = Warrior("Conan 2", "sword", 100)
    print(bob - bob2)
    # print(f'type(bob)={type(bob)}, type(Warrior)={type(Warrior)}, type(type)={type(type)}')
    # while bob.is_alive() and bob2.is_alive():
    #     time.sleep(0.5)
    #     bob.attack(bob2)
    #
    #     bob2.attack(bob)
