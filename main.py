import printing_utility as pu
import save_handler as save
import traceback
import logging


def main():
    pu.clear_terminal()
    pu.print_game_title()
    print("Welcome to SomeFantasyGame ! Would you like to load your save ?\n\n")
    user_input = input(f"{pu.Colors.input_blue}[1]{pu.Colors.reset} - Load\n{pu.Colors.input_blue}[2]{pu.Colors.reset} - New Save\n{pu.Colors.white_b}Input - {pu.Colors.reset}")
    pu.clear_terminal()
    match user_input:
        case "1":
            save.load(save.savepath)
        case "2":
            save.new(save.savepath)
        case _ :
            print(f"{pu.Colors.warning_yellow}Loading save by default{pu.Colors.reset}") # We may have to redo this
            save.load(save.savepath)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        logging.critical(e)
