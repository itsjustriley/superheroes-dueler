from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")
        self.teams = [self.team_one, self.team_two]

    def create_ability(self):
        name = input("What is the ability name?  ")
        max_damage = input("What is the max damage of the ability?  ")
        return Ability(name, max_damage)
    
    def create_weapon(self):
        name = input("What is the weapon name?  ")
        max_damage = input("What is the max damage of the weapon?  ")
        return Weapon(name, max_damage)
    
    def create_armor(self):
        name = input("What is the armor name?  ")
        max_block = input("What is the max block of the armor?  ")
        return Armor(name, max_block)
    
    def create_hero(self):
        hero_name = input("Hero's name:  ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("What do you want to add?\n1. Ability\n2. Weapon\n3. Armor\n4. Done adding items\n> ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())
        return hero
        
    def build_team_one(self):
        numOfTeamMembers = int(input("How many members would you like on Team One?\n> "))
        for i in range(numOfTeamMembers):
            self.team_one.add_hero(self.create_hero())
    
    def build_team_two(self):
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n> "))
        for i in range(numOfTeamMembers):
            self.team_two.add_hero(self.create_hero())

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def team_kdr(self, team):
        kills = 0
        deaths = 0
        for hero in team.heroes:
            kills += hero.kills
            deaths += hero.deaths
        if kills == 0 and deaths == 0:
            print(f'{team.name} average KD was: 0')
            return
        elif deaths == 0:
            print(f'{team.name} average KD was: {kills}')
            return
        else:
            print(f'{team.name} average KD was: {kills/deaths}')


    def survivors(self, team):
        survivors = 0
        print(f'{team.name} survivors:')
        for hero in team.heroes:
            if hero.is_alive():
                print(hero.name)
                survivors += 1
        return survivors

    def show_stats(self):
        team_one_survivors = 0
        team_two_survivors = 0
        print("\n")
        print(f'{self.team_one.name} vs {self.team_two.name}')
        print("\n")
        
        for team in self.teams:
            print(f'{team.name} Statistics')
            team.stats()
            print("\n")
            self.team_kdr(team)
            print("\n")
            if team == self.team_one:
                team_one_survivors = self.survivors(team)
            elif team == self.team_two:
                team_two_survivors = self.survivors(team)
            print("\n")
        if team_one_survivors > team_two_survivors:
            print(f'{self.team_one.name} wins!')
        elif team_two_survivors > team_one_survivors:
            print(f'{self.team_two.name} wins!')
        else:
            print("Draw!")
    
if __name__ == "__main__":
    game_is_running = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")
        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()


        



