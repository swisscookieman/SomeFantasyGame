import logging
import traceback
import printing_utility as pu


def main():
    pu.print_game_title()
    



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        logging.critical(e)
