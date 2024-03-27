import scripts.save_handler as save
import scripts.menus as menus
import traceback
import logging
import time


def main():
    data = save.get_data()
    menus.start()
    time.sleep(0.25)
    menus.main_menu(data)
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        logging.critical(e)
