import scripts.printing_utility as pu
import scripts.save_handler as save
import time

def start():
    pu.clear_terminal()
    pu.print_game_title()
    print("Welcome to SomeFantasyGame ! Would you like to load your save ?\n\n")
    user_input = input(f"{pu.Colors.input_blue}[1]{pu.Colors.reset} - New\n{pu.Colors.white_b}Input - {pu.Colors.reset}")
    pu.clear_terminal()
    if user_input == "1":
        save.new(save.savetemplate_path,save.save_path)
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
    user_input = str(input(f"{pu.Colors.input_blue}[1]{pu.Colors.reset} - Fight\n{pu.Colors.input_blue}[2]{pu.Colors.reset} - Inventory\n{pu.Colors.input_blue}[3]{pu.Colors.reset} - Craft\n{pu.Colors.input_blue}[4]{pu.Colors.reset} - Stats\n{pu.Colors.white_b}Input - {pu.Colors.reset}"))

def monsters():
    pu.clear_terminal()
    pu.print_monsters_title()

def inventory():
    pu.clear_terminal()
    pu.print_inventory_title()

def crafting():
    pu.clear_terminal()
    pu.print_crafting_title()