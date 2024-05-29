from default_stats import *
from enemy_list import *
import random

# enemy initialisation
enemy = voidranger_trampler_lvl95()

# skill point mechanic
skillPoints = 3
MAX_SP = 5

def changeSkillPoints(change):
    global skillPoints
    skillPoints += change
    skillPoints = min(skillPoints, MAX_SP)

# playable character class
class Character:
    def __init__(self, atk=ATK, max_hp=HP, defen=DEF, cr=CRIT_RATE, cd=CRIT_DAMAGE, max_er = MAX_ENERGY):
        self.atk = atk
        self.max_hp = max_hp
        self.hp = max_hp
        self.defen = defen
        self.cr = cr
        self.cd = cd
        self.max_er = max_er
        self.curr_energy = 0
    
    def basic_attack(self, enemy, multiplier=0.9):
        
        broken_multiplier = 1 if enemy.toughness == 0 else 0.9
        enemy_def_multiplier = 1-(enemy.defen/(enemy.defen+200+10*enemy.level))

        # non crit damage number
        actual_damage = self.atk * multiplier * enemy_def_multiplier * broken_multiplier
        
        # crit check, if crit multiplies by cd
        crit = random.random() < self.cr
        if crit:
            actual_damage *= self.cd
        print("Damage done: {}; Crit: {}".format(actual_damage, crit))
        
        # adds a skill point
        changeSkillPoints(1)

        # toughness damage
        toughnessDmg = 30

        # energy restored
        energy = self.curr_energy
        self.curr_energy = min(energy+20, 100)

        enemy.hp -= actual_damage
        enemy.toughness -= toughnessDmg

        # returns dmg dealt and crit info
        return actual_damage, crit, toughnessDmg
    
    def take_damage(self, incoming_damage):
        enemy_lvl = 80
        def_multiplier = 1-(self.defen/(self.defen+200+10*enemy_lvl))
        damage_taken = incoming_damage * def_multiplier
        self.hp -= damage_taken
        print("Player takes {} damage. HP: {}".format(damage_taken, self.hp))
        return max(self.hp, 1)
        
    
    def __str__(self):
        return f"ATK: {self.atk}\nHP: {self.hp}/{HP}\nEnergy: {self.curr_energy}/{self.max_er}"

# enemy class
pathless_char = Character()

pathless_char.basic_attack(enemy)
print(pathless_char)
print(skillPoints)


