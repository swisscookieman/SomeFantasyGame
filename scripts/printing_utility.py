import animation
import time
import os
from PIL import Image
import random
import json

rare_drop = ['\033[96m  R', '  RA', '  RAR', '  RARE', '  RARE D', '  RARE DR', '  RARE DRO', '  RARE DROP',
             '<<RARE DROP>>', '  RARE DROP  ', '<<RARE DROP>>', '  RARE DROP  ', '<<RARE DROP>>', '  RARE DROP  ', '<<RARE DROP>>']

ultra_rare_drop = ['\033[95mULTRA', '      RARE',
                   '           DROP', '                      ', 'ULTRA RARE DROP', '                      ', 'ULTRA RARE DROP', '                      ', 'ULTRA RARE DROP', '                      ', 'ULTRA RARE DROP']

relic_drop = ["\033[93mR L C  R P", " E I  D O ", "R L C  R P",
              " E I  D O ", "R         ", "RE        ", "REL       ", "RELI      ", "RELIC     ", "RELIC D   ", "RELIC DR  ", "RELIC DRO ", "RELIC DROP", "          ", "RELIC DROP", "          ", "RELIC DROP", "          ", "RELIC DROP"]


itemdata_path = "data/items.json"
items_assets_path = "assets/items"
monsters_assets_path = "assets/monsters/"
monsterdata_path = "data/monsters.json"
lootdata_path = "data/loot_tables.json"


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
    relic = '\033[38;5;214m'
    darkgreen = '\033[38;5;28m'


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


def print_shop_title():
    print("|---------------------|")
    print("|  ___ _              |")
    print("| / __| |_  ___ _ __  |")
    print("| \__ \ ' \/ _ \ '_ \ |")
    print("| |___/_||_\___/ .__/ |")
    print("|              |_|    |")
    print("|---------------------|")


def print_stats_title():
    print("|-----------------------|")
    print("|  ___ _        _       |")
    print("| / __| |_ __ _| |_ ___ |")
    print("| \__ \  _/ _` |  _(_-< |")
    print("| |___/\__\__,_|\__/__/ |")
    print("|-----------------------|")


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


def print_image(image_path, print_mode="no_bg", color_r="", color_g="", color_b=""):
    try:
        # Open, resize image
        image = Image.open(open(image_path, 'rb')).convert('RGB')
        image = image.resize((16, 16))
        width, height = image.size

        for y in range(height):
            for x in range(width):
                r, g, b = image.getpixel((x, y))

                # Print with a checkboard behing
                if print_mode == "check":
                    if r == g == b == 0:
                        if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
                            print(f"\033[38;2;255;255;255m" + "██", end="")
                        if (x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1):
                            print(f"\033[38;2;180;180;180m" + "██", end="")
                    else:
                        color_code = f"\033[38;2;{r};{g};{b}m"
                        print(color_code + "██", end="")

                # Print with no bg
                if print_mode == "no_bg":
                    if r == g == b == 0:
                        print("  ", end="")
                    else:
                        color_code = f"\033[38;2;{r};{g};{b}m"
                        print(color_code + "██", end="")

                # Print with white bg
                if print_mode == "white":
                    if r == g == b == 0:
                        print(f"\033[38;2;255;255;255m" + "██", end="")
                    else:
                        color_code = f"\033[38;2;{r};{g};{b}m"
                        print(color_code + "██", end="")

                if print_mode == "custom":
                    if r == g == b == 0:
                        print(
                            f"\033[38;2;{color_r};{color_g};{color_b}m" + "██", end="")
                    else:
                        color_code = f"\033[38;2;{r};{g};{b}m"
                        print(color_code + "██", end="")

            print("\033[0m")

    except Exception as e:
        print("Error:", e)

    print("")


