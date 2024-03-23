class Monster:
    def __init__(self,max_health,defense,speed,damage,crit_chance):
        self.max_health = max_health
        self.defense = defense
        self.speed = speed
        self.damage = damage
        self.crit_chance = crit_chance
        self.health = self.max_health

    def attack(self):
        #todo player.health -= self.damage
        print(f"Dealt {self.damage} damage")

    def heal(self,heal_amount:float):
        self.health += self.max_health * heal_amount # Heals by a percentage of max health