import image_printer as image_printer
import printing_utility as pu
import json

savepath = "local/save.json"

def load(savepath):
    f = open(savepath)
    playersave = json.load(f)

    print(f"\n{playersave['playername']} currently is level: {playersave['level']} with {playersave['xp']}xp towards next level\n")
    print("Currently owns the following items:")
    for item in playersave['owned_items']:
        print("\n----------------------------------------------------------------------\n")
        item_details = playersave['owned_items'][item]
        print(
            f"{item_details['amount']} {item_details['itemname']} with id {item_details['itemid']} of rarity {pu.Colors.green}{item_details['rarity']}{pu.Colors.reset}")
        print(
            f"Item is currently enchanted with {item_details['enchant1']}, {item_details['enchant2']}, {item_details['enchant3']}\n")
        imagedir = "assets/items/equipment/" + item_details['itemid'] + ".png"
        image_printer.print_image(imagedir)

def new(savepath): # Needs to overwrite any save to a fresh one. Could copy from a template that is in the github (local_save will be in gitignore)
    pass