def print_scenary(image_path, print_mode="no_bg", color_r="", color_g="", color_b=""):
    try:
        # Open, resize image
        image = Image.open(open(image_path, 'rb')).convert('RGB')
        image = image.resize((48, 16))
        width, height = image.size

        for y in range(height):
            for x in range(width):
                r, g, b = image.getpixel((x, y))

                # Print with a checkboard behing
                if print_mode == "check":
                    if r == g == b == 0:
                        if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
                            print(f"\033[38;2;255;255;255m" + "██", end="")
                        if (x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1):
                            print(f"\033[38;2;180;180;180m" + "██", end="")
                    else:
                        color_code = f"\033[38;2;{r};{g};{b}m"
                        print(color_code + "██", end="")

                # Print with no bg
                if print_mode == "no_bg":
                    if r == g == b == 0:
                        print("  ", end="")
                    else:
                        color_code = f"\033[38;2;{r};{g};{b}m"
                        print(color_code + "██", end="")

                # Print with white bg
                if print_mode == "white":
                    if r == g == b == 0:
                        print(f"\033[38;2;255;255;255m" + "██", end="")
                    else:
                        color_code = f"\033[38;2;{r};{g};{b}m"
                        print(color_code + "██", end="")

                if print_mode == "custom":
                    if r == g == b == 0:
                        print(
                            f"\033[38;2;{color_r};{color_g};{color_b}m" + "██", end="")
                    else:
                        color_code = f"\033[38;2;{r};{g};{b}m"
                        print(color_code + "██", end="")

            print("\033[0m")

    except Exception as e:
        print("Error:", e)

    print("")


def doc_item(id):
    with open(itemdata_path, 'r') as source_file:
        source_data = json.load(source_file)
    itemdata = source_data[id]
    print("\nItem Documentation--------------------")
    print_image(items_assets_path + itemdata["file"])
    print("----------------------------------------")
    print(itemdata["itemname"], end=" | ")
    if itemdata["rarity_tier"] == "common":
        print("Common")
    if itemdata["rarity_tier"] == "rare":
        print(Colors.rare + "Rare" + Colors.reset)
    if itemdata["rarity_tier"] == "fabled":
        print(Colors.fabled + "Fabled" + Colors.reset)
    if itemdata["rarity_tier"] == "relic":
        print(Colors.relic + "Relic" + Colors.reset)
    print("----------------------------------------")
    print(itemdata["description"])
    print("----------------------------------------")
    print("Statistics")
    item_stats = itemdata["stats"]

    if item_stats["health"] != 0 or item_stats["phy_resistance"] != 0 or item_stats["magic_resistance"] != 0 or item_stats["ranged_resistance"] != 0:
        print(f"{Style.italic}\n• Defensive Stats •{Style.reset}")
    if item_stats["health"] != 0:
        print(
            f"{Colors.health} +{item_stats['health']} {Icons.health} Health{Colors.reset}")
    if item_stats["phy_resistance"] != 0:
        print(
            f"{Colors.defence} +{item_stats['phy_resistance']} {Icons.strenght} Physical Resistance{Colors.reset}")
    if item_stats["magic_resistance"] != 0:
        print(
            f"{Colors.magic} +{item_stats['magic_resistance']} {Icons.empty_star_4} Magic Resistance{Colors.reset}")
    if item_stats["ranged_resistance"] != 0:
        print(
            f"{Colors.ranged} +{item_stats['ranged_resistance']} {Icons.circle} Ranged Resistance{Colors.reset}")

    if item_stats["strenght"] != 0 or item_stats["magic_knowledge"] != 0 or item_stats["archery"] != 0 or item_stats["crit_chance"] != 0:
        print(f"{Style.italic}\n• Offensive Stats •{Style.reset}")
    if item_stats["strenght"] != 0:
        print(
            f"{Colors.green} +{item_stats['strenght']} {Icons.strenght} Strenght{Colors.reset}")
    if item_stats["magic_knowledge"] != 0:
        print(
            f"{Colors.magic} +{item_stats['magic_knowledge']} {Icons.empty_star_4} Magic Knowledge{Colors.reset}")
    if item_stats["archery"] != 0:
        print(
            f"{Colors.ranged} +{item_stats['archery']} {Icons.circle} Archery{Colors.reset}")
    if item_stats["crit_chance"] != 0:
        print(
            f"{Colors.pink} +{item_stats['crit_chance']} {Icons.crit_chance} Crit Chance{Colors.reset}")
    print(f"{Style.italic}\n• Movement Stats •{Style.reset}")
    if item_stats["speed"] != 0:
        if item_stats["speed"] > 0:
            print(
                f" +{item_stats['speed']} {Icons.speed} Speed{Colors.reset}")
        elif item_stats["speed"] < 0:
            print(
                f" {item_stats['speed']} {Icons.speed} Speed{Colors.reset}")
    if item_stats["stealth"] != 0:
        print(
            f"{Colors.stealth} +{item_stats['stealth']} {Icons.heat} Stealth{  Colors.reset}")
    if item_stats["accuracy"] != 0:
        if item_stats["accuracy"] > 0:
            print(
                f"{Colors.accuracy} +{item_stats['accuracy']} {Icons.explosion} Accuracy{Colors.reset}")
        if item_stats["accuracy"] < 0:
            print(
                f"{Colors.accuracy} {item_stats['accuracy']} {Icons.explosion} Accuracy{Colors.reset}")
    print("----------------------------------------")


