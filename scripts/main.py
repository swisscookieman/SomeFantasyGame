import printing_utility as pu
import scripts.save_handler as save
import traceback
import logging


def main():
    pu.clear_terminal()
    pu.print_game_title()
    print("Welcome to SomeFantasyGame ! Would you like to load your save ?\n\n")
    user_input = input(f"{pu.Colors.input_blue}[1]{pu.Colors.reset} - Load\n{pu.Colors.input_blue}[2]{pu.Colors.reset} - New Save\n{pu.Colors.white_b}Input - {pu.Colors.reset}")
    pu.clear_terminal()
    if user_input == "2":
        save.new(save.save_path,save.savetemplate_path)
    print(f"{pu.Colors.warning_yellow}Starting game.{pu.Colors.reset}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        logging.critical(e)
