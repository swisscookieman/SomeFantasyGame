import printing_utility as pu
import traceback
import logging


def main():
    pu.clear_terminal()
    pu.print_game_title()
    print("Welcome to SomeFantasyGame ! Would you like to load your save ?\n\n")
    user_input = input("\033[38;2;0;0;255mwajwdn\033[0m")
    match user_input:
        case 1:
            pass
        case 2:
            pass
        case _ :
            pass

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        logging.critical(e)
