import json
import image_printer as image_printer


def load_save(savepath):
    f = open(savepath)
    playersave = json.load(f)

    print(f"\n{playersave['playername']} currently is level: {playersave['level']} with {playersave['xp']}xp towards next level\n")
    print("Currently owns the following items:")
    for item in playersave['owned_items']:
        print("\n----------------------------------------------------------------------\n")
        item_details = playersave['owned_items'][item]
        print(
            f"{item_details['amount']} {item_details['itemname']} with id {item_details['itemid']} of rarity \033[92m{item_details['rarity']}\033[0m")
        print(
            f"Item is currently enchanted with {item_details['enchant1']}, {item_details['enchant2']}, {item_details['enchant3']}")
        imagedir = "assets/items/equipment/" + item_details['itemid'] + ".png"
        image_printer.print_image(imagedir)


load_save("local/save.json")
