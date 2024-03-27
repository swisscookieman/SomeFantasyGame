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


def main_menu(data):
    pu.clear_terminal()
    pu.print_game_title()
    data = save.get_data()
    print(f"Welcome back {data['playername']}!\n")
    user_input = str(input(
        f"{pu.Colors.input_blue}[1]{pu.Colors.reset} - Fight\n{pu.Colors.input_blue}[2]{pu.Colors.reset} - Inventory\n{pu.Colors.input_blue}[3]{pu.Colors.reset} - Craft\n{pu.Colors.input_blue}[4]{pu.Colors.reset} - Shop\n{pu.Colors.input_blue}[5]{pu.Colors.reset} - Stats\n{pu.Colors.white_b}Input - {pu.Colors.reset}"))
    match user_input:
        case "1":
            monsters_menu()
        case "2":
            inventory_menu(data)
        case "3":
            crafting_menu()
        case "4":
            shop_menu()
        case "5":
            stats_menu()


def monsters_menu():
    pu.clear_terminal()
    pu.print_monsters_title()
    print("Where are you travelling ?")


def inventory_menu(data):
    pu.clear_terminal()
    pu.print_inventory_title()
    print(f"This is your inventory, you currently own {len(data['owned_items'])} items.\n")
    for item in data['owned_items']:
        print(f"{data['owned_items'][item]}") # need to make this clear

def shop_menu():
    pu.clear_terminal()
    print("Shop menu goes here")

def crafting_menu():
    pu.clear_terminal()
    pu.print_crafting_title() # Will do this later, nothing to do here for now
    print("Here you can craft materials into valuables")

def stats_menu():
    pu.clear_terminal
    print("Stats menu goes here")