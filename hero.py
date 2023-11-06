# import random 
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    self.weight = 0
    self.abilities = []
    self.armors = []

  def add_weapon(self, weapon):
    self.abilities.append(weapon)

  def add_ability(self, ability):
    self.abilities.append(ability)

  def attack(self):
    atk_damage = 0
    for ability in self.abilities:
      atk_damage += ability.attack()
    return atk_damage
  
  def defend(self):
    total_blk = 0
    for armor in self.armors:
      total_blk += armor.block()
    return total_blk
  
  def take_damage(self, incoming_damage):
    health_lost = incoming_damage - self.defend()
    self.current_health -= health_lost
  
  def is_alive(self):
    if self.current_health > 0:
      return True
    else:
      return False
  
  def fight(self, opponent):
    if len(self.abilities) == 0 and len(opponent.abilities) == 0:
      print("Draw!")
    else:
      while self.is_alive() and opponent.is_alive():
        self.take_damage(opponent.attack())
        opponent.take_damage(self.attack())
      if self.is_alive():
        print(f'{self.name} wins!')
      elif opponent.is_alive():
        print(f'{opponent.name} wins!')
      else:
        print("Draw! Both heroes are defeated.")
    # PREVIOUS CODE, WHEN IT WAS RANDOMIZED
    # options = [self, opponent]
    # total_power = 0
    # weight_list = []
    # for hero in options: 
    #   total_power += hero.power
    # for hero in options:
    #   hero.weight = hero.power / total_power
    #   weight_list.append(hero.weight)
    # winner = (random.choices(options, weights=weight_list, k=1)[0])
    # print(f'{winner.name} wins! ')
      
  def add_armor(self, armor):
    self.armors.append(armor)

  def defend(self):
    total_block = 0
    for armor in self.armors:
      total_block += armor.block()
    return total_block
  
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())