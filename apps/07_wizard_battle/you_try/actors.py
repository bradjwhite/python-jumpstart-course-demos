import random


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature {} of level {}".format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Dragon(Creature):
    def __init__(self, name, level, scale_thickness):
        super().__init__(name, level)


class Wizard(Creature):

    def attack(self, creature):
        print('The wizard {} attacks {}!'.format(
            self.name, creature.name
        ))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print("You roll {} ...".format(my_roll))
        print("{} rolls {}...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has handily triumphed over {}".format(creature.name))
            return True
        else:
            print("The wizard has been DEFEATED!!!")
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breathes_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier
