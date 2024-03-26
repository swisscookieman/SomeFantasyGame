import scripts.printing_utility as pu
import scripts.save_handler as save
import time

def start():
    pu.clear_terminal()
    pu.print_game_title()
    print("Welcome to SomeFantasyGame ! Would you like to load your save ?\n\n")
    user_input = input(f"{pu.Colors.input_blue}[1]{pu.Colors.reset} - Load\n{pu.Colors.input_blue}[2]{pu.Colors.reset} - New Save\n{pu.Colors.white_b}Input - {pu.Colors.reset}")
    pu.clear_terminal()
    if user_input == "2":
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
