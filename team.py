import random 

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
    
    def stats(self):
        for hero in self.heroes:
            if hero.deaths == 0:
                kd = hero.kills
            elif hero.kills == 0:
                kd = 0
            else:
                kd = hero.kills / hero.deaths
            print(f'{hero.name} Kill/Deaths:{kd}')
    
    def add_hero(self, hero):
        self.heroes.append(hero)
    
    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0
    
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        living_heroes = []
        living_opponents = []
        for hero in self.heroes:
            living_heroes.append(hero)
        for hero in other_team.heroes:
            living_opponents.append(hero)
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)
            hero.fight(opponent)
            if hero.is_alive():
                living_opponents.remove(opponent)
            elif opponent.is_alive():
                living_heroes.remove(hero)
            else:
                living_heroes.remove(hero)
                living_opponents.remove(opponent)
            