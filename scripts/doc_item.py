import json
import printing_utility as pu
import image_printer as imp

itemdata_path = "data/items.json"
items_assets_path = "assets/items"


def doc_item(id):
    with open(itemdata_path, 'r') as source_file:
        source_data = json.load(source_file)
    itemdata = source_data[id]
    print("\nDocumentation---------------------------")
    imp.print_image(items_assets_path + itemdata["file"])
    print("----------------------------------------")
    print(itemdata["itemname"], end=" | ")
    if itemdata["rarity_tier"] == "common":
        print("Common")
    if itemdata["rarity_tier"] == "rare":
        print(pu.Colors.rare + "Rare" + pu.Colors.reset)
    if itemdata["rarity_tier"] == "fabled":
        print(pu.Colors.fabled + "Fabled" + pu.Colors.reset)
    if itemdata["rarity_tier"] == "relic":
        print(pu.Colors.relic + "Relic" + pu.Colors.reset)
    print("----------------------------------------")
    print(itemdata["description"])
    print("----------------------------------------")
    print("Statistics")
    item_stats = itemdata["stats"]

    if item_stats["health"] != 0 or item_stats["phy_resistance"] != 0 or item_stats["magic_resistance"] != 0 or item_stats["ranged_resistance"] != 0:
        print(f"{pu.Style.italic}\n• Defensive Stats •{pu.Style.reset}")
    if item_stats["health"] != 0:
        print(
            f"{pu.Colors.health} +{item_stats['health']} {pu.Icons.health} Health{pu.Colors.reset}")
    if item_stats["phy_resistance"] != 0:
        print(
            f"{pu.Colors.defence} +{item_stats['phy_resistance']} {pu.Icons.strenght} Physical Resistance{pu.Colors.reset}")
    if item_stats["magic_resistance"] != 0:
        print(
            f"{pu.Colors.magic} +{item_stats['magic_resistance']} {pu.Icons.empty_star_4} Magic Resistance{pu.Colors.reset}")
    if item_stats["ranged_resistance"] != 0:
        print(
            f"{pu.Colors.ranged} +{item_stats['ranged_resistance']} {pu.Icons.circle} Ranged Resistance{pu.Colors.reset}")

    if item_stats["strenght"] != 0 or item_stats["magic_knowledge"] != 0 or item_stats["archery"] != 0 or item_stats["crit_chance"] != 0:
        print(f"{pu.Style.italic}\n• Offensive Stats •{pu.Style.reset}")
    if item_stats["strenght"] != 0:
        print(
            f"{pu.Colors.green} +{item_stats['strenght']} {pu.Icons.strenght} Strenght{pu.Colors.reset}")
    if item_stats["magic_knowledge"] != 0:
        print(
            f"{pu.Colors.magic} +{item_stats['magic_knowledge']} {pu.Icons.empty_star_4} Magic Knowledge{pu.Colors.reset}")
    if item_stats["archery"] != 0:
        print(
            f"{pu.Colors.ranged} +{item_stats['archery']} {pu.Icons.circle} Archery{pu.Colors.reset}")
    if item_stats["crit_chance"] != 0:
        print(
            f"{pu.Colors.pink} +{item_stats['crit_chance']} {pu.Icons.crit_chance} Crit Chance{pu.Colors.reset}")
    print(f"{pu.Style.italic}\n• Movement Stats •{pu.Style.reset}")
    if item_stats["speed"] != 0:
        print(
            f" +{item_stats['speed']} {pu.Icons.speed} Speed{pu.Colors.reset}")
    if item_stats["stealth"] != 0:
        print(
            f"{pu.Colors.stealth} +{item_stats['stealth']} {pu.Icons.heat} Stealth{pu.Colors.reset}")
    if item_stats["accuracy"] != 0:
        print(
            f"{pu.Colors.accuracy} +{item_stats['accuracy']} {pu.Icons.explosion} Accuracy{pu.Colors.reset}")
    print("----------------------------------------")

