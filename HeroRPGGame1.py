# RPG Game

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Character(object):
    def __init__(self):
        self.health = 10
        self.power = 10
    def alive(self):
        while self.health > 0:
            return True      
    def attack(self, other_character):
        other_character.health -= self.power

    def print_status(self, other_character):
        print "****You have %d health and %d power.****" % (self.health, self.power)
        print "**** Goblin has %d health and %d power.****" % (other_character.health, other_character.power)
class Hero(Character):
    def __init__(self):
        self.health = 10
        self.power = 5


class Goblin(Character):
    def __init__(self):
        self.health = 6
        self.power = 2

class Zombie(Character):
    def __init__(self):
        self.health = 100000
        self.power = 0



def main():
    hero = Hero()   
    goblin = Goblin()    
    zombie = Zombie()  

    while goblin.alive() and hero.alive():
        hero.print_status(goblin)
        # goblin.print_status()
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "4. fight Zombie"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
                # goblin_health -= hero_power
            print "You do %d damage to the goblin." % hero.power
            if goblin.health <= 0:
                print "The goblin is dead."
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        elif input == "4":
            # Hero attacks zombie
            hero.attack(zombie)
            print "You do %d damage to the zombie." % hero.power
            print "Zombie cannot die!!"
            if zombie.health <= 0:
                print "The zombie is dead."
            
        else:
            print "Invalid input %r" % input
        

        if goblin.alive() and input != "4":
            # Goblin attacks hero
            goblin.attack(hero)
                #hero_health -= goblin_power
            print "The goblin does %d damage to you." % goblin.power
            if not hero.alive():
                print "You are dead."



main()
