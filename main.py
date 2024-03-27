import scripts.framework as framework
import scripts.save_handler as save
import traceback
import logging
import time
import json


def main():
    data = save.get_data()
    framework.start()
    time.sleep(0.25)
    framework.main_menu(data)
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        logging.critical(e)
