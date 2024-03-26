import printing_utility as pu
import save_handler as save
import time


def start():
    pu.clear_terminal()
    pu.print_game_title()
    print("Welcome to SomeFantasyGame ! Would you like to load your save ?\n\n")
    user_input = input(
        f"{pu.Colors.input_blue}[1]{pu.Colors.reset} - New\n{pu.Colors.white_b}Input - {pu.Colors.reset}")
    pu.clear_terminal()
    if user_input == "1":
        save.new(save.savetemplate_path, save.save_path)
    print(f"{pu.Colors.warning_yellow}Starting game.{pu.Colors.reset}")
    time.sleep(0.25)
    pu.clear_terminal()
    print(f"{pu.Colors.warning_yellow}Starting game..{pu.Colors.reset}")
    time.sleep(0.25)
    pu.clear_terminal()
    print(f"{pu.Colors.warning_yellow}Starting game...{pu.Colors.reset}")


def main_menu():
    pu.clear_terminal()
    pu.print_game_title()
    data = save.get_data()
    print(f"Welcome back {data['playername']}!\n")
    user_input = str(input(
        f"{pu.Colors.input_blue}[1]{pu.Colors.reset} - Fight\n{pu.Colors.input_blue}[2]{pu.Colors.reset} - Inventory\n{pu.Colors.input_blue}[3]{pu.Colors.reset} - Craft\n{pu.Colors.input_blue}[4]{pu.Colors.reset} - Stats\n{pu.Colors.white_b}Input - {pu.Colors.reset}"))


class Level:
    # replace this with a mathematical formula
    levelrequirements = [0, 1000, 2000, 3000, 4000]
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


def monsters():
    pu.clear_terminal()
    pu.print_monsters_title()


def inventory():
    pu.clear_terminal()
    pu.print_inventory_title()


def crafting():
    pu.clear_terminal()
    pu.print_crafting_title()
