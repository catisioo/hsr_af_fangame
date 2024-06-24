class voidranger_trampler_lvl95:
    def __init__(self):
        self.level = 95
        self.atk = 718
        self.max_hp = 301193
        self.hp = 300000
        self.defen = 1150
        self.eff_h_r = 0.36
        self.eff_res = 0.3
        self.max_toughness = 300
        self.toughness = 300
        self.defense_reduction = 0

    def attack(self):
        multiplier = 4
        return self.atk * multiplier
    
    def __str__(self):
        return f"HP:{self.hp}/{self.max_hp}; Toughness:{self.toughness}/{self.max_toughness}"
    
    def calculate_def_multiplier(self):
        return 100 / ((self.level + 20) * (1 - self.defense_reduction) + 100)
    
    def calculate_toughness_multipilier(self):
        if self.toughness > 0:
            return 0.9
        else:
            return 1

    
    def takeDOT(self, target, dotMultiplier):
        enemy_def_multiplier = self.calculate_def_multiplier()
        actual_damage = target.atk * dotMultiplier * enemy_def_multiplier
        self.hp -= actual_damage
        print("Enemy takes {} dot.".format(actual_damage))
        return actual_damage

    def takeBrokenDmg(self, target):
        enemy_def_multiplier = self.calculate_def_multiplier()
        actual_damage = target.atk * target.break_effect_multiplier() * enemy_def_multiplier
        self.hp -= actual_damage
        print("Enemy takes {} break effect.".format(actual_damage))
        return actual_damage




