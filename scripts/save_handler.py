from scripts import printing_utility as pu
import json
import os

savetemplate_path = "data/save_template.json"
save_path = "data/local/save.json"

def new(savetemplate_path, save_path):
    if not os.path.exists(savetemplate_path):
        print(f"{pu.Colors.warning_yellow}Save template file not found: {savetemplate_path}{pu.Colors.reset}")
        return

    # Load data from the save template file
    with open(savetemplate_path, 'r') as source_file:
        source_data = json.load(source_file)
    if not os.path.exists(save_path):
        with open(save_path, 'w') as destination_file:
            json.dump(source_data, destination_file, indent=4)
            print(f"{pu.Colors.warning_yellow}New save file created: {save_path}{pu.Colors.reset}")
    else:
        # If the save file already exists, overwrite it
        with open(save_path, 'w') as destination_file:
            json.dump(source_data, destination_file, indent=4)
            print(f"{pu.Colors.warning_yellow}New save file created: {save_path}{pu.Colors.reset}")

    user_input = str(input("Name your character : "))
    with open(save_path, 'r') as file:
        data = json.load(file)
    data["playername"] = user_input
    with open(save_path, 'w') as file:
        json.dump(data, file, indent=4)

def get_save_data():
    with open("data/local/save.json") as file:
        data = json.load(file)
    return data

def get_items_data():
    with open("data/items.json") as file:
        data = json.load(file)
    return data