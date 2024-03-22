import json
import new_printer as printer


def load_save(savepath):
    f = open(savepath)
    playersave = json.load(f)

    print(f"Player with name: {playersave['playername']}")
    print(
        f"Is currently level: {playersave['level']} with {playersave['xp']} towards next level")
    print("Currently owns the following items: -----------------")
    print(playersave['owned_items']['archer_bow_00001'])
    '''for item in playersave['owned_items']:
        print(
            f"Quantity {item.amount} of {item.itemname} with id {item.itemid} in rarity \033[92m{item.rarity}\033[0m")
        print(
            f"Item is currently enchanted with the enchants {item.enchant1}, {item.enchant2}, {item.enchant3}")
        imagedir = "assets/items/"+item.itemid+".png"
        printer.print_image(imagedir, "no_bg")'''


load_save("local/save.json")
