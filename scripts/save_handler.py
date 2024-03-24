import image_printer as image_printer
import printing_utility as pu
import json

savetemplate_path = "data/save_template.json"
save_path = "data/local/save.json"

def new(savetemplate_path, save_path):
    with open(savetemplate_path, 'r') as source_file:
        source_data = json.load(source_file)
    with open(save_path, 'w') as destination_file:
        json.dump(source_data, destination_file, indent=4)

new(savetemplate_path, save_path)