def print_stats():
    # stats loading code here
    health = 100
    phy_resistance = 100
    magic_resistance = 100
    ranged_resistance = 100
    strenght = 100
    magic_knowledge = 100
    archery = 100
    crit_chance = 100
    speed = 100
    stealth = 100
    accuracy = 100

    print("\nStatistics---------------------------")

    print(f"{Style.italic}\n• Defensive Stats •{Style.reset}")
    print(
        f"{Colors.health} {health} {Icons.health} Health{Colors.reset}")
    print(
        f"{Colors.defence} {phy_resistance} {Icons.strenght} Physical Resistance{Colors.reset}")
    print(
        f"{Colors.magic} {magic_resistance} {Icons.empty_star_4} Magic Resistance{Colors.reset}")
    print(
        f"{Colors.ranged} {ranged_resistance} {Icons.circle} Ranged Resistance{Colors.reset}")

    print(f"{Style.italic}\n• Offensive Stats •{Style.reset}")
    print(
        f"{Colors.green} {strenght} {Icons.strenght} Strenght{Colors.reset}")
    print(
        f"{Colors.magic} {magic_knowledge} {Icons.empty_star_4} Magic Knowledge{Colors.reset}")
    print(
        f"{Colors.ranged} {archery} {Icons.circle} Archery{Colors.reset}")
    print(
        f"{Colors.pink} {crit_chance} {Icons.crit_chance} Crit Chance{Colors.reset}")

    print(f"{Style.italic}\n• Movement Stats •{Style.reset}")
    print(
        f" {speed} {Icons.speed} Speed{Colors.reset}")
    print(
        f"{Colors.stealth} {stealth} {Icons.heat} Stealth{  Colors.reset}")
    print(
        f"{Colors.accuracy} {accuracy} {Icons.explosion} Accuracy{Colors.reset}")
    print("----------------------------------------")


def progressbar(current, goal, size=20):
    # to do: handle when current is bigger than goal
    toprint = "\033[37;1m["
    percentage = current/goal
    green = size*percentage
    green = round(green)
    black = size - green

    for i in range(green):
        toprint = toprint + "\033[92m|"
    for i in range(black):
        toprint = toprint + "\033[38;5;18m|"
    toprint = toprint + "\033[37;1m]\033[0m"
    print(toprint)


def id_to_text(text):
    words = text.split('_')
    transformed_words = [word.capitalize() for word in words]
    return ' '.join(transformed_words)


def print_loot_table(tablename):
    with open(lootdata_path, 'r') as source_file:
        source_data = json.load(source_file)
    lootdata = source_data[tablename]
    print(f"\nLoot Table : {id_to_text(tablename)}")
    maxitemlen = 0
    maxdroplen = 0
    for item in lootdata:
        if len(item) > maxitemlen:
            maxitemlen = len(item)
        if len(str(lootdata[item])) > maxdroplen:
            maxdroplen = len(str(lootdata[item]))
    top = f"┏-{maxitemlen*'-'}---{maxdroplen*'-'}------┓"
    bottom = f"┗-{maxitemlen*'-'}---{maxdroplen*'-'}------┛"
    print(top)
    for item in lootdata:
        itemspaces = (maxitemlen - len(item))*" "
        dropspaces = (maxdroplen+1 - len(str(lootdata[item]))) * " "
        print(
            f"| {id_to_text(item)}{itemspaces} | {lootdata[item]}/1000{dropspaces}|")
    print(bottom)


