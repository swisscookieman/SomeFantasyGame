import printing_utility as pu

class Level:
    def __init__(self, level, xp):
        self.level = level
        self.xp = xp
        self.levelrequirements = 100*(self.level/2)^2

    def add_xp(self, amount):
        self.xp += amount
        print(f"You gained {amount} xp.\nYou now have {self.xp} xp")
        self.check_lvl()

    def check_lvl(self):
        print(f"The next level requires {self.levelrequirements[self.level]} xp, as you are level {self.level}")
        pu.progressbar(self.xp, self.levelrequirements, 20)
        if self.xp >= self.levelrequirements:
            self.xp -= self.levelrequirements
            self.level += 1
            print(f"You leveled up! You are now {self.level} and have {self.xp} towards the next level.")
            if self.xp >= self.levelrequirements:
                self.check_lvl()