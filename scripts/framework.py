import scripts.printing_utility as pu
import scripts.save_handler as save
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
    match user_input:
        case "1":
            monsters_menu()
        case "2":
            inventory_menu()
        case "3":
            crafting_menu()
        case "4":
            stats_menu()


def monsters_menu():
    pu.clear_terminal()
    pu.print_monsters_title()
    print("Choose which Monsters you want to fight.")


def inventory_menu():
    pu.clear_terminal()
    pu.print_inventory_title()


def crafting_menu():
    pu.clear_terminal()
    pu.print_crafting_title()

def stats_menu():
    pu.clear_terminal
    print("Stats menu goes here")

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