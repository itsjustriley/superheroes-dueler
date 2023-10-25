import random 

class Hero:
  def __init__(self, name, power, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    self.power = power
    self.weight = 0

  def fight(self, opponent):
    options = [self, opponent]
    total_power = 0
    weight_list = []
    for hero in options: 
      total_power += hero.power
    for hero in options:
      hero.weight = hero.power / total_power
      weight_list.append(hero.weight)
    winner = (random.choices(options, weights=weight_list, k=1)[0])
    print(f'{winner.name} wins! ')
      
  # TODO: Fight each hero until a victor emerges.
  # Phases to implement:
  #1) randomly choose winner,
  # Hint: Look into random library, more specifically the choice method

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman", 19)
    hero2 = Hero("Dumbledore", 1)

    hero1.fight(hero2)