def doc_monster(monstername):
    with open(monsterdata_path, 'r') as source_file:
        source_data = json.load(source_file)
    monsterdata = source_data[monstername]
    print("\nItem Documentation--------------------\n")
    print_image(monsterdata["image_file"])
    print("----------------------------------------")
    print(monsterdata["name"], end=" | ")
    if monsterdata["zone"] == "forest":
        print(f"{Colors.darkgreen}The Forest{Colors.reset}")
    print("----------------------------------------")
    print(monsterdata["description"])
    print("----------------------------------------")
    print("\nStatistics---------------------------")
    monsterdata = monsterdata["stats"]
    print(f"{Style.italic}\n• Defensive Stats •{Style.reset}")
    print(
        f"{Colors.health} {monsterdata['health']} {Icons.health} Health{Colors.reset}")
    print(
        f"{Colors.defence} {monsterdata['phy_resistance']} {Icons.strenght} Physical Resistance{Colors.reset}")
    print(
        f"{Colors.magic} {monsterdata['magic_resistance']} {Icons.empty_star_4} Magic Resistance{Colors.reset}")
    print(
        f"{Colors.ranged} {monsterdata['ranged_resistance']} {Icons.circle} Ranged Resistance{Colors.reset}")

    print(f"{Style.italic}\n• Offensive Stats •{Style.reset}")
    print(
        f"{Colors.green} {monsterdata['strenght']} {Icons.strenght} Strenght{Colors.reset}")
    print(
        f"{Colors.magic} {monsterdata['magic_knowledge']} {Icons.empty_star_4} Magic Knowledge{Colors.reset}")
    print(
        f"{Colors.ranged} {monsterdata['archery']} {Icons.circle} Archery{Colors.reset}")
    print(
        f"{Colors.pink} {monsterdata['crit_chance']} {Icons.crit_chance} Crit Chance{Colors.reset}")

    print(f"{Style.italic}\n• Movement Stats •{Style.reset}")
    print(
        f" {monsterdata['speed']} {Icons.speed} Speed{Colors.reset}")
    print(
        f"{Colors.stealth} {monsterdata['stealth']} {Icons.heat} Stealth{  Colors.reset}")
    print(
        f"{Colors.accuracy} {monsterdata['accuracy']} {Icons.explosion} Accuracy{Colors.reset}")
    print("----------------------------------------")


'''
Max health (base 100 max 1000)
Physical resistance (base 0 max 100) phy damage reduction %  
Magic resistance (base 0 max 100) mag dmg reduction %  
Ranged resistance (base 0 max 100) mag dmg reduction %    

Strenght (base 100 max 1000) increases physical damage  
Magic knowledge (base 100 max 1000) increases magic damage  
Archery (base 100 max 1000) increases ranged dmg
crit chance (base 10 max 100) chance to x2 dmg

Stealth (base 0 max 100) chance for enemy attack to miss  
Accuracy (base 80 max 200) chance for attack to hit  
speed (base 100 max 1000) increases hits per sec  
'''


def run_attack(attackeraccuracy, attackerpowervalue, defenderresistancevalue, defenderstealth, attackercritchance):
    multiplier = 1
    # this calculates whether this attack will hit, and if 2 times (acc > 100)
    if attackeraccuracy >= 100:
        accuracyrandom = random.randint(101, 200)
        if accuracyrandom > attackeraccuracy:
            multiplier = 1
            isaccurate = True
        elif accuracyrandom <= attackeraccuracy:
            multiplier = 2
            isaccurate = True
    elif attackeraccuracy < 100:
        accuracyrandom = random.randint(1, 100)
        if accuracyrandom > attackeraccuracy:
            isaccurate = False
        elif accuracyrandom <= attackeraccuracy:
            isaccurate = True
    # this calculates whether the attack will be dodged
    stealthrandom = random.randint(1, 100)
    if stealthrandom > defenderstealth:
        willdodge = False
    elif stealthrandom <= defenderstealth:
        willdodge = True
    # this calculates whether the attack will crit
    critrandom = random.randint(1, 100)
    if critrandom > attackercritchance:
        multiplier = multiplier
    if critrandom <= attackercritchance:
        multiplier = multiplier*2
    # this calculates damage dealt
    dmg = (attackerpowervalue*((100-defenderresistancevalue)/100))
    dmgaftermulti = dmg*multiplier
    if isaccurate and not willdodge:
        finaldmg = dmgaftermulti
    else:
        finaldmg = 0
    print(
        f"attack is accurate: {isaccurate}, attack dodged: {willdodge}, attack multiplier: x{multiplier}, attackdmg: {dmgaftermulti}, finalreturned dmg {finaldmg}")


run_attack(100, 100, 20, 0, 100)
