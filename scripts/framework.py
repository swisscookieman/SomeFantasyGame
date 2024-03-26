import printing_utility as pu


def main_menu():
    pass


class Level:
    levelrequirements = [0, 1000, 2000, 3000, 400]
    level = 1
    xp = 0

    def __init__(self) -> None:
        pass

    def add_xp(self, amount):
        self.xp += amount
        print(f"you have {self.xp} xp")
        self.check_lvl()

    def check_lvl(self):
        print(
            f"the next level requires {self.levelrequirements[self.level]} xp, as you are level {self.level}")
        pu.progressbar(self.xp, self.levelrequirements[self.level], 20)
        if self.xp >= self.levelrequirements[self.level]:
            self.xp -= self.levelrequirements[self.level]
            self.level += 1
            print(
                f"you leveled up, you are now {self.level} and have {self.xp} to the next level.")
            if self.xp >= self.levelrequirements[self.level]:
                self.check_lvl()


your_level = Level()
your_level.add_xp(500)
