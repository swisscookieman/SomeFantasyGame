import scripts.framework as framework
import traceback
import logging
import time


def main():
    framework.start()
    time.sleep(0.25)
    framework.main_menu()
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        logging.critical(e)
