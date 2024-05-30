class voidranger_trampler_lvl95:
    def __init__(self):
        self.level = 95
        self.atk = 718
        self.max_hp = 301193
        self.hp = 301193
        self.defen = 1150
        self.eff_h_r = 0.36
        self.eff_res = 0.3
        self.max_toughness = 300
        self.toughness = 300
        self.defense_reduction = 0

    def take_damage(self, incoming_damage, toughness_dmg=30):
        #def_multiplier = 1-(self.defen/(self.defen+200+10*80))
        def_multiplier = (100)/((self.level+20)*(1-self.defense_reduction)+100)
        damage_taken = incoming_damage*def_multiplier
        self.hp -= damage_taken
        self.toughness -= toughness_dmg
        print("Enemy takes {} damage. HP: {}/{}\nToughness: {}/{}".format(damage_taken, self.hp, self.max_hp, self.toughness, self.max_toughness))
        return max(self.hp, 1)
    
    def attack(self):
        multiplier = 4
        return self.atk * multiplier


