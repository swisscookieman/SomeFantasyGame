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
    print("----------------------------------------")
    print(itemdata["description"])


doc_item("archer_bow")
