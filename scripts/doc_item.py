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
    print("----------------------------------------")
    print(itemdata["description"])
    print("----------------------------------------")
    print("Statistics")
    item_stats = itemdata["stats"]
    if item_stats["defence"] != 0:
        print(
            f"{pu.Colors.defence}+{item_stats['defence']} ❈ Defence{pu.Colors.reset}")
    if item_stats["health"] != 0:
        print(
            f"{pu.Colors.health}+{item_stats['health']} ❤ Health{pu.Colors.reset}")


doc_item("coat_of_arms_shield")
