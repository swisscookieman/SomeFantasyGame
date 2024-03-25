import animation
import time
import os


rare_drop = ['\033[96m  R', '  RA', '  RAR', '  RARE', '  RARE D', '  RARE DR', '  RARE DRO', '  RARE DROP',
             '<<RARE DROP>>', '  RARE DROP  ', '<<RARE DROP>>', '  RARE DROP  ', '<<RARE DROP>>', '  RARE DROP  ', '<<RARE DROP>>']

ultra_rare_drop = ['\033[95mULTRA', '      RARE',
                   '           DROP', '                      ', 'ULTRA RARE DROP', '                      ', 'ULTRA RARE DROP', '                      ', 'ULTRA RARE DROP', '                      ', 'ULTRA RARE DROP']

relic_drop = ["\033[93mR L C  R P", " E I  D O ", "R L C  R P",
              " E I  D O ", "R         ", "RE        ", "REL       ", "RELI      ", "RELIC     ", "RELIC D   ", "RELIC DR  ", "RELIC DRO ", "RELIC DROP", "          ", "RELIC DROP", "          ", "RELIC DROP", "          ", "RELIC DROP"]


def print_game_title():
    print("|-------------------------------------------------------------------------|")
    print("|  _____               _____         _               _____                |")
    print("| |   __|___ _____ ___|   __|___ ___| |_ ___ ___ _ _|   __|___ _____ ___  |")
    print("| |__   | . |     | -_|   __| .'|   |  _| .'|_ -| | |  |  | .'|     | -_| |")
    print("| |_____|___|_|_|_|___|__|  |__,|_|_|_| |__,|___|_  |_____|__,|_|_|_|___| |")
    print("|                                              |___|                      |")
    print("|-------------------------------------------------------------------------|\n")


def print_inventory_title():
    print("|----------------------------------------|")
    print("|  ___                 _                 |")
    print("| |_ _|_ ___ _____ _ _| |_ ___ _ _ _  _  |")
    print("|  | || ' \ V / -_) ' \  _/ _ \ '_| || | |")
    print("| |___|_||_\_/\___|_||_\__\___/_|  \_, | |")
    print("|                                  |__/  |")
    print("|----------------------------------------|\n")


def print_monsters_title():
    print("|-------------------------------------|")
    print("|  __  __             _               |")
    print("| |  \/  |___ _ _  __| |_ ___ _ _ ___ |")
    print("| | |\/| / _ \ ' \(_-<  _/ -_) '_(_-< |")
    print("| |_|  |_\___/_||_/__/\__\___|_| /__/ |")
    print("|                                     |")
    print("|-------------------------------------|\n")


def print_crafting_title():
    print("|-------------------------------------|")
    print("|   ___           __ _   _            |")
    print("|  / __|_ _ __ _ / _| |_(_)_ _  __ _  |")
    print("| | (__| '_/ _` |  _|  _| | ' \/ _` | |")
    print("|  \___|_| \__,_|_|  \__|_|_||_\__, | |")
    print("|                               |___/ |")
    print("|-------------------------------------|\n")


def play_rare_drop():
    rare_animation = animation.Wait(rare_drop, 0.05)
    rare_animation.start()
    time.sleep(4)
    rare_animation.stop()


def play_ultrarare_drop():
    ultrarare_animation = animation.Wait(ultra_rare_drop, 0.05)
    ultrarare_animation.start()
    time.sleep(2.9)
    ultrarare_animation.stop()


def play_relic_drop():
    relic_animation = animation.Wait(relic_drop, 0.05)
    relic_animation.start()
    time.sleep(5)
    relic_animation.stop()


def clear_terminal():
    os.system("clear")


class Colors:  # Please add all important colors :)
    reset = '\033[0m'
    white_b = '\033[37;1m'
    input_blue = '\033[38;2;0;0;255m'
    warning_yellow = '\033[93m'
    magic = '\033[38;2;0;0;255m'
    green = '\033[92m'
    rare = '\033[96m'
    fabled = '\033[95m'
    defence = '\033[92m'
    health = '\033[91m'
    strenght = '\033[91m'
    yellow = '\033[33m'
    pink = '\033[35m'
    stealth = '\033[38;5;18m'
    accuracy = '\033[38;5;49m'
    ranged = '\033[38;5;214m'


class Style:
    reset = '\033[0m'
    italic = '\033[3m'


class Icons:
    strenght = '❁'
    defence = '❈'
    health = '❤'
    speed = '✦'
    crit_chance = '☣'
    luck = '☘'  # unused for now
    star = '✯'
    circle_star = '✪'
    death = '☠'
    warning = '⚠'
    music = '♫'  # random ?
    cross = '✖'
    check = '✔'
    arrow = '➜'
    flag = '⚑'
    dragon = '☬'
    smiley = '☺'
    circle = '⦾'
    swords = '⚔'
    explosion = '✷'
    heat = '♨'
    wave = 'ʬ'
    heart_2 = '❣'
    empty_star_4 = '✧'
    defence_2 = '❂'
